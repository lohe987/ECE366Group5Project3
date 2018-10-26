from sys import argv
from Simulator import Simulator
from assembler import assemble

binary_file = assemble(argv[1]) # assemble the program
simulation = Simulator(binary_file)
simulation.Run()