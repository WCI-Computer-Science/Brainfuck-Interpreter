# Brainfuck-Interpreter

An interpreter for Brainfuck written in Python.
The first pass parses the Brainfuck code and converts it to a sequence of tokens with some metadata,
which can be seen as a sort of abstract syntax sequence, since Brainfuck is so simple.
Then, the interpreter processes this sequence and produces a result.

```Bash
Usage: python3 main.py program.txt [-nw no_wrap] [-l length] [-p ptr_start] [-f flush]
```
`program.txt` should store the Brainfuck code.  
`no_wrap` should be any value to indicate that the cells should not overflow. This defaults to False (meaning overflow *will* occur).  
`length` should specify the length of the memory cell array. This defaults to 30000.  
`ptr_start` should specify the starting position of the pointer. This defaults to the position 0.  
`flush` should be any value to indicate that Python should flush the buffer each time it prints (not recommended). This defaults to False.
