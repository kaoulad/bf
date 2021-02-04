from lib.parser import parse
from lib.bytecode import BF
from lib.optimization import optimize_ast,search_patterns

def execute(code, input_):
  state = BF(input_)
  optimized=search_patterns(optimize_ast(parse(code)))

  # Evaluate each Brainfuck instruction.
  for ins in optimized:
    ins.eval(state)
  
try:
  content = open("examples/mandelbrot.bf", 'r').read()
  execute(content, "")
except FileNotFoundError:
  print("File not found.")