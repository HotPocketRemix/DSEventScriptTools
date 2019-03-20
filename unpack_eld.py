import struct
import sys
import re
import argparse
import contextlib

import dcx_handler
from emevd_handler import EVD_FileType

def extract_utf16z(content, offset):
    extracted = b''
    length = 0
    while content[offset + length:offset + length+ 2] != b'\x00\x00':
        extracted = extracted + content[offset + length:offset + length + 2]
        length += 2
    return (extracted.decode('utf-16'), length + 2)

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
    
# Wrapper for struct.unpack_from to make calculating offsets easier.
#  Returns (result, new_offset) where result is the output of struct.unpack_from.
def extract_struct(format_string, content, offset=0):
    result = struct.unpack_from(format_string, content, offset=offset)
    return (result, offset + struct.calcsize(format_string))
    
def string_list_to_binary_emeld(string_list, filetype, should_dcx):
    header = b'\x45\x4C\x44\x00'
    if filetype == EVD_FileType.DARK_SOULS_1:
        header += struct.pack("<II", 0x00000000, 0x00CC0065)
        header_size = 0x38
        header_pair_format_string = "<II"
    else:
        header += struct.pack("<II", 0x0000FF00, 0x00CC0065)
        header_size = 0x50
        header_pair_format_string = "<QQ"
    
    packed_data = b''
    packed_strings = b''
    current_string_offset = 0
    for (event_id, value) in string_list:
        if filetype == EVD_FileType.DARK_SOULS_1:
            packed_data += struct.pack("<III", event_id, current_string_offset, 0)
        else:
            packed_data += struct.pack("<QQ", event_id, current_string_offset)
        string_to_pack = value.encode("utf-16le") + b'\x00\x00'
        packed_strings += string_to_pack
        current_string_offset += len(string_to_pack)
    
    # Pad file to multiple of 8 bytes to match existing files.
    current_file_size = header_size + len(packed_data) + len(packed_strings)
    if current_file_size % 8 != 0:
        packed_strings += b'\x00' * (8 - current_file_size % 8)
        current_file_size +=  (8 - current_file_size % 8)
    
    strings_offset = header_size + len(packed_data)
    
    header += struct.pack("<I", current_file_size)
    header += struct.pack(header_pair_format_string, len(string_list), header_size)
    header += struct.pack(header_pair_format_string, 0, strings_offset)
    header += struct.pack(header_pair_format_string, 0, strings_offset)
    header += struct.pack(header_pair_format_string, len(packed_strings), strings_offset)
    if filetype == EVD_FileType.DARK_SOULS_1:
        header += struct.pack(header_pair_format_string, 0, 0)
    
    binary_emeld = header + packed_data + packed_strings
    
    if should_dcx:
        if filetype == EVD_FileType.DARK_SOULS_1:
            return dcx_handler.compress_dcx_content(binary_emeld, False)
        else:
            return dcx_handler.compress_dcx_content(binary_emeld, True)
    else:
        return binary_emeld
    
def emeld_file_content_to_string_list(file_content):
    should_dcx = False
    if dcx_handler.appears_dcx(file_content):
        tmp = dcx_handler.uncompress_dcx_content(file_content)
        should_dcx = True
        file_content = tmp
    master_offset = 0
    
    master_offset = consume_byte(file_content, master_offset, b'\x45', 1)
    master_offset = consume_byte(file_content, master_offset, b'\x4C', 1)
    master_offset = consume_byte(file_content, master_offset, b'\x44', 1)
    master_offset = consume_byte(file_content, master_offset, b'\x00', 1)
    
    ((version_part_1, version_part_2), master_offset) = extract_struct("<II", file_content, master_offset)
    
    if version_part_1 == 0x00000000 and version_part_2 == 0x00CC0065:
        filetype = EVD_FileType.DARK_SOULS_1
    elif version_part_1 == 0x0000FF00 and version_part_2 == 0x00CC0065:
        filetype = EVD_FileType.BLOODBORNE
    else:
        raise ValueError(("Unrecognized version bytes %08x %08x." + 
         "Could not determine ELD version.") % (version_part_1, version_part_2))
    
    ((file_size,), master_offset) = extract_struct("<I", file_content, master_offset)
    
    if filetype == EVD_FileType.DARK_SOULS_1:
        ((event_count, event_offset), master_offset) = extract_struct("<II", file_content, master_offset)
        ((_, _), master_offset) = extract_struct("<II", file_content, master_offset) # 0, strings_offset
        ((_, _), master_offset) = extract_struct("<II", file_content, master_offset) # 0, strings_offset
        ((strings_length, strings_offset), master_offset) = extract_struct("<II", file_content, master_offset)
        ((_, _), master_offset) = extract_struct("<II", file_content, master_offset) # 0, 0
    else:
        ((event_count, event_offset), master_offset) = extract_struct("<QQ", file_content, master_offset)
        ((_, _), master_offset) = extract_struct("<QQ", file_content, master_offset) # 0, strings_offset
        ((_, _), master_offset) = extract_struct("<QQ", file_content, master_offset) # 0, strings_offset
        ((strings_length, strings_offset), master_offset) = extract_struct("<QQ", file_content, master_offset)
    
    master_offset = event_offset
    return_list = []
    for i in range(event_count):
        if filetype == EVD_FileType.DARK_SOULS_1:
            ((event_id, string_offset, _), master_offset) = extract_struct("<III", file_content, master_offset)
        else:
            ((event_id, string_offset), master_offset) = extract_struct("<QQ", file_content, master_offset)
        (value, _) = extract_utf16z(file_content, strings_offset + string_offset)
        return_list.append((event_id, value))   
    return (return_list, filetype, should_dcx)
    
def string_list_to_human_readable(string_list, filetype, should_dcx):
    dcx_string = "UNDCX"
    if should_dcx:
        dcx_string = "DCX"
        
    return_string = EVD_FileType.to_string(filetype) + ":" + dcx_string + "\n\n"
    for (event_id, value) in string_list:
        return_string += "%d:%s\n" % (event_id, value)
    return return_string
    
def human_readable_to_string_list(file_content):
    filetype = None
    should_dcx = False
    string_list = []
    
    lines = file_content.splitlines()
    for (line_num, line) in enumerate(lines):
        if not line:
            continue
        if filetype == None:
            split_line = line.split(":")
            filetype = EVD_FileType.from_string(split_line[0])
            if filetype == None:
                raise ValueError("Line %d: Could not find acceptable ELD filetype signifier.")
            if len(split_line) > 1 and split_line[1] == "DCX":
                should_dcx = True
        else:
            m_string_entry = re.match(r"^(\d+):(.*)", line)
            if m_string_entry:
                event_id = int(m_string_entry.group(1))
                value = m_string_entry.group(2)
                string_list.append((event_id, value))
            else:
                raise ValueError("Line %d: Could not parse as event_id:readable_name pair.")
    return (string_list, filetype, should_dcx)


@contextlib.contextmanager
def _smart_open(filename=None, mode='w', encoding=None):
    """Opens filename and returns a file handle. If filename is None 
     or '-', uses stdout.
    """
    
    if filename and filename != '-':
        fh = open(filename, mode, encoding=encoding)
    else:
        if 'b' in mode:
            fh = sys.stdout.buffer
        else:
            fh = sys.stdout

    try:
        yield fh
    finally:
        if fh is not sys.stdout and fh is not sys.stdout.buffer:
            fh.close()

if __name__ == '__main__':
    desc = "Unpack and repack .emeld files."
    epilog = "Developed by HotPocketRemix."
    parser = argparse.ArgumentParser(description=desc, epilog=epilog)
    
    
    parser.add_argument("in_file", metavar="FILE", action="store",
        help="File to read from.")
    parser.add_argument("-p", "--parse", action="store_true", dest="should_parse_from_file", 
        help="Read from a human-readable file produced by -n rather than from a .emeld.")
    parser.add_argument("-v", "--verbose-print", action="store_true", dest="should_write_pretty",
        help="Emit the opened file as a human-readable version, suitable for easy inspection, rather than a .emeld.")
    parser.add_argument("-o", "--output", metavar="OUTFILE", action="store", dest="out_file", default="-",
        help="Write output to OUTFILE instead of stdout. Use \"-\" for stdout if required.")
            
    args = parser.parse_args()
    
    mode = 'rb'
    enc = None
    if args.should_parse_from_file:
        mode = 'r'
        enc = "utf-8"
    with open(args.in_file, mode, encoding=enc) as f:            
        if args.should_parse_from_file:
            (string_list, filetype, should_dcx) = human_readable_to_string_list(f.read())
        else:
            (string_list, filetype, should_dcx) = emeld_file_content_to_string_list(f.read())
        
        if args.should_write_pretty:
            with _smart_open(args.out_file, mode='w', encoding="utf-8") as out:
                out.write(string_list_to_human_readable(string_list, filetype, should_dcx))
        else: # Write as binary .emeld
            with _smart_open(args.out_file, mode='wb') as out:
                out.write(string_list_to_binary_emeld(string_list, filetype, should_dcx))
        
        

    

        
        
