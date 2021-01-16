import lib.ast as ast

# -------------------------------------

INSTRS = {
        '+': ast.Incr(), 
        '-': ast.Decr(), 
        '>': ast.MoveIncr(), 
        '<': ast.MoveDecr(), 
        '.': ast.Output(), 
        ',': ast.Input()
    }

# -------------------------------------

def parse(c):
    result = []
    stack = [result]

    for x in c:
        if x in INSTRS.keys():
            stack[-1].append(INSTRS[x])
        elif x == '[':
            obj = ast.Loop()
            stack.append(obj)
        elif x == ']':
            if len(stack) >= 2:
                stack[-2].append(stack[-1])
                stack.pop()
    return result