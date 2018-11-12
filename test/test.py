#!/usr/bin/env python3

import os, argparse, sys
from os import *
from stat import *
import difflib

# str1 = 'abcdefg'
# str1 = 'abc12def34g56'
#

stt = os.lstat('dir2/file1')
print(stt.st_mode)

print(os.access('dir2/file1', os.R_OK))
