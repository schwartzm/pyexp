#!/usr/bin/env python3

# Example of an executable Python
# script in Linux with a main() function.
# The filename is exe_main.py.
# Note: The filename "exe_main" is irrelevant. Can be foo.py.
#
# 1) Create the file exe_main.exe
# 2) Make executable: chmod +x exe_main.py (OR chmod 755 exe_main.py)
# 3) Add the shebang line at line 0 of file (see above)
# 4) Add your source code, like below. Notice the 
#    lines with 'main' in them.
# 5) Invocation in terminal: $ ./exe_main.py

def main():
    print("Running")
    print("Ending")

if __name__ == '__main__':
    main()
