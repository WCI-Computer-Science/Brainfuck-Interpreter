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

def gettok(c, i):
    try: return langspec[c]
    except: raise Exception("Unidentified token at position " + str(i))

def parse(stream):
    program = []
    stack = deque()
    i = 0

    c = stream.read(1)
    while c:
        x = gettok(c, i)
        if x != 8:
            program.append((x,))
        else:
            try: program.append((x, stack.pop()))
            except: raise Exception("Need a matching \"[\" for \"]\" at position " + str(i))
        i += 1
        c = stream.read(1)
    
    return program