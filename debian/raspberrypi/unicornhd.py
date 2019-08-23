# sudo apt install python3-spidev python3-numpy
# pip3 install unicornhathd

import psutil, time
import unicornhathd as uhd

uhd.rotation(-90)

def doCPU():
    cpu = psutil.cpu_times_percent()

    u = cpu.user + cpu.nice
    s = cpu.system + cpu.steal + cpu.guest_nice + cpu.guest
    w = cpu.irq + cpu.iowait +  cpu.softirq
    i = cpu.idle

    # Cumulative
    ac = s
    bc = ac + w
    cc = bc + u
    tot = cc + i

    aIdx = 16 * (ac / 100)
    bIdx = 16 * (bc / 100)
    cIdx = 16 * (cc / 100)

    uhd.clear()

    for x in range(16):
        if x <= aIdx:
            uhd.set_pixel(0, x, 40, 0, 0)
        elif x <= bIdx:
            uhd.set_pixel(0, x, 0, 0, 150)
        elif x <= cIdx:
            uhd.set_pixel(0, x, 0, 100, 0)
        # elif x < (tot * norm):
        #     r = 0
        else:
            uhd.set_pixel(0, x, 0, 0, 0)
    
    uhd.show()

while True:
    doCPU()
    time.sleep(1)