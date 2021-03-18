import sys

from parser import parse
from interpreter import Interpreter

with open(sys.argv[1], "r") as f:
    program = parse(f)

try: interpreter = Interpreter(length=int(sys.argv[2]))
except: interpreter = Interpreter()

i = 0
while i < len(program):
    if interpreter.parse(program[i]): i = program[i][1]
    i += 1
