import lib.ast as ast
import lib.bytecode as bytecode

# --------------------------------------------------------------------------------
# ------------------------ Optimize AST  -----------------------------------------
# --------------------------------------------------------------------------------

def set_move(inst,n=0):
  return n+1 if not isinstance(inst,ast.MoveDecr) else n-1

# -------------------------------------

def set_bytecode(inst):
  if isinstance(inst, ast.Incr):
    return bytecode.Add
    
  elif isinstance(inst, ast.Decr):
    return bytecode.Remove

  elif isinstance(inst, ast.MoveIncr) or isinstance(inst, ast.MoveDecr):
    return bytecode.Move

  elif isinstance(inst, ast.Output):
    return bytecode.Output

  elif isinstance(inst, ast.Input):
    return bytecode.Input

  else:
    return bytecode.Loop

# -------------------------------------------------------

def optimize_ast(parsed):
    optimized_ast=[]

    for i,instr in enumerate(parsed):
        opti_instr = set_bytecode(instr)

        # ----- Optimize Loop instruction -----------------------------
        if isinstance(instr,ast.Loop):
          optimized_ast.append(opti_instr(optimize_ast(instr.instr)))

        # ------ Optimize Output or Input instruction (without parameter) ----
        elif isinstance(instr,ast.Output) or isinstance(instr, ast.Input):
          optimized_ast.append(opti_instr())

        # ---- First instruction ----------------
        elif i == 0:
          optimized_ast.append(opti_instr(set_move(instr)))

        # ---- Grouping consecutive instructions (RLE) ----
        elif isinstance(optimized_ast[-1:][0],opti_instr):
          last = optimized_ast.pop()
          optimized_ast.append(opti_instr(set_move(instr, last.n)))
          
        # --------------
        else:
          optimized_ast.append(opti_instr(set_move(instr)))

    return optimized_ast

# --------------------------------------------------------------------------------
# ------------------------ Searching patterns  -----------------------------------
# --------------------------------------------------------------------------------

def pattern(inst):
  # The pattern is a Loop
  if isinstance(inst, bytecode.Loop):
    # Number of instructions in Loop = 1
    if len(inst.inst) == 1:
      # [-] Pattern
      if isinstance(inst.inst[0], bytecode.Remove):
        return bytecode.Clear()
      # [>],[<] Pattern
      if isinstance(inst.inst[0], bytecode.Move):
        return bytecode.MoveUntilZero(inst.inst[0].n)
      # -----------------
      return None
    # Number of instructions in Loop = 4
    elif len(inst.inst) == 4:
      # [->>>+<<<] Pattern
      if (isinstance(inst.inst[0], bytecode.Remove) and inst.inst[0].n == 1) and isinstance(inst.inst[1], bytecode.Move) and isinstance(inst.inst[2], bytecode.Add) and isinstance(inst.inst[3], bytecode.Move) and (inst.inst[3].n < 0) and inst.inst[1].n == abs(inst.inst[3].n):
        return bytecode.Mult(inst.inst[1].n, inst.inst[2].n)
      else:
        return None
    else:
      return None
  else:
    return None
  

# ----------------------------------------------

def setpattern(inst):
  p = pattern(inst)
  return p if p else ( bytecode.Loop(search_patterns(inst.inst)) if isinstance(inst, bytecode.Loop) else inst  )

def search_patterns(optimized):
  return list(map(setpattern, optimized))

    