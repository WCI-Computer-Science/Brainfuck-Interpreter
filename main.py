import sys
import argparse

from parser import parse
from interpreter import Interpreter

with open(sys.argv[1], "r") as f:
    program = parse(f)

argparser = argparse.ArgumentParser()
argparser.add_argument("--nowrap", "-nw", type=bool, default=False)
argparser.add_argument("--length", "-l", type=int, default=30000)
argparser.add_argument("--ptr", "-p", type=int, default=0)
argparser.add_argument("--flush", "-f", type=bool, default=False)
args, uknownargs = argparser.parse_known_args()

interpreter = Interpreter(not args.nowrap, args.ptr, args.length, args.flush)

i = 0
while i < len(program):
    if interpreter.parse(program[i]): i = program[i][1]
    i += 1
