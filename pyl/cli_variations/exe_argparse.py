#!/usr/bin/env python3

# Example of an executable Python
# script in Linux with a main() function and use of the
# (recommended) argparse builtin module.
# Best to read https://docs.python.org/3/howto/argparse.html
# Note: The use of a main() is not required.
# The filename is exe_arparse.py.
# Note: The filename "exe_argparse" is irrelevant. Can be foo.py.
#
# 1) Create the file exe_argparse.exe
# 2) Make executable: chmod +x exe_arparse.py (OR chmod 755 exe_argparse.py)
# 3) Add the shebang line at line 0 of file (see above)
# 4) Add the import statement (see below)
# 5) Add your source code, like below. Notice the 
#    lines with 'argparse' in them.
# 6) With the source below, try various invocations in terminal to
#    see argparse in action:
#    $ ./exe_argparse.py 
#    $ ./exe_argparse.py --help 
#    $ ./exe_argparse.py --h
#    $ ./exe_argparse.py blah 
#    $ ./exe_argparse.py --cats 7
#    $ ./exe_argparse.py --ca 4
#    $ ./exe_argparse.py --dogs 3
#    $ ./exe_argparse.py --dog 5
#    $ ./exe_argparse.py --dogs 2 --cats 1
#    $ ./exe_argparse.py --dgos 8        (intentional misspelling)

import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("--cats", type=int, help="number of cats you own")
parser.add_argument("--dogs", type=int, help="number of dogs you own")
args = parser.parse_args()

def main():

    print("Running")

    if args.cats:
        print(f"You own {args.cats} cats.")
    else:
        print("You own 0 cats.")

    if args.dogs:
        print(f"You own {args.dogs} dogs.")
    else:
        print("You own 0 dogs.")

    print("Ending")

if __name__ == '__main__':
    main()
