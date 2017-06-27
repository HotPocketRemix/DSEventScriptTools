import struct
import evd_command_to_readable

COMMAND_ARG_TYPE_DICT = {

2000: {0: '@iII', 1: '@iI', 2: '@B', 3: '@B', 4: '@I', 5: '@B'}, \
2001: {}, \
2002: {1: '@iI', 2: '@iIiBB', 3: '@iIi', 4: '@iIiBBi', 5: '@iIffifi'}, \
2003: {1: '@iiBB', 2: '@iB', 3: '@iB', 4: '@i', 5: '@iiiiiii', 6: '@iB', \
        7: '@iB', 8: '@iiB', 9: '@i', 10: '@h', 11: '@bihh', 12: '@i', \
        13: '@iIB', 14: '@BBi', 15: '@i', 16: '@I', 17: '@IIB', 18: '@iiBBB', \
        19: '@hh', 20: '@i', 21: '@B', 22: '@iiB', 23: '@i', 24: '@iii', \
        25: '@iiiii', 26: '@iB', 27: '@B', 28: '@i', 29: '@Bb', 30: '@B', \
        31: '@iII', 32: '@iI', 33: '@i', 34: '@iiii', 35: '@ii', 36: '@i', \
        37: '@', 38: '@', 39: '@', 40: '@', 41: '@iifi'}, \
2004: {1: '@iB', 2: '@iB', 3: '@iBii', 4: '@iB', 5: '@iB', 6: '@iiB', \
        7: '@i', 8: '@ii', 9: '@iiiiii', 10: '@iB', 11: '@ii', 12: '@iB', \
        13: '@ii', 14: '@ii', 15: '@iB', 16: '@i', 17: '@iiB', 18: '@iif', \
        19: '@ii', 20: '@i', 21: '@ii', 22: '@ihhiffBB', 23: '@iiiB', \
        24: '@iiii', 25: '@iif', 26: '@iBB', 27: '@iBB', 28: '@ii', \
        29: '@iB', 30: '@iB', 31: '@iB', 32: '@iiBii', 33: '@ii', 34: '@iBb', \
        35: '@iB', 36: '@iii', 37: '@i', 38: '@B', 39: '@iB', 40: '@iBiii', \
        41: '@iBii', 42: '@iBiii', 43: '@iB', 44: '@iB', 45: '@ii', \
        46: '@B', 47: '@'}, \
2005: {1: '@ib', 2: '@i', 3: '@iB', 4: '@iB', 5: '@iii', 6: '@iiB', \
        7: '@ii', 8: '@ib', 9: '@iiiiifff', 10: '@iBBB', 11: '@iih', \
        12: '@i', 13: '@iB', 14: '@iiiB', 15: '@i'}, \
2006: {1: '@iB', 2: '@i', 3: '@iiii', 4: '@iii', 5: '@ii'}, \
2007: {1: '@ihhif', 2: '@B', 3: '@iB', 4: '@iB', 5: '@i', 6: '@i', 7: '@i', \
        8: '@i', 9: '@i'}, \
2008: {1: '@ii', 2: '@iiiiff', 3: '@BBH'}, \
2009: {0: '@iii', 1: '@iii', 2: '@iii', 3: '@iiffi', 4: '@i', 5: '@ii', 6: '@B'}, \
2010: {1: '@BHiii', 2: '@iii', 3: '@iB'}, \
2011: {1: '@iB', 2: '@iB'}, \
2012: {1: '@iB'}, \
1000: {0: '@Bb', 1: '@BBb', 2: '@BBb', 3: '@B', 4: '@B', 5: '@Bbii', \
        6: '@Bbii', 7: '@BBb', 8: '@BBb', 9: '@f'}, \
1001: {0: '@f', 1: '@i', 2: '@ff', 3: '@ii'}, \
1003: {0: '@BBi', 1: '@BBBi', 2: '@BBBi', 3: '@BBBii', 4: '@BBBii', 5: '@Bb', \
        6: '@Bb', 7: '@BBBB', 8: '@BBBB'}, \
1005: {0: '@Bi', 1: '@BBi', 2: '@BBi'}, \
0: {0: '@bBb', 1: '@bbii'}, \
1: {0: '@bf', 1: '@bi', 2: '@bff', 3: '@bii'}, \
3: {0: '@bBBi', 1: '@bBBii', 2: '@bBii', 3: '@bBiif', 4: '@bBiB', 5: '@biifhfiBi', \
    6: '@bb', 7: '@bBi', 8: '@bBBB', 9: '@bI', 10: '@bBiibi', 11: '@bBBB', \
    12: '@biBBI', 13: '@biifhfiBi', 14: '@bi', 15: '@bii', 16: '@bBiB', \
    17: '@bBB', 18: '@biifhfiBii', 19: '@biifhfiBii', 20: '@biBBiB', 
    21: '@bB', 22: '@bB'}, \
4: {0: '@biB', 1: '@bii', 2: '@bibf', 3: '@bib', 4: '@biiB', 5: '@biiB', \
    6: '@biiib', 7: '@biB', 8: '@biiB', 9: '@biB', 10: '@bB', 11: '@bB', \
    12: '@bB', 13: '@bBI', 14: '@biBi'}, \
5: {0: '@bBi', 1: '@bii', 2: '@bi', 3: '@bibi'}, \
11: {0: '@bi', 1: '@bi', 2: '@bi'}

}

def get_byte_offset_from_struct(struct_format):
    """Computes an array of byte offsets from a struct format string.
    The ith element of the array indicates which byte in the struct is
    the first byte of the value packed as the ith character of the format 
    string.
    """
    
    endian = struct_format[0]
    format_string = struct_format[1:]
    byte_offset_array = {}
    for i in xrange(0, len(format_string)):
        byte_offset_array[struct.calcsize(endian + format_string[:i+1]) - struct.calcsize(endian + format_string[i])] = \
            (i , format_string[i])
    return byte_offset_array

class ParameterReplacement:
    def __init__(self, instr_number, destination_starting_byte = 0, source_starting_byte = 0, length = 0):
        self.instr_number = instr_number
        self.destination_starting_byte = destination_starting_byte
        self.source_starting_byte = source_starting_byte
        self.length = length
        
    def export_as_raw_numeric(self):
        return "(%d <- %d, %d)" % (self.destination_starting_byte, self.source_starting_byte, self.length)
        
    def export_as_binary(self):
        return struct.pack("@IIII4x", self.instr_number, self.destination_starting_byte, self.source_starting_byte, self.length)

class Instruction:
    def __init__(self, instr_class, instr_index, arg_format_string = "", argument_list = [], parameter_replacements = []):
        if len(arg_format_string.translate(None, '|')) != len(argument_list):
            raise ValueError("Cannot initialize Instruction [" + str(instr_class) + "][" + str(instr_index) +\
                "] with argument format string \"" + arg_format_string +\
                "\" due to argument list length mismatch (" + str(len(argument_list)) + ").")
        self.instr_class = instr_class
        self.instr_index = instr_index
        self.arg_format_string = arg_format_string
        self.argument_list = argument_list
        self.parameter_replacements = parameter_replacements
      
    def get_argument_byte_count(self):
        return struct.calcsize("@" + self.arg_format_string.translate(None, "|") + "0i")
    
    def count_parameter_replacements(self):
        return len(self.parameter_replacements)
        
    def append_parameter_replacement(self, param):
        self.parameter_replacements.append(param)
        
    def export_as_raw_numeric(self):
        arg_list_string = "[" + ", ".join([str(i) for i in self.argument_list]) + "]"
        returnList = ["%4d[%02d] (%s)" % (self.instr_class, self.instr_index, self.arg_format_string) + arg_list_string]
        for param in self.parameter_replacements:
            returnList.append("   ^" + param.export_as_raw_numeric())
        return returnList
        
    def export_as_human_readable(self):    
        fixed_args = []
        var_args = []
        
        split_point = self.arg_format_string.find('|')
        if split_point == -1:
            fixed_args = self.argument_list
            var_args = []
        else:
            fixed_args = self.argument_list[:split_point]
            var_args = self.argument_list[split_point:]
        return evd_command_to_readable.translate(self.instr_class, self.instr_index, fixed_args, var_args)
        
    def apply_parameter_replacement(self):
        """Applies any parameter replacement instructions to this instruction,
        which replaces the dummy value of the argument with a string 
        representation of the bytes of the parameter array.
        
        Returns the parameter strings used as replacements, as well as
        a dictionary with guesses as to the format string types that 
        should be used to represent each parameter.
        """
        
        PERMITTED = [0, 0.0, -1, 1]
        struct_offset_dict = get_byte_offset_from_struct("@" + self.arg_format_string.translate(None, "|"))
        
        instr_parameter_set = set()
        instr_parameter_types = {}
        
        for param in self.parameter_replacements:
            if param.destination_starting_byte not in struct_offset_dict:
                raise ValueError("Parameter destination " + str(param.destination_starting_byte) + \
                    " is misaligned with target instruction row (format: '" + self.arg_format_string + "').")
            (argument_index, argument_byte_type) = struct_offset_dict[param.destination_starting_byte]
            if struct.calcsize(argument_byte_type) < param.length:
                raise ValueError("Parameter of length " + str(param.length) + \
                    " will not fit in destination of length " + str(struct.calcsize(argument_byte_type)) + ".")
            value_to_overwrite = self.argument_list[argument_index]
            parameter_name = 'X' + str(param.source_starting_byte) + ':' + str(param.source_starting_byte + param.length - 1)
                
            if (value_to_overwrite not in PERMITTED) and value_to_overwrite != parameter_name:
                raise ValueError("Parameter is overwriting non-zero value " + str(value_to_overwrite) + ".")
            
            self.argument_list[argument_index] = parameter_name
            
            instr_parameter_set.add((param.source_starting_byte, param.source_starting_byte + param.length - 1))
            if parameter_name not in instr_parameter_types:
                instr_parameter_types[parameter_name] = set(argument_byte_type)
            else:
                instr_parameter_types[parameter_name].add(argument_byte_type)
        return (instr_parameter_set, instr_parameter_types)
        
    def export_argument_list_as_binary(self):
        format_string = "@" + self.arg_format_string.translate(None, "|") + "0i"
        return struct.pack(format_string, *self.argument_list)
        
    def export_parameter_replacements_as_binary(self):
        return "".join([param.export_as_binary() for param in self.parameter_replacements])
    
    def export_as_binary(self, arg_offset):
        return struct.pack("@IIIIi4x", self.instr_class, self.instr_index, self.get_argument_byte_count(), arg_offset, -1)

class Event:
    def __init__(self, event_id = 0, unknown_int = 0, instr_list = []):
        self.event_id = event_id
        self.unknown_int = unknown_int
        self.instr_list = instr_list
    
    def count_instructions(self):
        return len(self.instr_list)
        
    def get_total_argument_byte_count(self):
        return sum([i.get_argument_byte_count() for i in self.instr_list])
        
    def count_total_parameter_replacements(self):
        return sum([i.count_parameter_replacements() for i in self.instr_list])
        
    def export_as_raw_numeric(self):
        returnString = str(self.event_id) + ", " + str(self.unknown_int)
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
            
    def export_as_human_readable(self, suppress_line_numbers = False):
        returnString = "Event ID: " + str(self.event_id) + ", Int: " + str(self.unknown_int)
        returnString += "\n" + self.build_parameter_types()
        for i, instr in enumerate(self.instr_list):
            returnString += "\n    "
            if not suppress_line_numbers:
                returnString += "%3d" % i + ' '
            returnString += instr.export_as_human_readable()
        return returnString
        
    def export_as_binary(self, instr_offset, arg_offset, param_offset):
        total_params = self.count_total_parameter_replacements()
        if total_params == 0:
            param_offset = -1
        event_binary = struct.pack("@IIIIiI4x", self.event_id, self.count_instructions(),
            instr_offset, total_params, param_offset, self.unknown_int)
            
        instrs_binary = ""
        args_binary = ""
        params_list = []
        for instr in self.instr_list:
            instrs_binary += instr.export_as_binary(arg_offset)
            
            a_bin = instr.export_argument_list_as_binary()
            args_binary += a_bin
            arg_offset += len(a_bin)
            
            params_list += instr.parameter_replacements
        # Collect and sort parameter replacements to better match actual .emevd files. (Should be purely cosmetic)
        sorted_params_list = sorted(params_list, key=lambda param: (param.source_starting_byte, param.instr_number))
        params_binary = "".join([param.export_as_binary() for param in sorted_params_list])
            
        return (event_binary, instrs_binary, args_binary, params_binary)
            

HEADER_SIZE = 84           # Constant size of the .emevd data header
EVENT_TABLE_ROW_SIZE = 28  # Size of each entry in the event table
INSTR_TABLE_ROW_SIZE = 24  # Size of each entry in the instruction table
PARAM_TABLE_ROW_SIZE = 20  # Size of each entry in the parameter replacement table     

class EmevdData:
    def __init__(self, event_list = []):
        self.event_list = event_list
        
    @classmethod
    def build_from_emevd_file_content(cls, file_content):
        import emevd_opener
        return EmevdData(emevd_opener.emevd_file_content_to_event_list(file_content))
        
    @classmethod
    def build_from_raw_numeric_file_content(cls, file_content):
        import emevd_opener
        return EmevdData(emevd_opener.raw_numeric_file_content_to_event_list(file_content))
    
    def count_events(self):
        return len(self.event_list)
        
    def count_total_instructions(self):
        return sum([i.count_instructions() for i in self.event_list])
        
    def get_total_argument_byte_count(self):
        # There is a z4 after the Argument data, but it is included in the byte count
        #  for the Argument data given in the header.
        return sum([i.get_total_argument_byte_count() for i in self.event_list]) + 4 

    def count_total_parameter_replacements(self):
        return sum([i.count_total_parameter_replacements() for i in self.event_list])
        
    def compute_event_table_offset(self):
        return HEADER_SIZE 
        
    def compute_instruction_table_offset(self):
        return self.compute_event_table_offset() + EVENT_TABLE_ROW_SIZE * self.count_events()
        
    def compute_argument_data_offset(self):
        return self.compute_instruction_table_offset() + INSTR_TABLE_ROW_SIZE * self.count_total_instructions()
        
    def compute_parameter_table_offset(self):
        return self.compute_argument_data_offset() + self.get_total_argument_byte_count() 
        
    def compute_file_size(self):
        return self.compute_parameter_table_offset() + PARAM_TABLE_ROW_SIZE * self.count_total_parameter_replacements()
        
    def build_emevd_header(self):
        file_size = self.compute_file_size()
        event_count = self.count_events()
        instr_count = self.count_total_instructions()
        args_length = self.get_total_argument_byte_count()
        param_count = self.count_total_parameter_replacements()
        event_offset = self.compute_event_table_offset()
        instr_offset = self.compute_instruction_table_offset()
        args_offset = self.compute_argument_data_offset()
        param_offset = self.compute_parameter_table_offset()
        return struct.pack("@cccx 4x c3x 5I 4xI4xI 2I 4xI 2I 4xI4x", 'E', 'V', 'D', '\xCC',
            file_size, event_count, event_offset, instr_count, instr_offset,
            args_offset, args_offset, param_count, param_offset, file_size,
            args_length, args_offset, file_size)
        
    def export_as_raw_numeric(self):
        return "\n\n".join([event.export_as_raw_numeric() for event in self.event_list])
    
    def export_as_human_readable(self, suppress_line_numbers = False):
        return "\n\n".join([event.export_as_human_readable(suppress_line_numbers) for event in self.event_list])
    
    def export_as_emevd(self):
        event_table_binary = ""
        instr_table_binary = ""
        argument_data_binary = ""
        param_table_binary = ""
        
        current_instr_table_offset = 0
        current_argument_data_length = 0
        current_param_table_offset = 0
        
        header = self.build_emevd_header()
       
        for e in self.event_list:
            (e_bin, i_bin, a_bin, p_bin) = e.export_as_binary(current_instr_table_offset, current_argument_data_length, current_param_table_offset)
            
            event_table_binary += e_bin
            instr_table_binary += i_bin
            argument_data_binary += a_bin
            param_table_binary += p_bin
            
            if len(i_bin) != INSTR_TABLE_ROW_SIZE * e.count_instructions():
                raise ValueError("Event ID: " + str(e.event_id) + " returned packed instruction binary of size " +\
                    str(len(i_bin)) + " but reports " + str(e.count_instructions()) + " total instructions (with expected size " +\
                    str(INSTR_TABLE_ROW_SIZE * e.count_instructions()) + ").")
            if len(p_bin) != PARAM_TABLE_ROW_SIZE * e.count_total_parameter_replacements():
                raise ValueError("Event ID: " + str(e.event_id) + " returned packed parameter replacement binary of size " +\
                    str(len(p_bin)) + " but reports " + str(e.count_total_parameter_replacements()) + " total replacements (with expected size " +\
                    str(PARAM_TABLE_ROW_SIZE * e.count_total_parameter_replacements()) + ").")
            if len(a_bin) != e.get_total_argument_byte_count():
                raise ValueError("Event ID: " + str(e.event_id) + " returned packed argument data binary of size " +\
                    str(len(p_bin)) + " but reports expected size to be" + str(e.get_total_argument_byte_count()) + ".")
            
            current_instr_table_offset += len(i_bin)
            current_argument_data_length += len(a_bin)
            current_param_table_offset += len(p_bin)
        
        argument_data_binary += "\x00\x00\x00\x00" # Termination z4 for the packed ArgumentData
        
        emevd_binary = ""
        if len(header) != self.compute_event_table_offset():
            raise ValueError("Header was of size " + str(len(header)) + " but expected size was " + str(HEADER_SIZE) + ".")
        emevd_binary += header
        if len(emevd_binary) + len(event_table_binary) != self.compute_instruction_table_offset():
            raise ValueError("Event table was of size " + str(len(event_table_binary)) + " but expected size was " +\
                str(self.compute_instruction_table_offset() - len(emevd_binary)) + ".")
        emevd_binary += event_table_binary
        if len(emevd_binary) + len(instr_table_binary) != self.compute_argument_data_offset():
            raise ValueError("Instruction table was of size " + str(len(instr_table_binary)) + " but expected size was " +\
                str(self.compute_argument_data_offset() - len(emevd_binary)) + ".")
        emevd_binary += instr_table_binary
        if len(emevd_binary) + len(argument_data_binary) != self.compute_parameter_table_offset():
            raise ValueError("Argument data was of size " + str(len(argument_data_binary)) + " but expected size was " +\
                str(self.compute_parameter_table_offset() - len(emevd_binary)) + ".")
        emevd_binary += argument_data_binary
        if len(emevd_binary) + len(param_table_binary) != self.compute_file_size():
            raise ValueError("Parameter replacement table was of size " + str(len(param_table_binary)) + " but expected size was " +\
                str(self.compute_file_size() - len(emevd_binary)) + ".")
        emevd_binary += param_table_binary
        
        return emevd_binary
    
        
