import struct
import re

def consume_byte(content, offset, byte, length=1):
    """Consume length bytes from content, starting at offset. If they
     are not all byte, raises a ValueError.
    """
    
    for i in xrange(0, length-1):
        if content[offset + i] != byte:
            raise ValueError("Expected byte '" + byte.encode("hex") + "' at offset " +\
                    hex(offset + i) + " but received byte '" +\
                    content[offset + i].encode("hex") + "'.")
    return offset + length

def unpack_arg_array(content, command_class, command_index, offset, length):
    """Unpacks packed binary data in content as though it is the argument
    array for the command given by command_class and command_index.
    Only the portion of content given starting at offset of the given length
    is unpacked.
    
    If length exceeds the length of the argument array for the command, 
    the remaining bytes will be unpacked as unsigned ints.
    
    Returns the format string used for the unpacking (with any extra
    unspecified arguments separated by a |) and a list of the arguments.
    """
    if length == 0:
        return ("" , [ ])
    trimmed_struct_format = emevd_handler.COMMAND_ARG_TYPE_DICT[command_class][command_index][1:]
    struct_format = emevd_handler.COMMAND_ARG_TYPE_DICT[command_class][command_index] + "0i"
    struct_size = struct.calcsize(struct_format)
    if struct_size > length:
        raise ValueError("Struct too large. Content size: " + str(length) + \
            ", struct size: " + str(struct_size))
    args_from_struct = struct.unpack_from(struct_format, content, offset=offset)
    offset += struct_size
    
    extra_length = length - struct_size
    varargs = [struct.unpack_from("<I", content, offset=(offset + j))[0] for j in xrange(0, extra_length, 4)]
    if extra_length > 0:
        return (trimmed_struct_format + "|" + "I" * (extra_length / 4), [s for s in args_from_struct] + varargs)
    else:
        return (trimmed_struct_format, [s for s in args_from_struct])

def emevd_file_content_to_event_list(file_content):
    """Parses the binary data in file_content as a .emevd file. Returns
    the list of Events in the file. Raises a ValueError if file_content
    appears to be malformed or un-parseable.
    """
    
    event_list = []
    
    master_offset = 0
    
    master_offset = consume_byte(file_content, master_offset, '\x45', 1)
    master_offset = consume_byte(file_content, master_offset, '\x56', 1)
    master_offset = consume_byte(file_content, master_offset, '\x44', 1)
    master_offset = consume_byte(file_content, master_offset, '\x00', 1)
    
    master_offset = consume_byte(file_content, master_offset, '\x00', 4)
    
    master_offset = consume_byte(file_content, master_offset, '\xCC', 1)
    master_offset = consume_byte(file_content, master_offset, '\x00', 1)
    master_offset = consume_byte(file_content, master_offset, '\x00', 1)
    master_offset = consume_byte(file_content, master_offset, '\x00', 1)
         
    (file_size,) = struct.unpack_from("<I", file_content, offset=master_offset)
    master_offset += struct.calcsize("<I")
    
    (event_count, event_count_offset) = struct.unpack_from("<II", file_content, offset=master_offset)
    master_offset += struct.calcsize("<II")
    (instr_count, instr_offset) = struct.unpack_from("<II", file_content, offset=master_offset)
    master_offset += struct.calcsize("<II")
    (_, _) = struct.unpack_from("<II", file_content, offset=master_offset)
    master_offset += struct.calcsize("<II")
    (_, _) = struct.unpack_from("<II", file_content, offset=master_offset)
    master_offset += struct.calcsize("<II")
    (dynarg_count, dynarg_offset) = struct.unpack_from("<II", file_content, offset=master_offset)
    master_offset += struct.calcsize("<II")
    (_, _) = struct.unpack_from("<II", file_content, offset=master_offset)
    master_offset += struct.calcsize("<II")
    (fixarg_length, fixarg_offset) = struct.unpack_from("<II", file_content, offset=master_offset)
    master_offset += struct.calcsize("<II")
    (_, _) = struct.unpack_from("<II", file_content, offset=master_offset)
    master_offset += struct.calcsize("<II")
   
    master_offset = event_count_offset
    for i in xrange(event_count):
        (event_id, num_of_instr, starting_instr_offset, num_of_dynarg, \
            starting_dynarg_offset, unknown_int, zero) = struct.unpack_from("<IIIIiII", file_content, offset=master_offset)
        master_offset += struct.calcsize("<IIIIiII")

        offset = instr_offset + starting_instr_offset
        instr_list = []
        for i in xrange(num_of_instr):
            (instr_class, instr_index, fixarg_bytes, starting_fixarg_offset, \
                neg_one, zero) = struct.unpack_from("<IIIIiI", file_content, offset=offset)
            offset += struct.calcsize("<IIIIiI")
            
            if neg_one != -1 or zero != 0:
                raise ValueError("Expected final constant bytes [-1 0]. Read [" + \
                    str(neg_one) + " " + str(zero) + "].")
            
            (instr_format_string, instr_arg_list) = unpack_arg_array(file_content, instr_class, instr_index, \
                fixarg_offset + starting_fixarg_offset, fixarg_bytes)
            
            instr = emevd_handler.Instruction(instr_class, instr_index, instr_format_string, instr_arg_list, [])
            instr_list.append(instr)
            
        offset = dynarg_offset + starting_dynarg_offset
        for _ in xrange(num_of_dynarg):
            (instr_index, destination_starting_byte, source_starting_byte, \
                num_of_bytes, zero) = struct.unpack_from("<IIIII", file_content, offset=offset)
            offset += struct.calcsize("<IIIII")
            
            param = emevd_handler.ParameterReplacement(instr_index, destination_starting_byte, source_starting_byte, num_of_bytes)
            instr_list[instr_index].append_parameter_replacement(param)
            
        event = emevd_handler.Event(event_id, unknown_int, instr_list)
        event_list.append(event)
    return event_list
    
def raw_numeric_file_content_to_event_list(file_content):
    """Parses the text data in file_content as though it is of the form
    emitted by exporting a .emevd file as raw numeric data, and returns
    a list of Events. Raises a ValueError if file_content appears 
    malformed or un-parsable.
    """
    
    text_events = re.split(r'\n{2,}', file_content)
    
    event_list = []
    for text_event in text_events:
        event_lines = text_event.splitlines()
        header_line = event_lines[0]
        m = re.match(r"^(\d+), (0|1|2)", header_line)
        if not m:
            raise ValueError("Error parsing header line: \"" + header_line + "\".")
        event_id = int(m.group(1))
        unknown_int = int(m.group(2))
        
        instr_list = []
        for instr_or_param in event_lines[1:]:
            m_instr = re.match(r" [ ]*(\d+)\[(\d+)\] \(([iIhHbBf\|]*)\)\[([\d, \.-]*)\]", instr_or_param)
            m_param = re.match(r" [ ]*\^\((\d+) <- (\d+), (\d+)\)", instr_or_param)
            
            if m_instr:
                # Parse the line as an instruction.
                instr_class = int(m_instr.group(1))
                instr_index = int(m_instr.group(2))
                arg_format_string = m_instr.group(3)
                arg_list_string = m_instr.group(4)
               
                # Check the argument list against the format_string.
                split_arg_list = arg_list_string.split(",")
                trimmed_format_string = arg_format_string.translate(None, "|")
                if split_arg_list == ['']:
                    split_arg_list = []
                if len(trimmed_format_string) != len(split_arg_list):
                    raise ValueError("Length mismatch between format string (" + arg_format_string +\
                     ") and argument array [" + arg_list_string + "]")
                argument_list = []
                for i, char in enumerate(trimmed_format_string):
                    arg = split_arg_list[i]
                    if char == 'f':
                        argument_list.append(float(arg))
                        
                    CHAR_BOUNDS = {'b': (-128, 127), 'B': (0, 255), 'h': (-32768, 32767), \
                        'H': (0, 65535), 'i': (-2147483648, 2147483647), 'I': (0, 4294967295)}
                    if char in CHAR_BOUNDS:
                        (min_val, max_val) = CHAR_BOUNDS[char]
                        parsed_arg = int(arg)
                        if min_val <= parsed_arg and parsed_arg <= max_val:
                            argument_list.append(parsed_arg)
                        else:
                            raise ValueError("Argument \"" + arg + "\" is not inside the bounds for format specifier \"" + char + "\".")
                instr = emevd_handler.Instruction(instr_class, instr_index, arg_format_string, argument_list, [])
                instr_list.append(instr)
            elif m_param:
                if len(instr_list) >= 1:
                    # Parse the line as a parameter replacement for the previous line.
                    dest_byte = int(m_param.group(1))
                    source_byte = int(m_param.group(2))
                    length = int(m_param.group(3))
                    
                    param = emevd_handler.ParameterReplacement(len(instr_list)-1, dest_byte, source_byte, length)
                    instr_list[-1].append_parameter_replacement(param)
                else:
                    # Orphaned parameter line.
                    raise ValueError("Parameter replacement \"" + instr_or_param + "\" does not have an instruction to attach to.")
            else:
                # Malformed line.
                raise ValueError("Line \"" + instr_or_param + "\" cannot be parsed as a instruction or parameter replacement.")
        parsed_event = emevd_handler.Event(event_id, unknown_int, instr_list)
        event_list.append(parsed_event)
    return event_list
        
    
import emevd_handler
