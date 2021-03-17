class Interpreter:
    def __init__(self, length=30000):
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
    
    def outputCell(self):
        print(chr(cells[ptr]))

    def inputCell(self):
        cells[ptr] = int(input())
    

    def parse(self, stmt):
        if stmt[0] == 1:
            incrementPtr()
        elif stmt[0] == 2:
            decrementPtr()
        elif stmt[0] == 3:
            incrementCell()
        elif stmt[0]  == 4:
            decrementCell()
        elif stmt[0] == 5:
            outputCell()
        elif stmt[0] == 6:
            inputCell()
        elif stmt[0] == 7:
            if cells[ptr]:
                incrementCell()
            else:
                ptr = stmt[1]+1
        else:
            if cells[ptr]:
                ptr = stmt[1]+1
            else:
                incrementCell()
