import sys

class Interpreter:
    def __init__(self, wrap, ptr, length, flush):
        self.wrap = wrap
        self.length = length
        self.cells = [0 for i in range(length)]
        self.ptr = ptr

        self.flush = flush
    
    def check(self):
        if self.ptr < 0 or self.ptr >= self.length: raise Exception("Out of cell bounds at position " + str(self.ptr))
    
    def overflow(self):
        self.cells[self.ptr] = (self.cells[self.ptr]+256)%256
    
    def parse(self, stmt):
        self.check()
        if stmt[0] == 1:
            self.ptr += 1
            if self.wrap: self.overflow()
        elif stmt[0] == 2:
            self.ptr -= 1
            if self.wrap: self.overflow()
        elif stmt[0] == 3:
            self.cells[self.ptr] += 1
        elif stmt[0]  == 4:
            self.cells[self.ptr] -= 1
        elif stmt[0] == 5:
            print(chr(self.cells[self.ptr]), end="", flush=self.flush)
        elif stmt[0] == 6:
            self.cells[self.ptr] = int(sys.stdin.read(1))
            if self.wrap: self.overflow()
        elif stmt[0] == 7:
            if not self.cells[self.ptr]: return True
        else:
            if self.cells[self.ptr]: return True
