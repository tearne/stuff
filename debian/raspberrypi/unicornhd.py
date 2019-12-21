# sudo apt install python3-spidev python3-numpy
# pip3 install unicornhathd

import psutil, time
import unicornhathd as uhd

uhd.rotation(-90)
uhd.brightness(1.0)

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

    def set_row(y, r, g, b):
        for x in range(5,10):
            uhd.set_pixel(x, y, r, g, b)

    for y in range(16):
        if y <= aIdx:
            set_row(y, 70, 0, 0)
        elif y <= bIdx:
            set_row(y, 0, 0, 150)
        elif y <= cIdx:
            set_row(y, 0, 100, 0)
        else:
            set_row(y, 0, 0, 0)
    
    uhd.show()

while True:
    doCPU()
    time.sleep(1)