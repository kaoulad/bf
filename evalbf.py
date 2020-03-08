from abc import *
import sys

sys.setrecursionlimit(10000)

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

# -----------------------------------

class Incr(Instruction):

    def __repr__(self):
        return "Incr"

    def eval(self, state):
        state.memory[state.index] += 1

# -----------------------------------

class Decr(Instruction):

    def __repr__(self):
        return "Decr"

    def eval(self, state):
        state.memory[state.index] -= 1

# -----------------------------------

class MoveIncr(Instruction):

    def __repr__(self):
        return "MoveIncr"

    def eval(self, state):
        state.index += 1

# -----------------------------------

class MoveDecr(Instruction):

    def __repr__(self):
        return "MoveDecr"

    def eval(self, state):
        state.index -= 1

# -----------------------------------

class Output(Instruction):

    def __repr__(self):
        return "Output"

    def eval(self, state):
        print(chr(state.memory[state.index]), end='')

# -----------------------------------

class Input(Instruction):

    def __repr__(self):
        return "Input"

    def eval(self, state): 
        if state.input != []:
            state.memory[state.index] = ord(state.input.pop(0))

# -----------------------------------

class Loop(Instruction):

    def __init__(self, instr):
        self.instr = instr

    def __repr__(self):
        return f"Loop {self.instr}"

    def eval(self, state):
        while state.memory[state.index] != 0:
            for inst in self.instr:
                inst.eval(state)