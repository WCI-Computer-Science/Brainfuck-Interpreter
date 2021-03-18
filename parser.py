from collections import deque

# Brainfuck language specification, default is given
langspec = {
    ">": 1,
    "<": 2,
    "+": 3,
    "-": 4,
    ".": 5,
    ",": 6,
    "[": 7,
    "]": 8
}

def gettok(c):
    return langspec.get(c)

def parse(stream):
    program = []
    stack = deque()
    i = 0

    c = stream.read(1)
    while c:
        x = gettok(c)
        if not x:
            c = stream.read(1)
            continue

        if x < 7:
            program.append((x,))
        elif x == 7:
            stack.append(i)
            program.append(7)
        else:
            try:
                j = stack.pop()
                program[j] = (7, i)
                program.append((8, j))
            except: raise Exception("Need a matching \"[\" for \"]\" at position " + str(i))
        i += 1
        c = stream.read(1)
    
    return program