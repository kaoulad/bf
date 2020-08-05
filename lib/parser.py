import lib.evalbf as evalbf
from copy import deepcopy

INSTRS = {
        '+': evalbf.Incr(), 
        '-': evalbf.Decr(), 
        '>': evalbf.MoveIncr(), 
        '<': evalbf.MoveDecr(), 
        '.': evalbf.Output(), 
        ',': evalbf.Input()
    }

# -------------------------------------

def parse(c):
    ast = []
    stack = [ast]

    for x in c:
        if x in INSTRS.keys():
            stack[-1].append(INSTRS[x])
        elif x == '[':
            obj = deepcopy(evalbf.Loop())
            stack.append(obj)
        elif x == ']':
            if len(stack) >= 2:
                stack[-2].append(stack[-1])
                stack.pop()
        else:
            pass

    return ast