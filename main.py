import sys

from parser import parse
from interpreter import Interpreter

with open(sys.argv[1], "r") as f:
    program = parse(f)
length = int(sys.argv[2])

interpreter = Interpreter(length)
for c in program:
    interpreter.parse(c)
