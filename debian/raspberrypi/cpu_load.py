#!/usr/bin/env python3

import time, random, subprocess
from sys import exit
import ledshim

try:
    import psutil
except ImportError:
    exit('This script requires the psutil module\nInstall with: sudo pip install psutil')

class LEDRange:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.width = upper - lower
        self.range = range(lower, upper + 1)

    def toLEDIndex(self, fraction):
        # print("fraction ", fraction)
        return self.lower + int(round(self.width * fraction))

class Lights:
    def __init__(self):
        ledshim.set_clear_on_exit()
        ledshim.set_brightness(1)
        self.array = [(0,0,0)] * ledshim.NUM_PIXELS
    
    def set(self, index, r, g, b):
        self.array[index] = (r,g,b)

    def drawAndReset(self):
        for i in range(ledshim.NUM_PIXELS):
            ledshim.set_pixel(
                i, 
                self.array[i][0], 
                self.array[i][1], 
                self.array[i][2]
            )
            self.array[i] = (0,0,0)

        ledshim.show()

# 0123456789012345678901234567
# |-bat-||--hdd--||----CPU---|

batLEDRange = LEDRange(0, 6) 
hddLEDRange = LEDRange(7, 10)
cpuLEDRange = LEDRange(11, 27)

def doCPU(lights):
    cpu = psutil.cpu_times_percent()

    s = cpu.system + cpu.steal + cpu.guest_nice + cpu.guest
    w = cpu.irq + cpu.iowait +  cpu.softirq
    u = cpu.user + cpu.nice
    i = cpu.idle

    # Cumulative
    ac = s
    bc = ac + w
    cc = bc + u
    tot = cc + i

    aIdx = cpuLEDRange.toLEDIndex(ac / 100)
    bIdx = cpuLEDRange.toLEDIndex(bc / 100)
    cIdx = cpuLEDRange.toLEDIndex(cc / 100)

    for x in cpuLEDRange.range:
        if x <= aIdx:
            lights.set(x, 100, 0, 0)
        elif x <= bIdx:
            lights.set(x, 0, 0, 100)
        elif x <= cIdx:
            lights.set(x, 50, 150, 0)
        # elif x < (tot * norm):
        #     r = 0
        else:
            r = lights.set(x, 0, 0, 0)



def DiskIOMeter(prevBytes = 0, maxBytesSoFar = 10000):
    first = True

    def diskPercentage():
        nonlocal prevBytes, maxBytesSoFar, first
        def cumulativeBytes():
            counters = psutil.disk_io_counters()
            return counters.read_bytes + counters.write_bytes

        old = prevBytes
        prevBytes = cumulativeBytes()

        delta = prevBytes - old
        if not first:
            maxBytesSoFar = max(delta, maxBytesSoFar)
        
        first = False
        
        fraction = min(prevBytes - old, maxBytesSoFar) / maxBytesSoFar

        # print("max = ", maxBytes, "  delta = ", delta, "  percentage = ", fraction)

        return fraction

    return diskPercentage

def doIO(lights, ioPercentage):
    # hddPctIdx = hddLEDRange.toLEDIndex(ioPercentage())
    # for i in hddLEDRange.range:
    #     if i < hddPctIdx:
    #         lights.set(i, 0, 50, 0)
    #     else:
    #         lights.set(i, 0, 0, 0)
    if(ioPercentage() > 0):
        for i in hddLEDRange.range:
            lights.set(i, 100, 100, 100)

def doBat(lights):
    out = subprocess.Popen(["lifepo4wered-cli","get","vbat"], stdout=subprocess.PIPE).communicate()[0]
    vbat = int(out.splitlines()[0].decode('ascii'))

    vmax = 3300
    vmin = 2960
    range = vmax - vmin
    frac = min((vbat - vmin) / range, 1)
    batPctIdx = batLEDRange.toLEDIndex(frac)

    if(vbat > vmax):
        for i in batLEDRange.range:
            lights.set(i, 0, 100, 100)
    else:
        for i in batLEDRange.range:
            if i <= batPctIdx:
                lights.set(i, 0, 0, 250)
            else:
                lights.set(i, 250, 0, 100)

lights = Lights()
diskMeter = DiskIOMeter()

while True:
    doCPU(lights)
    doIO(lights, diskMeter)
    doBat(lights)
    
    lights.drawAndReset()
    
    time.sleep(1)
