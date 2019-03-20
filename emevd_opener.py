import struct
import re
import copy
import os

from emevd_handler import EVD_FileType
import serialize_edf
import dcx_handler

EDF_JSON_DIR = "EventScriptResources"
FILETYPE_JSON_DICT = {
    EVD_FileType.DARK_SOULS_1: os.path.join(EDF_JSON_DIR, "ds1-common.emedf.json"),
    EVD_FileType.BLOODBORNE: os.path.join(EDF_JSON_DIR, "bb-common.emedf.json"),
    EVD_FileType.DARK_SOULS_3_TEST: os.path.join(EDF_JSON_DIR, "ds3test-common.emedf.json"),
    EVD_FileType.DARK_SOULS_3: os.path.join(EDF_JSON_DIR, "ds3-common.emedf.json")
}

MEMOIZED_EDF_DATA = {}

def get_edf_data(filetype):
    if filetype in MEMOIZED_EDF_DATA:
        return MEMOIZED_EDF_DATA[filetype]
    else:
        MEMOIZED_EDF_DATA[filetype] = {}
        emedf_json = open(FILETYPE_JSON_DICT[filetype], "r").read()
        edf_data = serialize_edf.Serializeable_EDF_Struct.deserialize(emedf_json)
        MEMOIZED_EDF_DATA[filetype]["arg_type"] = edf_data.build_type_dict()
        MEMOIZED_EDF_DATA[filetype]["instr_string"] = edf_data.build_instruction_string_dict()
        MEMOIZED_EDF_DATA[filetype]["enum_list"] = edf_data.enums
        return MEMOIZED_EDF_DATA[filetype]
        
def get_arg_type_dict(filetype):
    return get_edf_data(filetype)["arg_type"]
    
def get_instr_string_dict(filetype):
    return get_edf_data(filetype)["instr_string"]
    
def get_enum_list(filetype):
    return get_edf_data(filetype)["enum_list"]
    

def consume_byte(content, offset, byte, length=1):
    """Consume length bytes from content, starting at offset. If they
     are not all byte, raises a ValueError.
    """
    
    for i in range(length-1):
        if content[offset + i:offset + i+1] != byte:
            raise ValueError(("Expected byte '0x%s' at offset " + 
             "0x%x but received byte '0x%s'.") % (byte.hex(), offset+i, 
             content[offset + i:offset + i+1].hex()))
    return offset + length

def unpack_arg_array(content, command_class, command_index, offset, length, filetype):
    """Unpacks packed binary data in content as though it is the argument
    array for the command given by command_class and command_index.
    Only the portion of content given starting at offset of the given length
    is unpacked.
    
    If length exceeds the length of the argument array for the command, 
    the remaining bytes will be unpacked as unsigned ints.
    
    Returns the format string used for the unpacking (with any extra
    unspecified arguments separated by a |) and a list of the arguments.
    """
    
    arg_type_dict = get_arg_type_dict(filetype)
    
    if length == 0:
        return ("" , [ ])
    if (command_class not in arg_type_dict or command_index not in arg_type_dict[command_class]):
        struct_size = struct.calcsize("@" + str(length) + "B0i" )
        args_from_struct = struct.unpack_from(str(length) + "B", content, offset=offset)
        offset += struct_size
        return (length * "x", ["0x%02x" % s for s in args_from_struct])
    else:
        # We replace "s" with "I" because strings are actually pointers into the string table,
        #  not strings themselves. However, we still need to return the format string containing
        #  the "s" so that the formatter can recognize that those arguments should perform string
        #  table lookups.
        trimmed_struct_format = arg_type_dict[command_class][command_index][1:]
        struct_format = arg_type_dict[command_class][command_index] + "0i"
        struct_size = struct.calcsize(struct_format.replace("s", "I"))
        if struct_size > length:
            raise ValueError("Struct too large in instruction %d[%02d]. Content size: %d, struct size: %d" %
             (command_class, command_index, length, struct_size))
        args_from_struct = struct.unpack_from(struct_format.replace("s", "I"), content, offset=offset)
        
        # Test to make sure only \x00 is used as a padding byte.
        #  If not, struct_format has probably missed a field.
        repack = struct.pack(struct_format.replace("s", "I"), *args_from_struct)
        if content[offset : offset + struct_size] != repack:
            raise ValueError("Nonzero pad byte in argument array for instruction of type %d[%02d].\nReceived bytes: %s\nExpected bytes: %s" %
             (command_class, command_index, str(content[offset : offset + struct_size]), str(repack)))
        
        offset += struct_size
        extra_length = length - struct_size
        varargs = [struct.unpack_from("<I", content, offset=(offset + j))[0] for j in range(0, extra_length, 4)]
        if extra_length > 0:
            return (trimmed_struct_format + "|" + "I" * (extra_length // 4), [s for s in args_from_struct] + varargs)
        else:
            return (trimmed_struct_format, [s for s in args_from_struct])

def emevd_file_content_to_event_list(file_content, filetype_override = None):
    """Parses the binary data in file_content as a .emevd file. Returns
    the list of Events in the file. Raises a ValueError if file_content
    appears to be malformed or un-parseable.
    
    Filetype is (mostly) automatically detected using header information,
    but can be overridden by passing a EVD_Filetype value as filetype_override.
    """
    
    filetype = filetype_override
    event_list = []
    
    should_dcx = False
    if dcx_handler.appears_dcx(file_content):
        tmp = dcx_handler.uncompress_dcx_content(file_content)
        file_content = tmp
        should_dcx = True
    
    master_offset = 0
    
    master_offset = consume_byte(file_content, master_offset, '\x45', 1)
    master_offset = consume_byte(file_content, master_offset, '\x56', 1)
    master_offset = consume_byte(file_content, master_offset, '\x44', 1)
    master_offset = consume_byte(file_content, master_offset, '\x00', 1)
    
    (version_part_1, version_part_2) = struct.unpack_from("<II", file_content, offset=master_offset)
    master_offset += struct.calcsize("<II")
    
    # Determine filetype from version bytes, if not overriden.
    if filetype == None:
        if version_part_1 == 0x00000000 and version_part_2 == 0x000000CC:
            filetype = EVD_FileType.DARK_SOULS_1
        elif version_part_1 == 0x0000FF00 and version_part_2 == 0x000000CC:
            # We cannot tell the difference between BB and DS3Test from the header,
            #  so default to BB unless the user forces an override.
            filetype = EVD_FileType.BLOODBORNE
        elif version_part_1 == 0x0001FF00 and version_part_2 == 0x000000CD:
            filetype = EVD_FileType.DARK_SOULS_3
        else:
            raise ValueError(("Unrecognized version bytes %08x %08x." + 
                "Could not determine EVD version.") % (version_part_1, version_part_2))
         
    (file_size,) = struct.unpack_from("<I", file_content, offset=master_offset)
    master_offset += struct.calcsize("<I")
    
    header_pair_format_string = "<II"
    if filetype == EVD_FileType.DARK_SOULS_1:
        header_pair_format_string = "<II"
    elif (filetype == EVD_FileType.BLOODBORNE or 
     filetype == EVD_FileType.DARK_SOULS_3_TEST or 
     filetype == EVD_FileType.DARK_SOULS_3):
        header_pair_format_string = "<QQ"
    
    (event_count, event_offset) = struct.unpack_from(header_pair_format_string, file_content, offset=master_offset)
    master_offset += struct.calcsize(header_pair_format_string)
    (instr_count, instr_offset) = struct.unpack_from(header_pair_format_string, file_content, offset=master_offset)
    master_offset += struct.calcsize(header_pair_format_string)
    
    # This table is unused in known formats, so it always has 0 count and dummy offset.
    (_, _) = struct.unpack_from(header_pair_format_string, file_content, offset=master_offset)
    master_offset += struct.calcsize(header_pair_format_string)
    
    (eventlayer_count, eventlayer_offset) = struct.unpack_from(header_pair_format_string, file_content, offset=master_offset)
    master_offset += struct.calcsize(header_pair_format_string)
    (dynarg_count, dynarg_offset) = struct.unpack_from(header_pair_format_string, file_content, offset=master_offset)
    master_offset += struct.calcsize(header_pair_format_string)
    (linked_files_count, linked_files_offset) = struct.unpack_from(header_pair_format_string, file_content, offset=master_offset)
    master_offset += struct.calcsize(header_pair_format_string)
    (fixarg_length, fixarg_offset) = struct.unpack_from(header_pair_format_string, file_content, offset=master_offset)
    master_offset += struct.calcsize(header_pair_format_string)
    (strings_length, strings_offset) = struct.unpack_from(header_pair_format_string, file_content, offset=master_offset)
    master_offset += struct.calcsize(header_pair_format_string)
   
    master_offset = event_offset
    for i in range(event_count):
        event_reset_mode = 0
        if filetype == EVD_FileType.DARK_SOULS_1:
            (event_id, num_of_instr, starting_instr_offset, num_of_dynarg,
                starting_dynarg_offset, event_reset_mode, zero) = struct.unpack_from("<IIIIiII", file_content, offset=master_offset)
            master_offset += struct.calcsize("<IIIIiII")
        elif filetype == EVD_FileType.BLOODBORNE or filetype == EVD_FileType.DARK_SOULS_3_TEST:
            (event_id, num_of_instr, starting_instr_offset, num_of_dynarg,
                starting_dynarg_offset, event_reset_mode, zero) = struct.unpack_from("<QQQQqII", file_content, offset=master_offset)
            master_offset += struct.calcsize("<QQQQi4xII")
        elif filetype == EVD_FileType.DARK_SOULS_3:
            (event_id, num_of_instr, starting_instr_offset, num_of_dynarg,
                starting_dynarg_offset, event_reset_mode, zero) = struct.unpack_from("<QQQQqII", file_content, offset=master_offset)
            master_offset += struct.calcsize("<QQQQqII")
        if zero != 0:
            raise ValueError("Event terminator zero was expected for event ID %d, but received %d instead." % (event_id, zero))

        offset = instr_offset + starting_instr_offset
        instr_list = []
        for i in range(num_of_instr):
            complain_about_zero = False
            if filetype == EVD_FileType.DARK_SOULS_1:
                (instr_class, instr_index, fixarg_bytes, starting_fixarg_offset,
                    starting_eventlayer_offset, zero) = struct.unpack_from("<IIIiiI", file_content, offset=offset)
                if zero != 0:
                    complain_about_zero = True
                offset += struct.calcsize("<IIIiiI")
            elif filetype == EVD_FileType.BLOODBORNE or filetype == EVD_FileType.DARK_SOULS_3_TEST:
                (instr_class, instr_index, fixarg_bytes, starting_fixarg_offset, \
                    starting_eventlayer_offset, zero) = struct.unpack_from("<IIQi4xiI", file_content, offset=offset)
                if zero != 0:
                    complain_about_zero = True
                offset += struct.calcsize("<IIQi4xi4x")
            elif filetype == EVD_FileType.DARK_SOULS_3:
                (instr_class, instr_index, fixarg_bytes, starting_fixarg_offset,
                    starting_eventlayer_offset) = struct.unpack_from("<IIQi4xq", file_content, offset=offset)
                offset += struct.calcsize("<IIQi4xq")
            if complain_about_zero:
                raise ValueError(("Instruction terminator zero was expected for " + 
                    "instruction %d[%03d] of event ID %d, but received %d instead.") % 
                    (instr_class, instr_index, event_id, zero))
            
            # Parse Event Layer
            eventlayer = None
            if starting_eventlayer_offset != -1:
                # Known examples have a very strict format. If something deviates from this, we should look into it.
                if filetype == EVD_FileType.DARK_SOULS_1:
                    # This is a guess, since DS1 never uses the event layer field.
                    (two, eventlayer, zero, neg_one, one) = struct.unpack_from("<IIIiI", file_content, 
                        offset=eventlayer_offset+starting_eventlayer_offset)
                elif (filetype == EVD_FileType.BLOODBORNE or 
                 filetype == EVD_FileType.DARK_SOULS_3_TEST or 
                 filetype == EVD_FileType.DARK_SOULS_3):
                    # This is partially a guess, since BB/DS3T never uses the event layer field.
                    (two, eventlayer, zero, neg_one, one) = struct.unpack_from("<IIQqQ", file_content, 
                        offset=eventlayer_offset+starting_eventlayer_offset)
                if two != 2:
                    ValueError("Event Layer @ %08x initializer 2 was expected but received %d instead." %
                        (eventlayer_offset+starting_eventlayer_offset, two))
                if zero != 0:
                    raise ValueError("Event Layer @ %08x terminator zero was expected but received %d instead." %
                        (eventlayer_offset+starting_eventlayer_offset, zero))
                if neg_one != -1:
                    raise ValueError("Event Layer @ %08x terminator -1 was expected but received %d instead." %
                        (eventlayer_offset+starting_eventlayer_offset, neg_one))
                if one != 1:
                    raise ValueError("Event Layer @ %08x terminator 1 was expected but received %d instead." %
                        (eventlayer_offset+starting_eventlayer_offset, one))
            
            (instr_format_string, instr_arg_list) = unpack_arg_array(file_content, instr_class, instr_index,
                fixarg_offset + starting_fixarg_offset, fixarg_bytes, filetype)
            
            instr = emevd_handler.Instruction(instr_class, instr_index, instr_format_string, instr_arg_list, [], eventlayer)
            instr_list.append(instr)
        
        offset = dynarg_offset + starting_dynarg_offset
        for i in range(num_of_dynarg):
            if filetype == EVD_FileType.DARK_SOULS_1:
                (instr_index, destination_starting_byte, source_starting_byte, \
                    num_of_bytes, zero) = struct.unpack_from("<IIIII", file_content, offset=offset)
                offset += struct.calcsize("<IIIII")
                if zero != 0:
                    raise ValueError(("Parameter replacement #%d terminator zero" + 
                        " was expected but received %d instead.") % (i, zero))
            elif (filetype == EVD_FileType.BLOODBORNE or 
             filetype == EVD_FileType.DARK_SOULS_3_TEST or 
             filetype == EVD_FileType.DARK_SOULS_3):
                (instr_index, destination_starting_byte, source_starting_byte,
                    num_of_bytes) = struct.unpack_from("<QQQQ", file_content, offset=offset)
                offset += struct.calcsize("<QQQQ")
            param = emevd_handler.ParameterReplacement(instr_index, destination_starting_byte, source_starting_byte, num_of_bytes)
            instr_list[instr_index].append_parameter_replacement(param)
            
        event = emevd_handler.Event(event_id, event_reset_mode, instr_list)
        event_list.append(event)
    
    strings = b""
    if strings_length != 0:
        strings = file_content[strings_offset:strings_offset + strings_length]
    
    master_offset = linked_files_offset
    linked_files_list = []
    for i in range(linked_files_count):
        if filetype == EVD_FileType.DARK_SOULS_1:
            # DS1 never uses linked files, but why not attempt to support it?
            (linked_files_name_offset,) = struct.unpack_from("<I", file_content, offset=master_offset)
            linked_files_list.append(linked_files_name_offset)
        elif (filetype == EVD_FileType.BLOODBORNE or 
         filetype == EVD_FileType.DARK_SOULS_3_TEST or 
         filetype == EVD_FileType.DARK_SOULS_3):
            (linked_files_name_offset,) = struct.unpack_from("<Q", file_content, offset=master_offset)
            linked_files_list.append(linked_files_name_offset)
    return (filetype, event_list, strings, linked_files_list, should_dcx)
    
def raw_numeric_file_content_to_event_list(file_content, filetype_override = None):
    """Parses the text data in file_content as though it is of the form
    emitted by exporting a .emevd file as raw numeric data, and returns
    a list of Events. Raises a ValueError if file_content appears 
    malformed or un-parsable.
    
    Filetype is automatically parsed using header information,
    but can be overridden by passing a EVD_Filetype value as filetype_override,
    if needed.
    """
    
    # 'Cheap' state information, since states are forgetful and can be
    #  flushed upon state change.
    filetype = None
    should_dcx = False
    
    event_list = []
    current_event_id = 0
    current_event_reset_mode = 0
    current_event_instrs = []
    
    strings = b""
    current_strings_offset = 0
    
    linked_files = []
    
    # State
    mode = ""
    
    lines = file_content.splitlines()
    for (line_num, line) in enumerate(lines):
        # Check for string table entries before stripping comments and whitespace.
        m_string_entry = re.match(r"^(\d+): (.*)", line)
        if mode == "string_table" and m_string_entry:
            offset = int(m_string_entry.group(1))
            if offset < current_strings_offset:
                raise ValueError(("Line %d: Offset in string table is incorrect." + 
                    "Expected %d but received %d.") % (line_num, current_strings_offset, offset))
            if filetype == EVD_FileType.DARK_SOULS_1:
                s = m_string_entry.group(2).encode("ascii") + b"\x00" # Add NUL.
            else:
                s = m_string_entry.group(2).encode("utf-16le") + b"\x00\x00" # Add UTF-16 NUL.
            strings += s
            current_strings_offset += len(s)
        else:
            # Strip comments and whitespace.
            m_comment = re.match(r"^([^#]*)#(.*)$", line)
            if m_comment:
                line = m_comment.group(1)
            line = "".join(line.split())
            
            # Skip blank lines.
            if not line:
                continue
            
            # Deal with mode change.
            m_event_start = re.match(r"^(\d+),(0|1|2)$", line)
            m_strings_start = re.match(r"^strings:$", line)
            m_linked_files_start = re.match(r"^linked:$", line)
            if m_event_start or m_strings_start or m_linked_files_start:
                if mode == "event":
                    # Flush current event data to prepare for mode change.
                    new_event = emevd_handler.Event(current_event_id, current_event_reset_mode, 
                        copy.deepcopy(current_event_instrs))
                    event_list.append(new_event)
                if mode == "string_table" or mode == "linked_files_table" or mode == "":
                    pass # No flushing needed.
                    
                if m_event_start:
                    mode = "event"
                    current_event_id = int(m_event_start.group(1))
                    current_event_reset_mode = int(m_event_start.group(2))
                    current_event_instrs = []
                elif m_strings_start:
                    mode = "string_table"
                elif m_linked_files_start:
                    mode = "linked_files_table"
                else:
                    mode = ""
                continue
                    
            # Handle mode-specific patterns.
            if mode == "event":
                m_instr_regex = re.compile(r"^(\d+)\[(\d+)\]\(([iIhHbBfxs\|]*)\)\[([\d,x\.-]*)\]")
                m_instr = m_instr_regex.match(line)
                m_param = re.match(r"\^\((\d+)<-(\d+),(\d+)\)", line)
                if m_instr:
                    instr_class = int(m_instr.group(1))
                    instr_index = int(m_instr.group(2))
                    arg_format_string = m_instr.group(3)
                    arg_list_string = m_instr.group(4)
                    
                    remaining_line = m_instr_regex.sub('', line)
                    m_eventlayer = re.match(r"^<([\d,]+)>$", remaining_line)
                    eventlayer = None
                    if m_eventlayer:
                        eventlayer = 0
                        prev_eventlayer_value = -1
                        eventlayer_strings = m_eventlayer.group(1).split(",")
                        for v in eventlayer_strings:
                            next_eventlayer_value = int(v)
                            if next_eventlayer_value <= prev_eventlayer_value:
                                raise ValueError("Line %d: Event Layer Bit %d is out of sequence."
                                 % (line_num, next_eventlayer_value))
                            if next_eventlayer_value < 0 or next_eventlayer_value > 31:
                                raise ValueError("Line %d: Event Layer Bit %d is not in range [0,31]."
                                 % (line_num, next_eventlayer_value))
                            eventlayer += 2 ** next_eventlayer_value
                            prev_eventlayer_value = next_eventlayer_value
                    elif remaining_line != '' and not m_eventlayer:
                        raise ValueError("Line %d: Instruction remnant '%s' could not be parsed."
                         % (line_num, remaining_line))
                   
                    # Check the argument list against the format_string.
                    split_arg_list = arg_list_string.split(",")
                    trimmed_format_string = arg_format_string.translate(str.maketrans("", "", "|"))
                    if split_arg_list == ['']:
                        split_arg_list = []
                    if len(trimmed_format_string) != len(split_arg_list):
                        raise ValueError(("Line %d: Length mismatch between format string (%d) " + 
                            "and argument array (%d)") % (line_num, arg_format_string, arg_list_string))
                    argument_list = []
                    for (i, char) in enumerate(trimmed_format_string):
                        arg = split_arg_list[i]
                        
                        if char == 'f':
                            argument_list.append(float(arg))
                            
                        CHAR_BOUNDS = {'b': (-128, 127), 'B': (0, 255), 'h': (-32768, 32767),
                            'H': (0, 65535), 'i': (-2147483648, 2147483647), 'I': (0, 4294967295),
                            'x': (0, 255), 's': (0, 4294967295)}
                        if char in CHAR_BOUNDS:
                            (min_val, max_val) = CHAR_BOUNDS[char]
                            parsed_arg = int(arg, 0)
                            if min_val <= parsed_arg and parsed_arg <= max_val:
                                argument_list.append(parsed_arg)
                            else:
                                raise ValueError(("Line %d: Argument \"%d\" is not inside " + 
                                    "the bounds for format specifier \"%s\".") % (line_num, arg, char))
                    instr = emevd_handler.Instruction(instr_class, instr_index, arg_format_string, argument_list, [], eventlayer)
                    current_event_instrs.append(instr)
                elif m_param:
                    if len(current_event_instrs) >= 1:
                        # Parse the line as a parameter replacement for the previous line.
                        dest_byte = int(m_param.group(1))
                        source_byte = int(m_param.group(2))
                        length = int(m_param.group(3))
                        
                        param = emevd_handler.ParameterReplacement(len(current_event_instrs)-1, dest_byte, source_byte, length)
                        current_event_instrs[-1].append_parameter_replacement(param)
                    else:
                        # Orphaned parameter line.
                        raise ValueError(("Line %d: Parameter replacement \"%s\" " + 
                            "does not have an instruction to attach to.") % (line_num, line))
                else: # Malformed line.
                    raise ValueError(("Line %d: Line \"%s\" cannot be parsed as a " + 
                     "instruction or parameter replacement.") % (line_num, line))
            elif mode == "strings_table":
                pass # Dealt with before comment/whitespace stripping.
            elif mode == "linked_files_table":
                m_linked_file = re.match(r"^(\d+)$", line)
                if m_linked_file:
                    linked_files.append(int(m_linked_file.group(1)))
            else:
                # Determine filetype at the start of the file.
                if filetype == None:
                    # Handle filetype override first.
                    if filetype_override != None:
                        filetype == filetype_override
                    else:
                        split_line = line.split(":")
                        filetype = EVD_FileType.from_string(split_line[0])
                        if filetype == None:
                            raise ValueError("Line %d: Could not find acceptable EVD filetype signifier.")
                        if len(split_line) > 1 and split_line[1] == "DCX":
                            should_dcx = True
    return (filetype, event_list, strings, linked_files, should_dcx)

import emevd_handler
