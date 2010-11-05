#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
Instruction memory
"""

from myhdl import Signal, delay, always_comb, now, Simulation, \
                  intbv, bin, instance, instances, toVHDL, toVerilog


def load_program(ROM, program='prog.txt', comment_char='#' ):
    index = 0
    for line in open(program):
        line = line.partition(comment_char)[0]
        line = line.rstrip()
        if len(line) == 32:
            ROM[index] = int(line, 2)
            index += 1 

    return tuple(ROM)

ROM = load_program([0] * 32)

def instruction_memory(address, instruction):
    """ 
    address -- the pointer defined by PC 
    instruction -- 32 bit encoded instruction
    """
    
    @always_comb
    def logic():
            instruction.next = ROM[int(address)]
    return logic




def testBench():

    I = Signal(intbv(0, min=0, max=16))
    O = Signal(intbv(0)[32:])
    

    #pd_instance = prime_detector(E, S)
    im_instance = toVHDL(instruction_memory, I, O)

    @instance
    def stimulus():
        for i in range(8):
            I.next = intbv(i)
            yield delay(10)
            print "address: " + bin(I, 4) + " (" + str(I) + ") | instruction: " + bin(O, 32)

    return instances()



def main():
    sim = Simulation(testBench())
    sim.run()


if __name__ == '__main__':
    main()