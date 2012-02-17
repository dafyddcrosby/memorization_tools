#!/usr/bin/env python
"""
Simple program to help you associate mnemonics for numbers 00-99

Copyright (c) 2012, Dafydd Crosby
http://dafyddcrosby.com
"""

import random
import sys

try:
    mnem_file = open(sys.argv[1])
except:
    print("Cannot open mnemonic list file")
    sys.exit(1)

mnem_list = []
for line in mnem_file:
    if line.strip() != "":
        mnem_list.append(line.strip())

while True:
    which = random.randint(0, len(mnem_list)-1)
    answer = raw_input(mnem_list[which]+"\n").strip()
    try:
        answer = int(answer)
    except:
        print("Please input integers only")
        continue
        
    if int(answer) == int(which):
        print("Correct!")
    else:
        print("Nope. %s is %i" % (mnem_list[which], which))
