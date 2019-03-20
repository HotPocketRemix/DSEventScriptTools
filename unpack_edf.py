import sys
import struct
import os
from enum import Enum, unique

import serialize_edf as serial

import logging
log = logging.getLogger(__name__)

TYPE_CHAR_DICT = {0: 'B', 1: 'H', 2: 'I', 3: 'b', 4: 'h', 5: 'i', 6: 'f', 8: 's'}

# Consumes length copies of byte from content, starting at offset.
# Returns the new offset after consumption.
# Raises a ValueError if any of the consumed bytes do not match the
#  given value. 
def consume_byte(content, offset, byte, length=1):
    for i in range(length-1):
        if content[offset + i:offset + i+1] != byte:
            raise ValueError(("Expected byte '0x%s' at offset " + 
             "0x%x but received byte '0x%s'.") % (byte.hex(), offset+i, 
             content[offset + i:offset + i+1].hex()))
    return offset + length

# Wrapper for struct.unpack_from to make calculating offsets easier.
#  Returns (result, new_offset) where result is the output of struct.unpack_from.
def extract_struct(format_string, content, offset=0):
    result = struct.unpack_from(format_string, content, offset=offset)
    return (result, offset + struct.calcsize(format_string))

# Extracts a NUL-terminated UTF-16 string from content starting at offset
#  and returns it as a UTF-8 encoded string, and the length of the string,
#  including the NUL.
def extract_utf16z(content, offset):
    extracted = b''
    length = 0
    while content[offset + length:offset + length+ 2] != b'\x00\x00':
        extracted = extracted + content[offset + length:offset + length + 2]
        length += 2
    return (extracted.decode('utf-16'), length + 2)
    
    
class EDF_Filetype(Enum):
    DARK_SOULS_1 = 0
    BLOODBORNE = 1

class EDF_EnumValue:
    def __init__(self, name_index, enum_value):
        self.name_index = name_index
        self.enum_value = enum_value
    
    @classmethod    
    def from_file_content(cls, content, offset, strings_offset_dict, filetype):
        master_offset = offset
        if filetype == EDF_Filetype.DARK_SOULS_1:
            ((name_offset,), master_offset) = extract_struct("<I", content, master_offset)
        else:
            ((name_offset,), master_offset) = extract_struct("<Q", content, master_offset)
        enum_value = content[master_offset : master_offset+4]
        master_offset += 4
        master_offset = consume_byte(content, master_offset, b'\x00', 4)

        name_index = strings_offset_dict[name_offset]
        
        return (EDF_EnumValue(name_index, enum_value), master_offset)
    
    def to_string(self):
        return ("EDF_EnumValue[name_index=%d, enum_value=0x%s]" %
            (self.name_index, self.enum_value.hex()))
            
    def to_binary(self, strings_name_index_dict, filetype):
        if filetype == EDF_Filetype.DARK_SOULS_1:
            return struct.pack("<I4sI", strings_name_index_dict[self.name_index],
                self.enum_value, 0)
        else:
            return struct.pack("<Q4sI", strings_name_index_dict[self.name_index],
                self.enum_value, 0)
    
    @classmethod
    def get_size(cls, filetype):
        if filetype == EDF_Filetype.DARK_SOULS_1:
            return struct.calcsize("<I4sI")
        else:
            return struct.calcsize("<Q4sI")

class EDF_Enum:
    def __init__(self, name_index, num_of_enum_values, starting_enum_value_index):
        self.name_index = name_index
        self.num_of_enum_values = num_of_enum_values
        self.starting_enum_value_index = starting_enum_value_index
    
    @classmethod    
    def from_file_content(cls, content, offset, strings_offset_dict, filetype):
        master_offset = offset
        
        if filetype == EDF_Filetype.DARK_SOULS_1:
            ((name_offset, num_of_enum_values, enum_value_table_offset),
                master_offset) = extract_struct("<III", content, master_offset)
            master_offset = consume_byte(content, master_offset, b'\x00', 4)
        else:
            ((name_offset, num_of_enum_values, enum_value_table_offset),
                master_offset) = extract_struct("<QQQ", content, master_offset)
        
        name_index = strings_offset_dict[name_offset]
        starting_enum_value_index = enum_value_table_offset // EDF_EnumValue.get_size(filetype)
        
        return (EDF_Enum(name_index, num_of_enum_values, starting_enum_value_index), master_offset)
    
    def to_string(self):
        return ("EDF_Enum[name_index=%d, enum_values=[%d:%d)]" %
            (self.name_index, self.starting_enum_value_index, 
                self.starting_enum_value_index + self.num_of_enum_values))
    
    def to_binary(self, strings_name_index_dict, filetype):
        if filetype == EDF_Filetype.DARK_SOULS_1:
            return struct.pack("<IIII", strings_name_index_dict[self.name_index], 
                self.num_of_enum_values, self.starting_enum_value_index * EDF_EnumValue.get_size(filetype), 0)
        else:
            return struct.pack("<QQQ", strings_name_index_dict[self.name_index], 
                self.num_of_enum_values, self.starting_enum_value_index * EDF_EnumValue.get_size(filetype))
            
    def to_serializeable(self, enums_values_list, strings_list):
        values_dict = {}
        for i in range(self.starting_enum_value_index, self.starting_enum_value_index + self.num_of_enum_values):
            (enum_value,) = struct.unpack("<i", enums_values_list[i].enum_value) # Might not always work...
            values_dict[enum_value] = strings_list[enums_values_list[i].name_index]
        return serial.Serializeable_EDF_Enum(**{
         'name': strings_list[self.name_index],
         'values': values_dict
        })
        
    @classmethod
    def get_size(cls, filetype):
        if filetype == EDF_Filetype.DARK_SOULS_1:
            return struct.calcsize("<IIII")
        else:
            return struct.calcsize("<QQQ")
        

class EDF_Argument: 
    def __init__(self, name_index, arg_type, enum_index, arg_default, 
     arg_min, arg_max, arg_increment, format_string_index, 
     unknown1, unknown2, unknown3, unknown4):
        self.name_index = name_index
        self.arg_type = arg_type
        self.enum_index = enum_index
        self.arg_default = arg_default
        self.arg_min = arg_min
        self.arg_max = arg_max
        self.arg_increment = arg_increment
        self.format_string_index = format_string_index
        self.unknown1 = unknown1
        self.unknown2 = unknown2
        self.unknown3 = unknown3
        self.unknown4 = unknown4
        
    @classmethod
    def get_type_dict(cls, filetype):
        if filetype == EDF_Filetype.DARK_SOULS_1:
            return {0: 'Bxxx', 1: 'Hxx', 2: 'I', 3: 'bxxx', 4: 'hxx', 5: 'i', 6: 'f', 8: 'I'}
        else:
            return {0: 'Bxxxxxxx', 1: 'Hxxxxxx', 2: 'Ixxxx', 3: 'bxxxxxxx', 4: 'hxxxxxx', 5: 'ixxxx', 6: 'fxxxx', 8: 'Q'}
    
    @classmethod    
    def from_file_content(cls, content, offset, strings_offset_dict, filetype):
        master_offset = offset
        
        type_dict = EDF_Argument.get_type_dict(filetype)
        if filetype == EDF_Filetype.DARK_SOULS_1:
            ((name_offset, arg_type, enum_table_offset), 
                master_offset) = extract_struct("<IIi", content, master_offset)
            arg_type_string = type_dict[arg_type]
            ((arg_default, arg_min, arg_max, arg_increment),
                master_offset) = extract_struct("<" + (arg_type_string * 4), content, master_offset)
            ((format_code_offset, unknown1, unknown2, unknown3, unknown4),
                master_offset) = extract_struct("<IBBBB", content, master_offset)
        else:
            ((name_offset, arg_type, unknown1, unknown2, unknown3, unknown4, enum_table_offset), 
                master_offset) = extract_struct("<QIBBBBixxxx", content, master_offset)
            arg_type_string = type_dict[arg_type]
            ((arg_default, arg_min, arg_max, arg_increment),
                master_offset) = extract_struct("<" + (arg_type_string * 4), content, master_offset)
            ((format_code_offset,), master_offset) = extract_struct("<Q", content, master_offset)
        
        name_index = strings_offset_dict[name_offset]
        if enum_table_offset != -1:
            enum_index = enum_table_offset // EDF_Enum.get_size(filetype)
        else:
            enum_index = -1
        format_string_index = strings_offset_dict[format_code_offset]
        
        if arg_type == 8: # Actually a pointer to a string
            arg_default = strings_offset_dict[arg_default]
        
        return (EDF_Argument(name_index, arg_type, enum_index, 
            arg_default, arg_min, arg_max, arg_increment, format_string_index,
            unknown1, unknown2, unknown3, unknown4), master_offset)
    
    def to_string(self):
        return (("EDF_Argument[name_index=%d, type=%d, enum_index=%d, " + 
         "default=%d, range=[%d:%d:%d], format_string_index=%d, unknown=%02x%02x%02x%02x]") %
            (self.name_index, self.arg_type, self.enum_index, self.arg_default, 
                self.arg_min, self.arg_increment, self.arg_max, self.format_string_index,
                self.unknown1, self.unknown2, self.unknown3, self.unknown4))
                
    def to_binary(self, strings_name_index_dict, filetype):
        if self.enum_index != -1:
            enum_table_offset = self.enum_index * EDF_Enum.get_size(filetype)
        else:
            enum_table_offset = -1
            
        if self.arg_type == 8:
            default = strings_name_index_dict[self.arg_default]
        else:
            default = self.arg_default
        
        type_dict = EDF_Argument.get_type_dict(filetype)
        if filetype == EDF_Filetype.DARK_SOULS_1:
            packed_data = struct.pack("<IIi", strings_name_index_dict[self.name_index], 
                self.arg_type, enum_table_offset)
            packed_data += struct.pack("<" + (TYPE_DICT[self.arg_type] * 4), 
                self.arg_default, self.arg_min, self.arg_max, self.arg_increment)
            packed_data += struct.pack("<IBBBB", strings_name_index_dict[self.format_string_index],
                self.unknown1, self.unknown2, self.unknown3, self.unknown4)
        else:
            packed_data = struct.pack("<QIBBBBiI", strings_name_index_dict[self.name_index],
                self.arg_type, self.unknown1, self.unknown2, self.unknown3, 
                self.unknown4, enum_table_offset, 0)
            packed_data += struct.pack("<" + (TYPE_DICT[self.arg_type] * 4), 
                self.arg_default, self.arg_min, self.arg_max, self.arg_increment)
            packed_data += struct.pack("<Q", strings_name_index_dict[self.format_string_index])
        return packed_data
        
    def to_serializeable(self, enums_list, strings_list):
        enum_name = None
        if self.enum_index != -1:
            enum_name = strings_list[enums_list[self.enum_index].name_index]
            
        if self.arg_type == 8:
            default = strings_list[self.arg_default]
        else:
            default = self.arg_default
        
        return serial.Serializeable_EDF_Argument(**{
         'name': strings_list[self.name_index],
         'type': self.arg_type,
         'enum_name': enum_name,
         'default': default,
         'min': self.arg_min,
         'max': self.arg_max,
         'increment': self.arg_increment,
         'format_string': strings_list[self.format_string_index],
         'unk1': self.unknown1,
         'unk2': self.unknown2,
         'unk3': self.unknown3,
         'unk4': self.unknown4
        })
        
    @classmethod
    def get_size(cls, filetype):
        if filetype == EDF_Filetype.DARK_SOULS_1:
            return struct.calcsize("<IIi IIII IBBBB")
        else:
            return struct.calcsize("<QIBBBBi xxxx QQQQ Q")
    
class EDF_Instr:
    def __init__(self, instr_index, num_of_arguments, starting_arg_index, name_index):
        self.index = instr_index
        self.num_of_arguments = num_of_arguments
        self.starting_arg_index = starting_arg_index
        self.name_index = name_index
    
    @classmethod    
    def from_file_content(cls, content, offset, strings_offset_dict, filetype):
        master_offset = offset
        
        if filetype == EDF_Filetype.DARK_SOULS_1:
            ((instr_index, num_of_arguments, arg_table_offset, name_offset),
                master_offset) = extract_struct("<IIII", content, master_offset)
            master_offset = consume_byte(content, master_offset, b'\x00', 4)
        else:
            ((instr_index, num_of_arguments, arg_table_offset, name_offset),
                master_offset) = extract_struct("<QQQQ", content, master_offset)
        
        starting_arg_index = arg_table_offset // EDF_Argument.get_size(filetype)
        name_index = strings_offset_dict[name_offset]
        
        return (EDF_Instr(instr_index, num_of_arguments, 
            starting_arg_index, name_index), master_offset)
    
    def to_string(self):
        return ("EDF_Instr[index=%d, args=[%d,%d), name_index=%d]" %
            (self.index, self.starting_arg_index, self.starting_arg_index +
                self.num_of_arguments, self.name_index))
    
    def to_binary(self, strings_name_index_dict, filetype):
        if filetype == EDF_Filetype.DARK_SOULS_1:
            return struct.pack("<IIIII", self.index, self.num_of_arguments, 
                self.starting_arg_index * EDF_Argument.get_size(filetype),
                strings_name_index_dict[self.name_index], 0)
        else:
            return struct.pack("<QQQQ", self.index, self.num_of_arguments, 
                self.starting_arg_index * EDF_Argument.get_size(filetype),
                strings_name_index_dict[self.name_index])
            
    def to_serializeable(self, args_list, enums_list, strings_list):
        args = [args_list[i].to_serializeable(enums_list, strings_list) 
         for i in range(self.starting_arg_index, 
          self.starting_arg_index + self.num_of_arguments)]
        return serial.Serializeable_EDF_Instruction(**{
         'name': strings_list[self.name_index],
         'index': self.index,
         'args': args
        })
        
    @classmethod
    def get_size(cls, filetype):
        if filetype == EDF_Filetype.DARK_SOULS_1:
            return struct.calcsize("<IIII xxxx")
        else:
            return struct.calcsize("<QQQQ")

class EDF_Class:
    def __init__(self, class_index, starting_instr_index, num_of_class_instructions, name_index):
        self.index = class_index
        self.starting_instr_index = starting_instr_index
        self.num_of_instrs = num_of_class_instructions
        self.name_index = name_index
        
    @classmethod
    def from_file_content(cls, content, offset, strings_offset_dict, filetype):
        master_offset = offset
        
        if filetype == EDF_Filetype.DARK_SOULS_1:
            ((class_index, num_of_class_instructions, instruction_table_offset, 
                name_offset), master_offset) = extract_struct("<IIII", content, master_offset)
            master_offset = consume_byte(content, master_offset, b'\x00', 4)
        else:
            ((class_index, num_of_class_instructions, instruction_table_offset, 
                name_offset), master_offset) = extract_struct("<QQQQ", content, master_offset)
        
        starting_instr_index = instruction_table_offset // EDF_Instr.get_size(filetype)
        name_index = strings_offset_dict[name_offset]
        return (EDF_Class(class_index, starting_instr_index, 
            num_of_class_instructions, name_index), master_offset)

    def to_string(self):
        return ("EDF_Class[index=%d, instrs=[%d:%d), name_index=%d]" %
            (self.index, self.starting_instr_index, self.starting_instr_index + 
                self.num_of_instrs, self.name_index))
                
    def to_binary(self, strings_name_index_dict, filetype):
        if filetype == EDF_Filetype.DARK_SOULS_1:
            return struct.pack("<IIIII", self.index, self.num_of_instrs,
                self.starting_instr_index * EDF_Instr.get_size(filetype),
                strings_name_index_dict[self.name_index], 0)
        else:
            return struct.pack("<QQQQ", self.index, self.num_of_instrs,
                self.starting_instr_index * EDF_Instr.get_size(filetype),
                strings_name_index_dict[self.name_index])
            
    def to_serializeable(self, instrs_list, args_list, enums_list, strings_list):
    
        instrs = [instrs_list[i].to_serializeable(args_list, enums_list, strings_list) 
         for i in range(self.starting_instr_index, 
          self.starting_instr_index + self.num_of_instrs)]
        return serial.Serializeable_EDF_Class(**{
         'name': strings_list[self.name_index],
         'index': self.index,
         'instrs': instrs
        })
    
    @classmethod
    def get_size(cls, filetype):
        if filetype == EDF_Filetype.DARK_SOULS_1:
            return struct.calcsize("<IIII xxxx")
        else:
            return struct.calcsize("<QQQQ")
        

    
class EDF_Struct:
    def __init__(self, unknown, main_classes_list, main_instrs_list, 
     main_args_list, extra_classes_list, extra_instrs_list, 
     extra_args_list, enums_list, enum_values_list, strings_list)  :
        self.unknown = unknown
        self.main_classes_list = main_classes_list
        self.main_instrs_list = main_instrs_list
        self.main_args_list = main_args_list
        self.extra_classes_list = extra_classes_list
        self.extra_instrs_list = extra_instrs_list
        self.extra_args_list = extra_args_list
        self.enums_list = enums_list
        self.enum_values_list = enum_values_list
        self.strings_list = strings_list
    
    @classmethod
    def from_file_content(cls, content):
        master_offset = 0
        
        master_offset = consume_byte(content, master_offset, b'\x45', 1)
        master_offset = consume_byte(content, master_offset, b'\x44', 1)
        master_offset = consume_byte(content, master_offset, b'\x46', 1)
        master_offset = consume_byte(content, master_offset, b'\x00', 1)
        
        ((version_part_1, version_part_2), master_offset) = extract_struct("<II", content, master_offset)
        if version_part_1 == 0x00000000 and version_part_2 == 0x00CC0065:
            filetype = EDF_Filetype.DARK_SOULS_1
            header_single_format_string = "<I"
            header_pair_format_string = "<II"
        elif version_part_1 == 0x0000FF00 and version_part_2 == 0x00CC0065:
            filetype = EDF_Filetype.BLOODBORNE
            header_single_format_string = "<Q"
            header_pair_format_string = "<QQ"
        else:
            raise ValueError(("Unrecognized version bytes %#010x %#010x." + 
                "Could not determine EDF version.") % (version_part_1, version_part_2))
        
        ((filesize,), master_offset) = extract_struct("<I", content, master_offset)
        ((num_of_classes_main, classes_offset_main), 
            master_offset) = extract_struct(header_pair_format_string, content, master_offset)
        ((num_of_instructions_main, instructions_offset_main), 
            master_offset) = extract_struct(header_pair_format_string, content, master_offset)
        ((num_of_arguments_main, arguments_offset_main), 
            master_offset) = extract_struct(header_pair_format_string, content, master_offset)
            
        ((num_of_classes_extra, classes_offset_extra), 
            master_offset) = extract_struct(header_pair_format_string, content, master_offset)
        ((num_of_instructions_extra, instructions_offset_extra), 
            master_offset) = extract_struct(header_pair_format_string, content, master_offset)
        ((num_of_arguments_extra, arguments_offset_extra), 
            master_offset) = extract_struct(header_pair_format_string, content, master_offset)
            
        ((num_of_enums, enums_offset), 
            master_offset) = extract_struct(header_pair_format_string, content, master_offset)
        ((num_of_enum_values, enum_values_offset), 
            master_offset) = extract_struct(header_pair_format_string, content, master_offset)
        ((length_of_packed_strings, packed_strings_offset), 
            master_offset) = extract_struct(header_pair_format_string, content, master_offset)
        ((unknown,), master_offset) = extract_struct(header_single_format_string, content, master_offset)
        
        if filetype == EDF_Filetype.DARK_SOULS_1:
            master_offset = consume_byte(content, master_offset, b'\x00', 4)
        
        # Check sizes of offsets.
        if master_offset != classes_offset_main:
            log.error("Main class table offset mismatch! Expected %#010x but was at %#010x." %
                (classes_offset_main, master_offset))
        actual_instr_offset_main = classes_offset_main + (num_of_classes_main * EDF_Class.get_size(filetype))
        if actual_instr_offset_main != instructions_offset_main:
            log.error("Main instruction table offset mismatch! Expected %#010x but was at %#010x." %
                (instructions_offset_main, actual_instr_offset_main))
        actual_argument_offset_main = instructions_offset_main + (num_of_instructions_main * EDF_Instr.get_size(filetype))
        if actual_argument_offset_main != arguments_offset_main:
            log.error("Main argument table offset mismatch! Expected %#010x but was at %#010x." %
                (arguments_offset_main, actual_argument_offset_main))
        actual_classes_offset_extra = arguments_offset_main + (num_of_arguments_main * EDF_Argument.get_size(filetype))
        if actual_classes_offset_extra != classes_offset_extra:
            log.error("Extra class table offset mismatch! Expected %#010x but was at %#010x." %
                (classes_offset_extra, actual_classes_offset_extra))
        actual_instr_offset_extra = classes_offset_extra + (num_of_classes_extra * EDF_Class.get_size(filetype))
        if actual_instr_offset_extra != instructions_offset_extra:
            log.error("Extra instruction table offset mismatch! Expected %#010x but was at %#010x." %
                (instructions_offset_extra, actual_instr_offset_extra))
        actual_argument_offset_extra = instructions_offset_extra + (num_of_instructions_extra * EDF_Instr.get_size(filetype))
        if actual_argument_offset_extra != arguments_offset_extra:
            log.error("Extra argument table offset mismatch! Expected %#010x but was at %#010x." %
                (arguments_offset_extra, actual_argument_offset_extra))
        actual_enums_offset = arguments_offset_extra + (num_of_arguments_extra * EDF_Argument.get_size(filetype))
        if actual_enums_offset != enums_offset:
            log.error("Enums table offset mismatch! Expected %#010x but was at %#010x." %
                (enums_offset, actual_enums_offset))
        actual_enum_values_offset = enums_offset + (num_of_enums * EDF_Enum.get_size(filetype))
        if actual_enum_values_offset != enum_values_offset:
            log.error("Enum values table offset mismatch! Expected %#010x but was at %#010x." %
                (enum_values_offset, actual_enum_values_offset))
        actual_strings_offset = enum_values_offset + (num_of_enum_values * EDF_EnumValue.get_size(filetype))
        if actual_strings_offset != packed_strings_offset:
            log.error("Strings table offset mismatch! Expected %#010x but was at %#010x." %
                (packed_strings_offset, actual_strings_offset))
        actual_filesize = packed_strings_offset + length_of_packed_strings
        if actual_filesize != filesize:
            log.error("End of file mismatch! Expected %#010x but was at %#010x." %
                (filesize, actual_filesize))
                
        # Parse packed strings table into list for future reference.
        strings_offset_dict = {}
        strings_list = []
        offset_into_strings_table = 0
        count = 0
        while offset_into_strings_table < length_of_packed_strings:
            strings_offset_dict[offset_into_strings_table] = count
            (unpacked_string, length) = extract_utf16z(content, packed_strings_offset + offset_into_strings_table)
            offset_into_strings_table += length
            
            # Fix malformed format string.
            if unpacked_string == "%0.3ｆ":
                unpacked_string = "%0.3f"
            
            strings_list.append(unpacked_string)  # strings_list[count] = unpacked_string
            count += 1
        
        main_classes_list = []
        for _ in range(num_of_classes_main):
            (extracted_class, master_offset) = EDF_Class.from_file_content(content, master_offset, strings_offset_dict, filetype)
            main_classes_list.append(extracted_class)
        main_instrs_list = []
        for _ in range(num_of_instructions_main):
            (extracted_instr, master_offset) = EDF_Instr.from_file_content(content, master_offset, strings_offset_dict, filetype)
            main_instrs_list.append(extracted_instr)
        main_args_list = []
        for _ in range(num_of_arguments_main):
            (extracted_arg, master_offset) = EDF_Argument.from_file_content(content, master_offset, strings_offset_dict, filetype)
            main_args_list.append(extracted_arg)
        extra_classes_list = []
        for _ in range(num_of_classes_extra):
            (extracted_class, master_offset) = EDF_Class.from_file_content(content, master_offset, strings_offset_dict, filetype)
            extra_classes_list.append(extracted_class)
        extra_instrs_list = []
        for _ in range(num_of_instructions_extra):
            (extracted_instr, master_offset) = EDF_Instr.from_file_content(content, master_offset, strings_offset_dict, filetype)
            extra_instrs_list.append(extracted_instr)
        extra_args_list = []
        for _ in range(num_of_arguments_extra):
            (extracted_arg, master_offset) = EDF_Argument.from_file_content(content, master_offset, strings_offset_dict, filetype)
            extra_args_list.append(extracted_arg)
        enums_list = []
        for _ in range(num_of_enums):
            (extracted_enum, master_offset) = EDF_Enum.from_file_content(content, master_offset, strings_offset_dict, filetype)
            enums_list.append(extracted_enum)
        enum_values_list = []
        for _ in range(num_of_enum_values):
            (extracted_enum_value, master_offset) = EDF_EnumValue.from_file_content(content, master_offset, strings_offset_dict, filetype)
            enum_values_list.append(extracted_enum_value)      
        
        return EDF_Struct(unknown, main_classes_list, main_instrs_list, 
            main_args_list, extra_classes_list, extra_instrs_list, 
            extra_args_list, enums_list, enum_values_list, strings_list)        
        
    def to_string(self):
        return_list = []
        return_list.append("EDF_Struct[unknown=%d, ..." % self.unknown)
        return_list.append(" Main Classes:")
        for (index, c) in enumerate(self.main_classes_list):
            return_list.append("  [%d] " % index + c.to_string())
        return_list.append(" Main Instructions:")
        for (index, i) in enumerate(self.main_instrs_list):
            return_list.append("  [%d] " % index + i.to_string())
        return_list.append(" Main Arguments:")
        for (index, a) in enumerate(self.main_args_list):
            return_list.append("  [%d] " % index + a.to_string())
        return_list.append(" Extra Classes:")
        for (index, c) in enumerate(self.extra_classes_list):
            return_list.append("  [%d] " % index + c.to_string())
        return_list.append(" Extra Instructions:")
        for (index, i) in enumerate(self.extra_instrs_list):
            return_list.append("  [%d] " % index + i.to_string())
        return_list.append(" Extra Arguments:")
        for (index, a) in enumerate(self.extra_args_list):
            return_list.append("  [%d] " % index + a.to_string())
        return_list.append(" Enums:")
        for (index, e) in enumerate(self.enums_list):
            return_list.append("  [%d] " % index + e.to_string())
        return_list.append(" Enum Values:")
        for (index, v) in enumerate(self.enum_values_list):
            return_list.append("  [%d] " % index + v.to_string())
        return_list.append(" Strings:")
        for (index, s) in enumerate(self.strings_list):
            return_list.append("  [%d] '" % index + s + "'")
        return_list.append("]")
        return "\n".join(return_list)
        
    def to_binary(self, filetype):
        # Build string name index -> strings table offset dict
        packed_strings_data = ""
        strings_name_index_dict = {}
        for (index, s) in enumerate(self.strings_list):
            strings_name_index_dict[index] = len(packed_strings_data)
            packed_strings_data += s.decode("utf-8").encode("utf-16le") + b'\x00\x00'

        if filetype == EDF_Filetype.DARK_SOULS_1:
            header_size = struct.calcsize("<4sIII 18I I xxxx")
        else:
            header_size = struct.calcsize("<4sIII 18Q Q")
        
        packed_data = ""
        offset_to_main_class_table = len(packed_data) + header_size
        for c in self.main_classes_list:
            packed_data += c.to_binary(strings_name_index_dict)
        offset_to_main_instr_table = len(packed_data) + header_size
        for i in self.main_instrs_list:
            packed_data += i.to_binary(strings_name_index_dict)
        offset_to_main_arg_table = len(packed_data) + header_size
        for a in self.main_args_list:
            packed_data += a.to_binary(strings_name_index_dict)
        offset_to_extra_class_table = len(packed_data) + header_size
        for c in self.extra_classes_list:
            packed_data += c.to_binary(strings_name_index_dict)
        offset_to_extra_instr_table = len(packed_data) + header_size
        for i in self.extra_instrs_list:
            packed_data += i.to_binary(strings_name_index_dict)
        offset_to_extra_arg_table = len(packed_data) + header_size
        for a in self.extra_args_list:
            packed_data += a.to_binary(strings_name_index_dict)
        offset_to_enum_table = len(packed_data) + header_size
        for e in self.enums_list:
            packed_data += e.to_binary(strings_name_index_dict)
        offset_to_enum_values_table = len(packed_data) + header_size
        for v in self.enum_values_list:
            packed_data += v.to_binary(strings_name_index_dict)
        offset_to_strings_table = len(packed_data) + header_size
        packed_data += packed_strings_data
        filesize = len(packed_data) + header_size
        
        if filetype == EDF_Filetype.DARK_SOULS_1:
            packed_data_header = b"EDF\x00" + b"\x00\x00\x00\x00\x65\x00\xCC\x00"
            packed_data_header += struct.pack("<I 18I II", filesize, len(self.main_classes_list),
                offset_to_main_class_table, len(self.main_instrs_list),
                offset_to_main_instr_table, len(self.main_args_list),
                offset_to_main_arg_table, len(self.extra_classes_list),
                offset_to_extra_class_table, len(self.extra_instrs_list),
                offset_to_extra_instr_table, len(self.extra_args_list),
                offset_to_extra_arg_table, len(self.enums_list),
                offset_to_enum_table, len(self.enum_values_list),
                offset_to_enum_values_table, len(packed_strings_data),
                offset_to_strings_table, self.unknown, 0)
        else:
            packed_data_header = b"EDF\x00" + b"\x00\xFF\x00\x00\x65\x00\xCC\x00"
            packed_data_header += struct.pack("<I 18Q Q", filesize, len(self.main_classes_list),
                offset_to_main_class_table, len(self.main_instrs_list),
                offset_to_main_instr_table, len(self.main_args_list),
                offset_to_main_arg_table, len(self.extra_classes_list),
                offset_to_extra_class_table, len(self.extra_instrs_list),
                offset_to_extra_instr_table, len(self.extra_args_list),
                offset_to_extra_arg_table, len(self.enums_list),
                offset_to_enum_table, len(self.enum_values_list),
                offset_to_enum_values_table, len(packed_strings_data),
                offset_to_strings_table, self.unknown)
        return packed_data_header + packed_data
        
    def to_serializeable(self):
        main_classes = [c.to_serializeable(self.main_instrs_list, self.main_args_list, 
         self.enums_list, self.strings_list) for c in self.main_classes_list]
        extra_classes = [c.to_serializeable(self.extra_instrs_list, self.extra_args_list, 
         self.enums_list, self.strings_list) for c in self.extra_classes_list]
        enums = [e.to_serializeable(self.enum_values_list, self.strings_list) for e in self.enums_list]
        return serial.Serializeable_EDF_Struct(**{
         'unknown': self.unknown, 
         'main_classes': main_classes,
         'extra_classes': extra_classes,
         'enums': enums
        })
        

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.WARN)
    if len(sys.argv) == 1:
        print("Usage: " + sys.argv[0] + " <EMEDF File>")
    else:
        with open(sys.argv[1], "rb") as f:
            content = f.read()
            edf_data = EDF_Struct.from_file_content(content)
            edf_data.main_classes_list.sort(key=lambda x: x.index)
            print(edf_data.to_serializeable().to_pretty_string(suppress_unknown_arg_data = True))
