import emevd_handler
import emevd_opener

import argparse

import sys
import contextlib

@contextlib.contextmanager
def _smart_open(filename=None, mode='w'):
    """Opens filename and returns a file handle. If filename is None 
     or '-', uses stdout.
    """
    
    if filename and filename != '-':
        fh = open(filename, mode)
    else:
        fh = sys.stdout

    try:
        yield fh
    finally:
        if fh is not sys.stdout:
            fh.close()

if __name__ == '__main__':
    desc = "Unpack and repack .emevd files. Can also write to / read from raw numeric data, which is more convenient to " +\
        "inspect and hand-edit than a binary file. Also can produce a pretty-printed verbose version, which is more easily human " +\
        "readable, but cannot be repacked. The typical usage pattern is to unpack an .emevd into both raw and verbose versions. " +\
        "Using the verbose version as a guide, edit the raw version to make suitable changes. Then, check the changes are correct by " +\
        "converting the raw version to a new verbose version. Finally, the raw version can then be re-packed as a .emevd file."
    parser = argparse.ArgumentParser(description=desc)
    
    
    parser.add_argument("in_file", metavar="FILE", action="store",
        help="File to read from.")
    parser.add_argument("-p", "--parse", action="store_true", dest="should_parse_from_file", 
        help="Read from a numeric file produced by -n rather than from a .emevd.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-n", "--numeric_print", action="store_true", dest="should_write_numeric",
        help="Emit the opened file as raw numeric data, suitable for hand editing.")
    group.add_argument("-v", "--verbose_print", action="store_true", dest="should_write_pretty",
        help="Emit the opened file as a pretty-printed version, suitable for easy inspection.")
    parser.add_argument("-o", "--output", metavar="OUTFILE", action="store", dest="out_file", default="-",
        help="Write output to OUTFILE instead of stdout. Use \"-\" for stdout if required.")
    parser.add_argument("-s", "--suppress", action="store_true", dest="suppress_line_numbers", default=False,
        help="Suppress line numbers when emitting a pretty-printed version, to allow for easier diffing.")
    
    args = parser.parse_args()
    
    mode = 'rb'
    if args.should_parse_from_file:
        mode = 'r'
    with open(args.in_file, mode) as f:
        emevd = emevd_handler.EmevdData([])
        
        if args.should_parse_from_file:
            emevd = emevd_handler.EmevdData.build_from_raw_numeric_file_content(f.read())
        else:
            emevd = emevd_handler.EmevdData.build_from_emevd_file_content(f.read())
        
        if args.should_write_numeric or args.should_write_pretty:
            with _smart_open(args.out_file, mode='w') as out:
                if args.should_write_numeric:
                    out.write(emevd.export_as_raw_numeric())
                else: # args.should_write_pretty
                    out.write(emevd.export_as_human_readable(suppress_line_numbers = args.suppress_line_numbers))
        else: # Write as binary .emevd
            with _smart_open(args.out_file, mode='wb') as out:
                out.write(emevd.export_as_emevd())
        
        

    
