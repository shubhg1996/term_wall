# Used for creating, running and analyzing applescript and bash scripts.

import os
import sys
import subprocess

from adapter import identify

def change_terminal(image_file_path):
    adapter = identify()
    if adapter is None:
        print("Terminal not supported")
    adapter.set_image_file_path(image_file_path)