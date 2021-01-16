class Incr():
    def __repr__(self):
        return "Incr"
        
# -----------------------------------

class Decr():
    def __repr__(self):
        return "Decr"

# -----------------------------------

class MoveIncr():
    def __repr__(self):
        return "MoveIncr"

# -----------------------------------

class MoveDecr():
    def __repr__(self):
        return "MoveDecr"

# -----------------------------------

class Output():
    def __repr__(self):
        return "Output"

# -----------------------------------

class Input():
    def __repr__(self):
        return "Input"

# -----------------------------------

class Loop():
    def __init__(self, instr=None):
        self.instr = instr or []
        
    def __repr__(self):
        return f"Loop {self.instr}"

    def append(self, s):
        self.instr.append(s)