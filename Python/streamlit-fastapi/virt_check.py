# type: ignore
# pylint: skip-file
import sys

def check():
    return sys.prefix == sys.base_prefix

if __name__ == "__main__":
    flag = check()
    if flag == True:
        print("venv is inactive")
    elif flag == False:
        print("venv is active")