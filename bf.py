import parser
import evalbf

def execute(code, input_):
  instrs = parser.parse(code, [])
  state = evalbf.BF(input_)

  for instr in instrs:
    instr.eval(state)

try:
  content = open("hello.bf", 'r').read()
  execute(content, "mortim")
except FileNotFoundError:
  print("File not found.")