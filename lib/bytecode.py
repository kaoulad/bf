from abc import *
import sys

class BF:
  def __init__(self, input_=""):
    self.memory = [0] * 30000
    self.index = 0
    self.input = list(input_)

# ----------------------------------

class Instruction(ABC):
  @abstractmethod
  def eval(self, state):
    raise NotImplemented

# ----------------------------------

class Add(Instruction):
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"Add({self.n})"

    def eval(self, state):
        state.memory[state.index] += self.n

# ----------------------------------

class Remove(Instruction):
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"Remove({self.n})"
    
    def eval(self, state):
        state.memory[state.index] -= self.n

# ----------------------------------

class MoveRight(Instruction):
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"MoveRight({self.n})"

    def eval(self, state):
        state.index += self.n

# ----------------------------------

class MoveLeft(Instruction):
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"MoveLeft({self.n})"

    def eval(self, state):
        state.index -= self.n

# ----------------------------------

class Output(Instruction):
    def __repr__(self):
        return f"Output"

    def eval(self, state):
        sys.stdout.write(chr(state.memory[state.index]))

# ----------------------------------

class Input(Instruction):
    def __repr__(self):
        return f"Input"
    
    def eval(self, state):
        if state.input != []:
            state.memory[state.index] = ord(state.input.pop(0))

# ----------------------------------

class Clear(Instruction):
    def __repr__(self):
        return f"Clear"

    def eval(self, state):
        state.memory[state.index] = 0

# ----------------------------------

class Loop(Instruction):
    def __init__(self, inst):
        self.inst = inst

    def __repr__(self):
        return f"Loop {self.inst}"

    def eval(self, state):
        while state.memory[state.index] != 0:
            for inst in self.inst:
                inst.eval(state)

# ----------------------------------


    