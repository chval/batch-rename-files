#!/usr/bin/env python3

import argparse
import os
import sys
import re
from glob import glob

intro = """
***********************************************
In a directory rename files that match pattern
***********************************************
"""


def run():
    parser = argparse.ArgumentParser(description=intro, formatter_class=argparse.RawTextHelpFormatter, add_help=False)
    parser.add_argument('-h', '--help', action='help', help='Show this help message and exit')
    parser.add_argument('-d', '--dir', type=str, help='Directory where to search files', required=True)
    parser.add_argument('-m', '--match', type=str, help='Filename regular expression match pattern')
    parser.add_argument('-r', '--rename', type=str, help='Renamed filename (can include matched groups {0},{1}, ...)')
    parser.add_argument('-a', '--approve', action='store_true',
                        help="Approve file rename (by default script doesn't do any file operations)")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    if not os.path.isdir(args.dir):
        raise ValueError("Please specify a valid directory")

    cre = re.compile(args.match) if args.match else None
    matched_count = 0

    for glob_file in glob(os.path.normpath(args.dir) + "/*"):
        if not os.path.isfile(glob_file):
            continue

        (path, filename) = glob_file.rsplit('/', 1)
        ms = re.search(cre, filename) if cre else None

        if cre and not ms:
            continue

        matched_count += 1

        if not args.rename or ms is None:
            print(filename)
            continue

        new_filename = args.rename.format(*ms.groups())
        print(filename, ' -> ', new_filename)

        if not args.approve:
            continue

        rename_from = '/'.join((path, filename))
        rename_dest = '/'.join((path, new_filename))

        try:
            os.rename(rename_from, rename_dest)
        except OSError:
            print(f"Something went wrong while rename {filename} -> {new_filename}")
            break

    if not matched_count:
        print("Nothing found at: " + args.dir)


if __name__ == '__main__':
    run()
