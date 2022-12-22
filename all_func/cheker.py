import os

def file_exist(filename: str):
    """ file exist or break the program """
    if not os.path.isfile(filename):
        print("[*] file not exist.")
        exit()
    else:
        return filename
