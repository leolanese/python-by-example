# You can use Python's built-in "dis"
# module to disassemble functions and
# inspect their CPython VM bytecode:

def greet(name):
  return 'Hello, ' + name + '!'

greet('Dan') # 'Hello, Dan!'

import dis
dis.dis(greet)
