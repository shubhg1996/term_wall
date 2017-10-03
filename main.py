#!/usr/bin/env python3

"""The main module that brings everything together."""
import os
import sys
import time

import scripter

def main(argv=sys.argv):
    """Entrance to the program."""
    if len(argv) == 1:
        print('No command line arguments specified.')
        return
    if os.path.exists("/home/shubh/Documents/term_wall/Data/"+argv[1]+".jpg"):
        fpath = "/home/shubh/Documents/term_wall/Data/"+argv[1]+".jpg"
    elif os.path.exists("/home/shubh/Documents/term_wall/Data/"+argv[1]+".png"):
        fpath = "/home/shubh/Documents/term_wall/Data/"+argv[1]+".png"
    else:
        print("no such background exists")
        fpath = "/home/shubh/Documents/term_wall/Data/black.jpg"
    scripter.change_terminal(fpath)

if __name__ == "__main__":
    # Entrance to the program.
    main(sys.argv)