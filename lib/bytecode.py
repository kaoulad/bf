from sys import stdout

class BF:
  def __init__(self, input_=""):
    self.memory = [0] * 30000
    self.index = 0
    self.input = list(input_)

# ----------------------------------

class Add():
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"Add({self.n})"

    def eval(self, state):
        if state.memory[state.index]+self.n <= 255:
            state.memory[state.index] += self.n
        else:
            state.memory[state.index] = (state.memory[state.index]+self.n)%256

# ----------------------------------

class Remove():
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"Remove({self.n})"
    
    def eval(self, state):
        if self.n <= state.memory[state.index]:
            state.memory[state.index] -= self.n
        else:
            state.memory[state.index] = (state.memory[state.index]-self.n)%256

# ----------------------------------

class Move():
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"Move({self.n})"

    def eval(self, state):
        if state.index+self.n <= len(state.memory)-1:
            state.index += self.n
        else:
            state.index = (state.index+self.n)%len(state.memory)

# ----------------------------------

class Output():
    def __repr__(self):
        return "Output"

    def eval(self, state):
        stdout.write(chr(state.memory[state.index]))

# ----------------------------------

class Input():
    def __repr__(self):
        return "Input"
    
    def eval(self, state):
        if state.input != []:
            state.memory[state.index] = ord(state.input.pop(0))

# ----------------------------------

class Loop():
    def __init__(self, inst):
        self.inst = inst

    def __repr__(self):
        return f"Loop {self.inst}"

    def eval(self, state):
        while state.memory[state.index] != 0:
            for inst in self.inst:
                inst.eval(state)

# ----------------------------------

class Clear():
    def __repr__(self):
        return "Clear"

    def eval(self, state):
        state.memory[state.index] = 0

# ----------------------------------

class MoveUntilZero():
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"MoveUntilZero({self.n})"

    def eval(self, state):
        while state.memory[state.index] != 0:
            state.index += self.n

# ----------------------------------

class Mult():
    def __init__(self,i,factor):
        self.i = i
        self.factor = factor

    def __repr__(self):
        return f"Mult(i={self.i},factor={self.factor})"

    def eval(self, state):
        state.memory[state.index+self.i] += self.factor*state.memory[state.index]
        state.memory[state.index] = 0