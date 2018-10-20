from sys import argv
from Simulator import Simulator

simulation = Simulator(argv[1])
simulation.Run()