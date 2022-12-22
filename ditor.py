#!/usr/bin/python3

import sys
from all_func import read_file, copy_file, file_exist

def main():
    """ main function """
    argv = sys.argv

    if len(argv) > 1:
        filename = file_exist(filename=argv[1])

    # command check
    i = 2
    while i < len(argv):
        if argv[i] == "-r":
            read_file(filename=filename, show_line_num=False)
        elif argv[i] == "-rl":
            read_file(filename=filename, show_line_num=True)
        elif argv[i] == "-c":
            copy_file(filename=filename)
        elif argv[i][0:4] == "-cl=":
            copy_file(filename=filename, line_num=int(argv[i].split("=")[1]))
        else:
            print("[-] No command found.")
        print("")

        i += 1





if __name__ == "__main__":
    main()


