import parser
import evalbf

def execute(code, input_):
  instrs = parser.parse(code, [])
  state = evalbf.BF(input_)

  for instr in instrs:
    instr.eval(state)

  return "".join(state.output)

print(execute("++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.", ""))