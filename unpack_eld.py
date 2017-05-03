#!/usr/bin/env python

import struct
import sys

def extract_utf16z(content, offset):
    extracted = ''
    while content[offset:offset + 2] != '\x00\x00':
        extracted = extracted + content[offset:offset + 2]
        offset += 2
    return unicode(extracted, 'utf-16')

def consume_byte(content, offset, byte, length=1):
    for i in xrange(0, length-1):
        if content[offset + i] != byte:
            raise ValueError("Expected byte '" + byte.encode("hex") + "' at offset " +\
                    hex(offset + i) + " but received byte '" +\
                    content[offset + i].encode("hex") + "'.")
    return offset + length

if __name__ == '__main__': 
    if len(sys.argv) <= 1:
        print "Usage: " + sys.argv[0] + " <EMELD File>"
        sys.exit(1)

    filename = sys.argv[1]
    
    with open(filename, mode='rb') as file:
        file_content = file.read()
        
        master_offset = 0
        
        master_offset = consume_byte(file_content, master_offset, '\x45', 1)
        master_offset = consume_byte(file_content, master_offset, '\x4C', 1)
        master_offset = consume_byte(file_content, master_offset, '\x44', 1)
        master_offset = consume_byte(file_content, master_offset, '\x00', 1)
        
        master_offset = consume_byte(file_content, master_offset, '\x00', 4)
        
        master_offset = consume_byte(file_content, master_offset, '\x65', 1)
        master_offset = consume_byte(file_content, master_offset, '\x00', 1)
        master_offset = consume_byte(file_content, master_offset, '\xCC', 1)
        master_offset = consume_byte(file_content, master_offset, '\x00', 1)
        
        (file_size,) = struct.unpack_from("<I", file_content, offset=master_offset)
        master_offset += struct.calcsize("<I")
        
        (flag_count, flags_offset) = struct.unpack_from("<II", file_content, offset=master_offset)
        master_offset += struct.calcsize("<II")
        master_offset = consume_byte(file_content, master_offset, '\x00', 4)
        
        (strings_offset,) = struct.unpack_from("<I", file_content, offset=master_offset)
        master_offset += struct.calcsize("<I")
        
        # Skip a number of fields that always seem to be repeated or are not useful.
        
        master_offset = flags_offset
        for i in xrange(flag_count):
            (flag_number, string_offset) = struct.unpack_from("<II", file_content, offset=master_offset)
            master_offset += struct.calcsize("<II")
            master_offset = consume_byte(file_content, master_offset, '\x00', 4)
            
            value = extract_utf16z(file_content, strings_offset + string_offset)
            print (str(flag_number) + ": '" + value + "'").encode("utf-8")
