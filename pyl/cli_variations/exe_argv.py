#!/usr/bin/env python3

# Example of an executable Python
# script in Linux with a main() function and argument use.
# Note: You should really use argparse, rather than argv.
# See the exe_argparse.py example.
# Note: The use of a main() is not required.
# The filename is exe_argv.py.
# Note: The filename "exe_argv" is irrelevant. Can be foo.py.
#
# 1) Create the file exe_argv.exe
# 2) Make executable: chmod +x exe_arvg.py (OR chmod 755 exe_argv.py)
# 3) Add the shebang line at line 0 of file (see above)
# 4) Add the import statement (see below)
# 5) Add your source code, like below. Notice the 
#    lines with 'argv' in them.
# 6) Invocation in terminal: $ ./exe_argv.py hello world

import sys

def main():
    print("Running " + sys.argv[0])
    print("Arguments: " + str(sys.argv[1:]))
    print("Ending")

if __name__ == '__main__':
    main()
