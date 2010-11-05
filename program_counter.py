#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
Program counter
"""


from myhdl import Signal, delay, always_comb, always, Simulation, \
                  intbv, bin, instance, instances, now, toVHDL

from clock_driver import clock_driver



def program_counter(clk, address):
    """
    clk : clock signal    
    address: address output
    """

    @always(clk.posedge)
    def inc():        
        address.next = address + 1

    return inc


def testBench():

    clk = Signal(intbv(0)[1:])
    S = Signal(intbv(0, min=0, max=32))

    clkdriver_inst = clock_driver(clk)
    pc_inst = toVHDL(program_counter, clk, S)

    @instance
    def stimulus():
        while True:
            yield delay(1)
            print "time: %s | Clock: %i | address: %i" % (now(), clk, S)

    return instances()


def main():
    sim = Simulation(testBench())
    sim.run(20)

if __name__ == '__main__':
    main()
    
