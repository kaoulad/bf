import lib.ast as ast
import lib.bytecode as bytecode

# ---------------------------------------------------

BYTECODES = {
  "Incr":bytecode.Add,
  "Decr":bytecode.Remove,
  "MoveIncr":bytecode.MoveRight,
  "MoveDecr":bytecode.MoveLeft,
  "Output":bytecode.Output,
  "Input":bytecode.Input,
}

# ---------------------------------------------------

def get_bytecode_instr(instr):
  return BYTECODES[instr] if instr in BYTECODES.keys() else bytecode.Loop

# ---------------------------------------------------

def optimize_ast(parsed):
    optimised_ast=[]
  
    for i,instr in enumerate(parsed):
        opti_instr = get_bytecode_instr(repr(instr))
        # --------------------------------------
        if isinstance(instr,ast.Loop):
          if repr(instr) == "Loop [Decr]": # Check [-] pattern to optimize it
            optimised_ast.append(bytecode.Clear())
          else:
            optimised_ast.append(opti_instr(optimize_ast(instr.instr)))

        # --------------------------------------
        elif isinstance(instr,ast.Output) or isinstance(instr, ast.Input):
          optimised_ast.append(opti_instr())

        # --------------------------------------
        elif i == 0:
          optimised_ast.append(opti_instr(1))

        # --------------------------------------
        else:
            if isinstance(optimised_ast[-1:][0],opti_instr):
                last = optimised_ast.pop()
                optimised_ast.append(opti_instr(last.n+1))
            # -------------------
            else:
                optimised_ast.append(opti_instr(1))
        # --------------------------------------
    return optimised_ast