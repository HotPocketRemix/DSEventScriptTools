import emevd_opener

def stringify_args(format_string_or_enum_list, arg_list, enum_list):
    """Applies stringify_arg to each element of arg_list, using the
    respective format or enum string in format_string_or_enum_list.
    """
    
    return [stringify_arg(format_string_or_enum, arg, enum_list) for 
     (format_string_or_enum, arg) in zip(format_string_or_enum_list, arg_list)]

def stringify_arg(format_string_or_enum, arg, enum_list):
    """Formats arg in accordance with format_string_or_enum. If it is 
    a format string, arg must be of the correct type. Otherwise, if it
    is an enum, then arg is treated as an index into this enum.
    """
    
    enum_names = [e.name for e in enum_list]
    if format_string_or_enum in enum_names:
        return parse_enum(arg, format_string_or_enum, enum_list)
    else:
        if isinstance(arg, str):
            return arg
        else:
            return format_string_or_enum % arg  

def parse_enum(value, enum_name, enum_list):
    """Indexes the enum enum_name using value. If value is not found in
    enum, then a dummy string representation of enum_name[value] is 
    used instead.
    """
    
    for enum in enum_list:
        if enum.name == enum_name:
            if value not in enum.values:
                return enum.name + "[" + str(value) + "]"
            else:
                return enum.values[value]
        
def default_readable(instr_class, instr_index, fixed_args, var_args):
    """Creates a default readable representation of the command with
    command instr_class and instr_index with arguments fixed_args and var_args.
    Provides no information about the command's purpose.
    """
    
    arg_array_string = ''
    if not var_args:
        arg_array_string = "(" + ", ".join([str(s) for s in fixed_args]) + ")"
    else:
        arg_array_string = "(" + ", ".join([str(s) for s in fixed_args]) + " | " + ", ".join([str(s) for s in var_args]) + ")"
    
    return ("%4d" % instr_class + "[" + "%2d" % instr_index + "] " + arg_array_string)

def translate(instr_class, instr_index, fix_args, var_args, filetype):
    """Creates a human-readable representation of the command with
    command instr_class and instr_index with arguments fixed_args and var_args.
    If the command is known, the human-readable representation is
    a string that desribes its function. If not, a default representation
    using default_readable is used as a fallback.
    """
    
    # The var_args handling is not great and should be reworked.
    # Instead, the instructions full format string should be parsed, but
    #  this is annoying because it does not have the same verbose information
    #  as the one from the .emedf.
    
    var_arg_string = ""
    if var_args:
        var_arg_string = "{, " + ", ".join([str(s) for s in var_args]) + "}"
    instr_string_dict = emevd_opener.get_instr_string_dict(filetype)
    enum_list = emevd_opener.get_enum_list(filetype)
    if (instr_class not in instr_string_dict or instr_index not in instr_string_dict[instr_class]):
        return default_readable(instr_class, instr_index, fix_args, var_args)
    else:
        (output_string, arg_format_string_or_enum_list) = instr_string_dict[instr_class][instr_index]
        return output_string.format(*stringify_args(arg_format_string_or_enum_list, fix_args, enum_list)) + var_arg_string

