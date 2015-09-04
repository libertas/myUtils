#! /usr/bin/env python3

import os.path
import time

if __name__ == "__main__":
    src = "a.c"
    des = "b.c"
    lastTime = time.ctime(os.path.getmtime(src))
    while True:
        try:
            thisTime = time.ctime(os.path.getmtime(src))
        except FileNotFoundError:
            continue
        if thisTime != lastTime:
            fsrc = open(src, "rb")
            fdes = open(des, "wb")
            fdes.write(fsrc.read())
            fsrc.close()
            fdes.close()

