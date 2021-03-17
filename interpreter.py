class Interpreter:
    def __init__(self, program, length=30000):
        self.length = length
        self.cells = [0 for i in range(length)]
        self.ptr = 0

        self.lptr = -1
        self.rptr = -1
    
    def incrementPtr(self):
        ptr += 1
        if ptr >= length: raise Exception("Out of cell bounds")
    
    def decrementPtr(self):
        ptr -= 1
        if ptr < 0: raise Exception("Out of cell bounds")
    
    def incrementCell(self):
        cells[ptr] += 1
    
    def decrementCell(self):
        cells[ptr] -= 1

    def inputCell(self):
        cells[ptr] = int(input())
    
    def outputCell(self):
        print(chr(cells[ptr]))
