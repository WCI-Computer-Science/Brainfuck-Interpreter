class Interpreter:
    def __init__(self, length=30000):
        self.length = length
        self.cells = [0 for i in range(length)]
        self.ptr = 0

        self.lptr = -1
        self.rptr = -1
    
    def check(self):
        if self.ptr < 0 or self.ptr >= self.length: raise Exception("Out of cell bounds at position " + str(self.ptr))
    
    def parse(self, stmt):
        self.check()
        #print(self.cells[:20])
        if stmt[0] == 1:
            self.ptr += 1
        elif stmt[0] == 2:
            self.ptr -= 1
        elif stmt[0] == 3:
            self.cells[self.ptr] += 1
        elif stmt[0]  == 4:
            self.cells[self.ptr] -= 1
        elif stmt[0] == 5:
            print(chr(self.cells[self.ptr]), end="")
        elif stmt[0] == 6:
            self.cells[self.ptr] = int(input())
        elif stmt[0] == 7:
            if not self.cells[self.ptr]: return True
        else:
            if self.cells[self.ptr]: return True
