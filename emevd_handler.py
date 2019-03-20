import struct
from enum import Enum, unique

import dcx_handler

def get_byte_offset_from_struct(struct_format):
    """Computes an array of byte offsets from a struct format string.
    The ith element of the array indicates which byte in the struct is
    the first byte of the value packed as the ith character of the format 
    string. An 's' in the format string will be treated as an 'I' for offset
    calculations.
    """
    endian = struct_format[0]
    format_string = struct_format[1:]
    fixed_format_string = format_string.replace("s", "I")
    byte_offset_array = {}
    for i in range(0, len(fixed_format_string)):
        offset = struct.calcsize(endian + fixed_format_string[:i+1]) - struct.calcsize(endian + fixed_format_string[i])
        byte_offset_array[offset] = (i , format_string[i])
    return byte_offset_array
    
def extract_utf16z(content, offset):
    extracted = b''
    length = 0
    while content[offset + length:offset + length+ 2] != b'\x00\x00':
        extracted = extracted + content[offset + length:offset + length + 2]
        length += 2
    return (extracted.decode('utf-16'), length + 2)
    
def extract_asciiz(content, offset):
    extracted = b''
    length = 0
    while bytes([content[offset+length]]) != b'\x00':
        extracted += bytes([content[offset+length]])
        length += 1
    return (extracted.decode('ascii'), length+1)
    
def extract_string(content, offset, filetype):
    if filetype == EVD_FileType.DARK_SOULS_1:
        return extract_asciiz(content, offset)
    elif (filetype == EVD_FileType.BLOODBORNE or
     filetype == EVD_FileType.DARK_SOULS_3_TEST or
     filetype == EVD_FileType.DARK_SOULS_3):
        return extract_utf16z(content, offset)
    
def uint32_to_bitshift_string(uint32):
    bitshifts = []
    for i in range(32):
        if (2 ** i) & uint32:
            bitshifts.append(str(i))
    return ", ".join(sorted(bitshifts))
    
    
@unique
class EVD_FileType(Enum):
    DARK_SOULS_1 = 0
    BLOODBORNE = 1
    DARK_SOULS_3_TEST = 2
    DARK_SOULS_3 = 3
    
    def to_string(self):
        name_dict = {
            self.DARK_SOULS_1: "EVD-DS1",
            self.BLOODBORNE: "EVD-BB",
            self.DARK_SOULS_3_TEST: "EVD-DS3Test",
            self.DARK_SOULS_3: "EVD-DS3Main"}
        return name_dict[self]
        
    @classmethod
    def from_string(cls, string):
        if string == "EVD-DS1":
            return cls.DARK_SOULS_1
        elif string == "EVD-BB":
            return cls.BLOODBORNE
        elif string == "EVD-DS3Test":
            return cls.DARK_SOULS_3_TEST
        elif string == "EVD-DS3Main":
            return cls.DARK_SOULS_3
        else:
            return None

class ParameterReplacement:
    def __init__(self, instr_number, destination_starting_byte = 0, source_starting_byte = 0, length = 0):
        self.instr_number = instr_number
        self.destination_starting_byte = destination_starting_byte
        self.source_starting_byte = source_starting_byte
        self.length = length
        
    def export_as_raw_numeric(self):
        return "(%d <- %d, %d)" % (self.destination_starting_byte, self.source_starting_byte, self.length)
        
    def export_as_binary(self, filetype):
        if filetype == EVD_FileType.DARK_SOULS_1:
            return struct.pack("@IIII4x", self.instr_number, self.destination_starting_byte, self.source_starting_byte, self.length)
        elif (filetype == EVD_FileType.BLOODBORNE or 
         filetype == EVD_FileType.DARK_SOULS_3_TEST or 
         filetype == EVD_FileType.DARK_SOULS_3):
            return struct.pack("@QQQQ", self.instr_number, self.destination_starting_byte, self.source_starting_byte, self.length)

class Instruction:
    def __init__(self, instr_class, instr_index, arg_format_string = "", argument_list = None, parameter_replacements = None, eventlayer = None):
        if argument_list == None:
            argument_list = []
        if parameter_replacements == None:
            parameter_replacements = []
        
        if len(arg_format_string.translate(str.maketrans(dict.fromkeys('|')))) != len(argument_list):
            raise ValueError("Cannot initialize Instruction [" + str(instr_class) + "][" + str(instr_index) +\
                "] with argument format string \"" + arg_format_string +\
                "\" due to argument list length mismatch (" + str(len(argument_list)) + ").")
        self.instr_class = instr_class
        self.instr_index = instr_index
        self.arg_format_string = arg_format_string
        self.argument_list = argument_list
        self.parameter_replacements = parameter_replacements
        self.eventlayer = eventlayer
      
    def get_argument_byte_count(self):
        translation_dict = {'|': None, 's': 'I'}
        return struct.calcsize("@" + self.arg_format_string.translate(str.maketrans(translation_dict)) + "0i")
    
    def count_parameter_replacements(self):
        return len(self.parameter_replacements)
        
    def append_parameter_replacement(self, param):
        self.parameter_replacements.append(param)
        
    def export_as_raw_numeric(self):
        arg_list_string = "[" + ", ".join([str(i) for i in self.argument_list]) + "]"
        first_line = "%4d[%02d] (%s)" % (self.instr_class, self.instr_index, self.arg_format_string) + arg_list_string
        if self.eventlayer != None:
            first_line += " <%s>" % uint32_to_bitshift_string(self.eventlayer)
        returnList = [first_line]
        for param in self.parameter_replacements:
            returnList.append("   ^" + param.export_as_raw_numeric())
        return returnList
        
    def export_as_human_readable(self, strings, filetype): 
        import evd_command_to_readable
         
        fixed_args = []
        var_args = []
        
        arg_list_to_split = self.argument_list
        
        has_split = False
        count = 0
        for format_char in self.arg_format_string:
            if format_char == "|":
                has_split = True
                continue
            arg_value = self.argument_list[count]
            if format_char == "s":
                string_offset = self.argument_list[count]
                if isinstance(string_offset, str):
                    arg_value = "StringTable[%s]" % string_offset
                else:
                    (extracted_string, _) = extract_string(strings, string_offset, filetype)
                    arg_value = '"' + extracted_string + '"'
            if has_split:
                var_args.append(arg_value)
            else:
                fixed_args.append(arg_value)
            count += 1
        result = evd_command_to_readable.translate(self.instr_class, self.instr_index, fixed_args, var_args, filetype)
        
        if self.eventlayer:
            result += " <EventLayers: %s>" % uint32_to_bitshift_string(self.eventlayer)
        return result
        
    def apply_parameter_replacement(self):
        """Applies any parameter replacement instructions to this instruction,
        which replaces the dummy value of the argument with a string 
        representation of the bytes of the parameter array.
        
        Returns the parameter strings used as replacements, as well as
        a dictionary with guesses as to the format string types that 
        should be used to represent each parameter.
        """
        
        PERMITTED = [0, 0.0, -1, 1, 10]
        struct_offset_dict = get_byte_offset_from_struct("@" + self.arg_format_string.translate(str.maketrans(dict.fromkeys('|'))))
        
        instr_parameter_set = set()
        instr_parameter_types = {}
        
        for param in self.parameter_replacements:
            if param.destination_starting_byte not in struct_offset_dict:
                print(str(self.instr_class) + "[" + str(self.instr_index) + "]")
                print(str(self.argument_list))
                print(param.export_as_raw_numeric())
                raise ValueError("Parameter destination " + str(param.destination_starting_byte) + \
                    " is misaligned with target instruction row (format: '" + self.arg_format_string + "').")
            (argument_index, argument_byte_type) = struct_offset_dict[param.destination_starting_byte]
            if argument_byte_type != "x":
                arg_byte_size = struct.calcsize(argument_byte_type)
                if argument_byte_type == "s":
                    arg_byte_size = 4
                if arg_byte_size < param.length:
                    print(str(self.instr_class) + "[" + str(self.instr_index) + "]")
                    print(str(self.argument_list))
                    print(param.export_as_raw_numeric())
                    raise ValueError("Parameter of length " + str(param.length) + \
                        " will not fit in destination of length " + str(struct.calcsize(argument_byte_type)) + ".")
                value_to_overwrite = self.argument_list[argument_index]
                parameter_name = 'X' + str(param.source_starting_byte) + ':' + str(param.source_starting_byte + param.length - 1)
                    
                if ((value_to_overwrite not in PERMITTED) and 
                 value_to_overwrite != parameter_name and
                 argument_byte_type != "s"):
                    print(str(self.instr_class) + "[" + str(self.instr_index) + "]")
                    print(str(self.argument_list))
                    print(param.export_as_raw_numeric())
                    raise ValueError("Parameter is overwriting non-zero value " + str(value_to_overwrite) + ".")
                
                self.argument_list[argument_index] = parameter_name
                
                instr_parameter_set.add((param.source_starting_byte, param.source_starting_byte + param.length - 1))
                if parameter_name not in instr_parameter_types:
                    instr_parameter_types[parameter_name] = set(argument_byte_type)
                else:
                    instr_parameter_types[parameter_name].add(argument_byte_type)
            else:
                value_to_overwrite = self.argument_list[argument_index]
                parameter_name = 'X' + str(param.source_starting_byte) + ':' + str(param.source_starting_byte + param.length - 1)
                self.argument_list[argument_index] = parameter_name + ": " + value_to_overwrite
                instr_parameter_set.add((param.source_starting_byte, param.source_starting_byte + param.length - 1))
                if parameter_name not in instr_parameter_types:
                    instr_parameter_types[parameter_name] = set(argument_byte_type)
                else:
                    instr_parameter_types[parameter_name].add(argument_byte_type)
        return (instr_parameter_set, instr_parameter_types)
        
    def export_argument_list_as_binary(self, filetype):
        translation_dict = {'|': None, 's': 'I'}
        format_string = "@" + self.arg_format_string.translate(str.maketrans(translation_dict)) + "0i"
        return struct.pack(format_string, *self.argument_list)
        
    def export_parameter_replacements_as_binary(self):
        return "".join([param.export_as_binary(filetype) for param in self.parameter_replacements])
    
    def export_as_binary(self, arg_offset, eventlayer_offset, filetype):
        if self.get_argument_byte_count() == 0:
            arg_offset = -1
        if filetype == EVD_FileType.DARK_SOULS_1:
            return struct.pack("@IIIii4x", self.instr_class, self.instr_index, self.get_argument_byte_count(), arg_offset, eventlayer_offset)
        elif filetype == EVD_FileType.BLOODBORNE or filetype == EVD_FileType.DARK_SOULS_3_TEST:
            return struct.pack("@IIQi4xi4x", self.instr_class, self.instr_index, self.get_argument_byte_count(), arg_offset, eventlayer_offset)
        elif filetype == EVD_FileType.DARK_SOULS_3:
            return struct.pack("@IIQi4xq", self.instr_class, self.instr_index, self.get_argument_byte_count(), arg_offset, eventlayer_offset)
        
    def export_eventlayer_as_binary(self, filetype):
        if filetype == EVD_FileType.DARK_SOULS_1:
            # This is a guess, since DS1 never uses the event layer.
            return struct.pack("@IIIiI", 2, self.eventlayer, 0, -1, 1)
        elif (filetype == EVD_FileType.BLOODBORNE or 
         filetype == EVD_FileType.DARK_SOULS_3_TEST or
         filetype == EVD_FileType.DARK_SOULS_3):
            # This is partially a guess, since BB/DS3T never uses the event layer.
            return struct.pack("@IIQqQ", 2, self.eventlayer, 0, -1, 1)

class Event:
    def __init__(self, event_id = 0, reset_mode = 0, instr_list = []):
        self.event_id = event_id
        self.reset_mode = reset_mode
        self.instr_list = instr_list
    
    def count_instructions(self):
        return len(self.instr_list)
        
    def get_total_argument_byte_count(self):
        return sum([i.get_argument_byte_count() for i in self.instr_list])
        
    def count_total_parameter_replacements(self):
        return sum([i.count_parameter_replacements() for i in self.instr_list])
        
    def export_as_raw_numeric(self):
        returnString = str(self.event_id) + ", " + str(self.reset_mode)
        for instr in self.instr_list:
            returnString += "\n " + "\n ".join(instr.export_as_raw_numeric())
        return returnString
        
    def build_parameter_types(self):
        """Applies any parameter replacement instructions to their
        instructions and attempts to build a string representing the types
        of all the parameters used. Since parameters are packed as binary
        data, some parameters may overlap or have different apparent types,
        although this never occurs in the normal files.
        """
        
        total_instr_parameter_set = set()
        total_instr_parameter_types = {}
        for instr in self.instr_list:
            (instr_parameter_set, instr_parameter_types) = instr.apply_parameter_replacement()
            total_instr_parameter_set = total_instr_parameter_set.union(instr_parameter_set)
            for k in instr_parameter_types:
                if k not in total_instr_parameter_types:
                    total_instr_parameter_types[k] = set(instr_parameter_types[k])
                else:
                    total_instr_parameter_types[k] = total_instr_parameter_types[k].union(instr_parameter_types[k])
        sorted_parameter_list = sorted(total_instr_parameter_set)
        return "Parameters: {" + ", ".join(['X' + str(i) + ':' + str(j) for (i,j) in sorted_parameter_list]) + "} (" + \
            "".join(["|".join(total_instr_parameter_types['X' + str(i) + ':' + str(j)]) for (i,j) in sorted_parameter_list]) + ")"
            
    def export_as_human_readable(self, strings, filetype, suppress_line_numbers = False):
        reset_mode_names = ["Ignores", "Restarts on", "Ends on"]
        
        returnString = "Event ID: %d, %s Bonfire Rest" % (self.event_id, reset_mode_names[self.reset_mode])
        returnString += "\n" + self.build_parameter_types()
        for i, instr in enumerate(self.instr_list):
            returnString += "\n    "
            if not suppress_line_numbers:
                returnString += "%3d" % i + ' '
            returnString += instr.export_as_human_readable(strings, filetype)
        return returnString
        
    def export_as_binary(self, instr_offset, arg_offset, param_offset, eventlayer_list, filetype):
        total_params = self.count_total_parameter_replacements()
        if total_params == 0:
            param_offset = -1
        
        if filetype == EVD_FileType.DARK_SOULS_1:
            event_binary = struct.pack("@IIIIiI4x", self.event_id, self.count_instructions(),
                instr_offset, total_params, param_offset, self.reset_mode)
        elif filetype == EVD_FileType.BLOODBORNE or filetype == EVD_FileType.DARK_SOULS_3_TEST:
            event_binary = struct.pack("@QQQQi4xI4x", self.event_id, self.count_instructions(),
                instr_offset, total_params, param_offset, self.reset_mode)
        elif filetype == EVD_FileType.DARK_SOULS_3:
            event_binary = struct.pack("@QQQQqI4x", self.event_id, self.count_instructions(),
                instr_offset, total_params, param_offset, self.reset_mode)
            
        instrs_binary = b""
        args_binary = b""
        params_list = []
        for instr in self.instr_list:
            eventlayer_offset = -1
            if instr.eventlayer:
                eventlayer_binary = instr.export_eventlayer_as_binary(filetype)
                if eventlayer_binary not in eventlayer_list:
                    eventlayer_list.append(eventlayer_binary)
                index = eventlayer_list.index(eventlayer_binary)
                eventlayer_offset = sum([len(f) for f in eventlayer_list[:index]])
            instrs_binary += instr.export_as_binary(arg_offset, eventlayer_offset, filetype)
            a_bin = instr.export_argument_list_as_binary(filetype)
            args_binary += a_bin
            arg_offset += len(a_bin)
            params_list += instr.parameter_replacements
        # Collect and sort parameter replacements to better match actual .emevd files. (Should be purely cosmetic)
        sorted_params_list = sorted(params_list, key=lambda param: (param.source_starting_byte, param.instr_number))
        params_binary = b"".join([param.export_as_binary(filetype) for param in sorted_params_list])
            
        return (event_binary, instrs_binary, args_binary, params_binary, eventlayer_list)

class EmevdData:
    def __init__(self, filetype, event_list = None, strings = None, 
     linked_files_name_offset = None, should_dcx = False):
        self.filetype = filetype
        if event_list == None:
            event_list = []
        if strings == None:
            strings = []
        if linked_files_name_offset == None:
            linked_files_name_offset = []
        self.event_list = event_list
        self.strings = strings
        self.linked_files_name_offset = linked_files_name_offset
        self.should_dcx = should_dcx
        
    @classmethod
    def build_from_emevd_file_content(cls, file_content, filetype_override = None):
        import emevd_opener
        (filetype, event_list, strings, linked_files_name_offsets, should_dcx) = emevd_opener.emevd_file_content_to_event_list(file_content, filetype_override)
        return EmevdData(filetype, event_list, strings, linked_files_name_offsets, should_dcx)
        
    @classmethod
    def build_from_raw_numeric_file_content(cls, file_content, filetype_override = None):
        import emevd_opener
        (filetype, event_list, strings, linked_files_name_offsets, should_dcx) = emevd_opener.raw_numeric_file_content_to_event_list(file_content, filetype_override)
        return EmevdData(filetype, event_list, strings, linked_files_name_offsets, should_dcx)
        
    def export_as_raw_numeric(self):
        dcx_string = "UNDCX"
        if self.should_dcx:
            dcx_string = "DCX"
        
        return_string = EVD_FileType.to_string(self.filetype) + ":" + dcx_string + "\n\n"
        
        return_string += "\n\n".join([event.export_as_raw_numeric() for event in self.event_list])
        
        return_string += "\n\n\nstrings:\n"
        offset = 0
        while offset < len(self.strings):
            (extracted_string, length) = extract_string(self.strings, offset, self.filetype)
            return_string += "%d: %s\n" % (offset, extracted_string)
            offset += length
            
        return_string += "\n\n\nlinked:\n"
        for name_offset in self.linked_files_name_offset:
            return_string += "%d\n" % name_offset
        return return_string
    
    def export_as_human_readable(self, suppress_line_numbers = False):
        return_string = EVD_FileType.to_string(self.filetype) + "\n\n"
        
        return_string += "\n\n".join([event.export_as_human_readable(self.strings, 
         self.filetype, suppress_line_numbers) for event in self.event_list])
        return_string += "\n\n\nString Table:\n"
        offset = 0
        while offset < len(self.strings):
            (extracted_string, length) = extract_string(self.strings, offset, self.filetype)
            return_string += "%d: %s\n" % (offset, extracted_string)
            offset += length
            
        return_string += "\n\n\nLinked .emevd Files:\n"
        for name_offset in self.linked_files_name_offset:
            (linked_file_name, _) = extract_string(self.strings, name_offset, self.filetype)
            return_string += "%s\n" % linked_file_name
        return return_string
    
    def export_as_emevd(self):
        event_table_binary = b""
        instr_table_binary = b""
        argument_data_binary = b""
        param_table_binary = b""
        eventlayer_list = []
        
        current_instr_table_offset = 0
        current_instr_count = 0
        current_argument_data_length = 0
        current_param_table_offset = 0
        current_param_count = 0
        
        for e in self.event_list:
            (e_bin, i_bin, a_bin, p_bin, eventlayer_list) = e.export_as_binary(current_instr_table_offset, 
                current_argument_data_length, current_param_table_offset, eventlayer_list, self.filetype)
            
            event_table_binary += e_bin
            instr_table_binary += i_bin
            argument_data_binary += a_bin
            param_table_binary += p_bin
            
            current_instr_table_offset += len(i_bin)
            current_instr_count += e.count_instructions()
            current_argument_data_length += len(a_bin)
            current_param_table_offset += len(p_bin)
            current_param_count += e.count_total_parameter_replacements()
            
        eventlayer_binary = b"".join(eventlayer_list)
        
        linked_files_offset_binary = b""
        for l in self.linked_files_name_offset:
            if self.filetype == EVD_FileType.DARK_SOULS_1:
                linked_files_offset_binary += struct.pack("<I", l)
            elif (self.filetype == EVD_FileType.BLOODBORNE or 
             self.filetype == EVD_FileType.DARK_SOULS_3_TEST or 
             self.filetype == EVD_FileType.DARK_SOULS_3):
                linked_files_offset_binary += struct.pack("<Q", l)

        # Prepare header tables and offsets.
        emevd_header_binary = b""
        emevd_data_binary = b""
        header_pair_format_string = "<II"
        if self.filetype == EVD_FileType.DARK_SOULS_1:
            header_pair_format_string = "<II"
            header_size = 0x54
        elif (self.filetype == EVD_FileType.BLOODBORNE or 
         self.filetype == EVD_FileType.DARK_SOULS_3_TEST or 
         self.filetype == EVD_FileType.DARK_SOULS_3):
            header_pair_format_string = "<QQ"
            header_size = 0x90
        
        emevd_header_binary += struct.pack(header_pair_format_string, len(self.event_list), header_size + 0)
        emevd_data_binary += event_table_binary
        emevd_header_binary += struct.pack(header_pair_format_string, current_instr_count, header_size + len(emevd_data_binary))
        emevd_data_binary += instr_table_binary
        
        # Unused table.
        emevd_header_binary += struct.pack(header_pair_format_string, 0, header_size + len(emevd_data_binary))
        emevd_data_binary += b""
        
        emevd_header_binary += struct.pack(header_pair_format_string, len(eventlayer_list), header_size + len(emevd_data_binary))
        emevd_data_binary += eventlayer_binary
        
        # Argument data is packed here, but the header entry comes later.
        if self.filetype == EVD_FileType.DARK_SOULS_1:
            argument_data_binary += b"\x00\x00\x00\x00" # Termination z4 for the packed ArgumentData
        elif (self.filetype == EVD_FileType.BLOODBORNE or 
         self.filetype == EVD_FileType.DARK_SOULS_3_TEST or 
         self.filetype == EVD_FileType.DARK_SOULS_3):
            # Pad data with NUL to multiple of 16.
            current_data_length = header_size + len(emevd_data_binary) + len(argument_data_binary)
            to_next_multiple = 16 - (current_data_length % 16)
            if to_next_multiple < 16:
                current_data_length += to_next_multiple
                argument_data_binary += b"\x00" * to_next_multiple
        argument_header_binary = struct.pack(header_pair_format_string, len(argument_data_binary), header_size + len(emevd_data_binary))
        emevd_data_binary += argument_data_binary 
        
        emevd_header_binary += struct.pack(header_pair_format_string, current_param_count, header_size + len(emevd_data_binary))
        emevd_data_binary += param_table_binary
        emevd_header_binary += struct.pack(header_pair_format_string, len(self.linked_files_name_offset), header_size + len(emevd_data_binary))
        emevd_data_binary += linked_files_offset_binary
        
        # Argument data header entry.
        emevd_header_binary += argument_header_binary
        
        emevd_header_binary += struct.pack(header_pair_format_string, len(self.strings), header_size + len(emevd_data_binary))
        emevd_data_binary += self.strings
        
        # DS1 has a header-terminating z4, which removed in later formats.
        if self.filetype == EVD_FileType.DARK_SOULS_1:
            emevd_header_binary += b"\x00\x00\x00\x00"
        
        filesize = header_size + len(emevd_data_binary)
        emevd_data = emevd_header_binary + emevd_data_binary
        
        # Build EVD file.
        emevd_header = b"EVD\x00"
        if self.filetype == EVD_FileType.DARK_SOULS_1:
            emevd_header += struct.pack("<II", 0x00000000, 0x000000CC)
        elif self.filetype == EVD_FileType.BLOODBORNE or self.filetype ==  EVD_FileType.DARK_SOULS_3_TEST:
            emevd_header += struct.pack("<II", 0x0000FF00, 0x000000CC)
        elif self.filetype == EVD_FileType.DARK_SOULS_3:
            emevd_header += struct.pack("<II", 0x0001FF00, 0x000000CD)
        else:
            raise ValueError("Unrecognized filetype. Cannot write version bytes.")
        emevd_header += struct.pack("<I", filesize)
        emevd = emevd_header + emevd_data
        
        if self.should_dcx:
            if self.filetype == EVD_FileType.DARK_SOULS_1:
                return dcx_handler.compress_dcx_content(emevd, False)
            else:
                return dcx_handler.compress_dcx_content(emevd, True)
        else:
            return emevd
    
        
