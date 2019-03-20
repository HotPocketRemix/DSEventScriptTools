import json
import sys

TYPE_CHAR_DICT = {0: 'B', 1: 'H', 2: 'I', 3: 'b', 4: 'h', 5: 'i', 6: 'f', 8: 's'}

# Serializable object template.
# Override _fields to set types to parse. Format is a list of 2-tuples 
#  (name, type) where name is a string. type can be an actual type or class
#   or a list of types and classes.
# Override _verify_arg to provide post-parsing type assertion 
#  (for elements of list types, for instance).
class Structure(object):

    _fields = []

    def _init_arg(self, expected_type, value):
        if isinstance(expected_type, list):
            for type_in_list in expected_type:
                if isinstance(value, type_in_list):
                    return value
                else:
                    try:
                        return type_in_list(**value)
                    except TypeError:
                        continue
            raise TypeError("Cannot coerce " + str(value) + " to types [" +
             ", ".join([str(t) for t in expected_type]) + "]")
        else:
            if isinstance(value, expected_type):
                return value
            else:
                return expected_type(**value)
            
    def _verify_init(self):
        return

    def __init__(self, **kwargs):
        field_names, field_types = zip(*self._fields)
        assert [isinstance(name, str) for name in field_names]
        for type_ in field_types:
            if isinstance(type_, list):
                # Actually dealing with a list of types.
                assert [isinstance(t, type) for t in type_]
            else:
                assert isinstance(type_, type)

        for name, field_type in self._fields:
            setattr(self, name, self._init_arg(field_type, kwargs.pop(name)))
            
        self._verify_init()

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid arguments(s): {}'.format(','.join(kwargs)))
            
            
class Serializeable_EDF_Enum(Structure):
    _fields = [('name', str), ('values', dict)]
    
    def _verify_init(self):
        new_values = {}
        for (k, v) in self.values.items():
            new_values[int(k)] = self._init_arg(str, v)
        self.values = new_values
        
        assert all(isinstance(x, int) for x in self.values.keys())
        assert all(isinstance(x, str) for x in self.values.values())

    def to_pretty_string_list(self, format_string):
        return_list = []
        return_list.append("%s = {" % self.name)
        for (enum_key, enum_value) in self.values.items():
            return_list.append(" " + format_string % enum_key + ": " + enum_value)
        return_list.append("}")
        return return_list

class Serializeable_EDF_Argument(Structure):
    _fields = [('name', str), ('type', int), ('enum_name', [str, type(None)]), 
     ('default', [int, float, str]), ('min', [int, float, str]), ('max', [int, float, str]), 
     ('increment', [int, float, str]), ('format_string', str), 
     ('unk1', int), ('unk2', int), ('unk3', int), ('unk4', int)]
     
    def _verify_init(self):
        assert self.type in [0, 1, 2, 3, 4, 5, 6, 8]
        if self.type in [0, 1, 2, 3, 4, 5]:
            arg_type = int
        elif self.type in [6]:
            arg_type = float
        elif self.type in [8]:
            arg_type = str
        assert isinstance(self.default, arg_type), "Argument default is '" + str(self.default) + "' which is not of type " + str(arg_type)
        if self.type != 8: # String only uses default, the others are left as 0.
            assert isinstance(self.min, arg_type), "Argument min is '" + str(self.min) + "' which is not of type " + str(arg_type)
            assert isinstance(self.max, arg_type), "Argument max is '" + str(self.max) + "' which is not of type " + str(arg_type)
            assert isinstance(self.increment, arg_type), "Argument increment is '" + str(self.increment) + "' which is not of type " + str(arg_type)
                
    def to_pretty_string(self, suppress_unknown_arg_data):
        return_string = "%s " % TYPE_CHAR_DICT[self.type]
        if not suppress_unknown_arg_data:
            return_string += "[%02x|%02x|%02x|%02x] " % (self.unk1, 
             self.unk2, self.unk3, self.unk4)
        return_string += " %s" % self.name
        if self.enum_name != None:
            return_string += " [ENUM: %s]" % self.enum_name
        else:
            if self.type == 8:
                return_string += " ('" + self.format_string % self.default + "')"
            else:
                fs = self.format_string
                arg_format = " [" + fs + ":" + fs + ":" + fs + "] (" + fs + ")"
                return_string += arg_format % (self.min, self.increment, self.max, self.default)
        return return_string
        
class Serializeable_EDF_Instruction(Structure):
    _fields = [('name', str), ('index', int), ('args', list)]
    
    def _verify_init(self):
        self.args = [self._init_arg(Serializeable_EDF_Argument, x) for x in self.args]
        
    def to_pretty_string_list(self, suppress_unknown_arg_data):
        return_list = []
        return_list.append("[%02d] - %s" % (self.index, self.name))
        for arg in self.args:
            return_list.append("     " + arg.to_pretty_string(suppress_unknown_arg_data))
        return return_list
        
class Serializeable_EDF_Class(Structure):
    _fields = [('name', str), ('index', int), ('instrs', list)]
    
    def _verify_init(self):
        self.instrs = [self._init_arg(Serializeable_EDF_Instruction, x) for x in self.instrs]
        
    def to_pretty_string_list(self, suppress_unknown_arg_data):
        return_list = []
        return_list.append("%d - %s" % (self.index, self.name))
        for instr in self.instrs:
            return_list += [" " + l for l in instr.to_pretty_string_list(suppress_unknown_arg_data)]
        return return_list
        
class Serializeable_EDF_Struct(Structure):
    _fields = [('unknown', int), ('main_classes', list), ('extra_classes', list), ('enums', list)]
    
    def _verify_init(self):
        self.main_classes = [self._init_arg(Serializeable_EDF_Class, x) for x in self.main_classes]
        self.extra_classes = [self._init_arg(Serializeable_EDF_Class, x) for x in self.extra_classes]
        self.enums = [self._init_arg(Serializeable_EDF_Enum, x) for x in self.enums]
        
        # Check that all referenced Enums in every argument actually exist.
        enum_names = [enum.name for enum in self.enums]
        for c in self.main_classes + self.extra_classes:
            for i in c.instrs:
                for a in i.args:
                    if a.enum_name != None:
                        assert a.enum_name in enum_names, "Argument uses '" + str(a.enum_name) + "' but it is not included in the enum list."
    
    def to_pretty_string(self, suppress_unknown_arg_data = False):
        return_list = []
        return_list.append("EMEDF")
        return_list.append("")
        return_list.append("")
        return_list.append("Main Classes:")
        for c in self.main_classes:
            return_list += c.to_pretty_string_list(suppress_unknown_arg_data)
            return_list.append("")
        return_list.append("")
        return_list.append("Extra Classes:")
        for c in self.extra_classes:
            return_list += c.to_pretty_string_list(suppress_unknown_arg_data)
            return_list.append("")
        return_list.append("")
        return_list.append("Enums:")
        for e in self.enums:
            return_list += e.to_pretty_string_list("%d")
            return_list.append("")
        return "\n".join(return_list)
    
    # Build a dictionary of types for this EDF.
    # Returns type_dict, where type_dict[instr_class][instr_index] is
    #  a format string for the arguments of the command with class
    #  instr_class and index instr_index.
    def build_type_dict(self):
        type_dict = {}
        for c in self.main_classes:
            class_type_dict = {}
            for i in c.instrs:
                format_string = "@"
                for a in i.args:
                    format_string += TYPE_CHAR_DICT[a.type]
                class_type_dict[i.index] = format_string
            type_dict[c.index] = class_type_dict
        return type_dict
        
    # Build a dictionary of instruction strings for this EDF.
    # Returns instr_string_dict, where instr_string_dict[instr_class][instr_index] = (s, l)
    #  where s is the instruction format string for the command with class
    #  instr_class and index instr_index, and l is a list of the format
    #  strings for each of the command's arguments. Each element of l
    #  is either a true format string, or the name of an enum as a string.
    def build_instruction_string_dict(self):
        instr_string_dict = {}
        for c in self.main_classes:
            class_instr_string_dict = {}
            for i in c.instrs:
                arg_output_string_list = []
                arg_format_string_or_enum_list = []
                for (arg_count, a) in enumerate(i.args):
                    arg_output_string_list.append(a.name + ": {" + str(arg_count) + "}")
                    if a.enum_name != None:
                        arg_format_string_or_enum_list.append(a.enum_name)
                    else:
                        arg_format_string_or_enum_list.append(a.format_string)
                        
                class_instr_string_dict[i.index] = (i.name + " (" + 
                 ", ".join(arg_output_string_list) + ")", arg_format_string_or_enum_list)
            instr_string_dict[c.index] = class_instr_string_dict
        return instr_string_dict
        
    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)
        
    @classmethod
    def deserialize(cls, data):
        return cls(**json.loads(data))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: " + sys.argv[0] + " <JSON File>")
    else:
        with open(sys.argv[1], "rb") as f:
            content = f.read()
            print(Serializeable_EDF_Struct.deserialize(content).to_pretty_string(suppress_unknown_arg_data = True))
