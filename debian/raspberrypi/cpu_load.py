#!/usr/bin/env python

import time, random
from sys import exit

try:
    import psutil
except ImportError:
    exit('This script requires the psutil module\nInstall with: sudo pip install psutil')

import ledshim

ledshim.set_clear_on_exit()

nled = ledshim.NUM_PIXELS
norm = nled / 100

def getCPU():
    cpu = psutil.cpu_times_percent()
    arr = [0] * nled

    u = cpu.user + cpu.nice
    s = cpu.system + cpu.guest + cpu.guest_nice + cpu.steal
    w = cpu.iowait + cpu.irq + cpu.softirq
    i = cpu.idle

    # Cumulative
    ac = s
    bc = ac + w
    cc = bc + u
    tot = cc + i

    for x in range(nled):
        if x < (ac * norm):
            r = 30
        elif x < (bc * norm):
            r = 0
        elif x < (cc * norm):
            r = 250
        elif x < (tot * norm):
            r = 0
        else:
            r = 0

        arr[nled - x -1] = r
    
    return arr


def buildDiskIO(prevBytes = 0):
    def diskBytesDelta():
        nonlocal prevBytes
        def cumulativeBytes():
            counters = psutil.disk_io_counters()
            return counters.read_bytes + counters.write_bytes

        old = prevBytes
        prevBytes = cumulativeBytes()
        return prevBytes - old

    return diskBytesDelta

ledshim.set_brightness(1)
bytesThing = buildDiskIO()


def getIO(bytesMeter = buildDiskIO()):
    arr = [0] * nled

    if bytesMeter() > 0:
        for x in range(nled):
            arr[x] = random.randrange(255)
    
    return arr


while True:
    red = getCPU()
    green = getIO()

    for i in range(nled):
        ledshim.set_pixel(i, red[i], green[i], 0)
    ledshim.show()
    
    time.sleep(1)
