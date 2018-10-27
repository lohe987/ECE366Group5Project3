from sys import argv
from Simulator import Simulator
from assembler import assemble

simulation = Simulator(argv[1])
simulation.Run()