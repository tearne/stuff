#!/usr/bin/env python

import time
from sys import exit

try:
    import psutil
except ImportError:
    exit('This script requires the psutil module\nInstall with: sudo pip install psutil')

import ledshim

ledshim.set_clear_on_exit()

nled = ledshim.NUM_PIXELS
norm = nled / 100


def show_graph(cpu):
    u = cpu.user + cpu.nice
    s = cpu.system + cpu.guest + cpu.guest + cpu.guest_nice + cpu.steal
    w = cpu.iowait + cpu.irq + cpu.softirq
    i = cpu.idle

    # Cumulative
    ac = u
    bc = ac + s
    cc = bc + w
    tot = cc + i

    for x in range(nled):
        if x < (ac * norm):
            r, g, b = 0, 100, 0
        elif x < (bc * norm):
            r, g, b = 150, 100, 0
        elif x < (cc * norm):
            r, g, b = 250, 0, 0
        elif x < (tot * norm):
            r, g, b = 0, 0, 0
        else:
            r, g, b = 100, 0,100

        ledshim.set_pixel(nled - x -1, r, g, b)
    ledshim.show()


ledshim.set_brightness(0.5)

while True:
    cpu = psutil.cpu_times_percent()
    show_graph(cpu)
    time.sleep(1)
