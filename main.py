from importFile import readfile
from roundRobin import startRoundRobin

processos = readfile()

Quantum = 4

startRoundRobin(processos, Quantum)