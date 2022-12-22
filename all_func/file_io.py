import pyperclip


def read_file(filename: str, show_line_num: bool = False):
    """ read file with line number or without line number """
    with open(filename) as f:
        for idx, line in enumerate(f.read().splitlines()):
            if show_line_num:
                print(str(idx)+". "+line)
            else:
                print(line)


def copy_file(filename: str, line_num:int = -1):
    with open(filename) as f:
        if line_num != -1: 
            txt = f.readlines()
            pyperclip.copy(txt[line_num])
            print("[+] "+str(line_num)+" number line copied.")
        else:
            txt = f.read()
            pyperclip.copy(txt)
            print("[+] Copied.")
