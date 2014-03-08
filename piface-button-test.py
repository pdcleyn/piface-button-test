#!/usr/bin/python

import pifacedigitalio as p
p.init()

#keep track of state of the inputs of previous run
prevports = -1

while 1:
    #mask will indicate which bit to set in the bitfield
    mask = 1
    #bitfield to record state of all ports
    ports = 0
    
    for x in range(0,8):
        #read port state of port x
        i = p.digital_read(x)
        #if port is high, add it to the bitfield
        if (i == 1):
            ports = ports | mask
        #set mask for next port
        mask = mask << 1
    #only output a line if a change since last check has been detected and save the new state
    if (ports != prevports):
        print "ports: %s" % bin(ports)[2:].zfill(8)
        prevports = ports
