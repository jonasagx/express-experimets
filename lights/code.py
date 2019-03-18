import time
import random
from adafruit_circuitplayground.express import cpx

while True:
    for i in range(9, 0, -1):
        s = time.localtime().tm_sec
        m = time.localtime().tm_min
        h = time.localtime().tm_hour
        cpx.pixels[i] = (h, m+30, s)
        time.sleep(1)
    cpx.pixels[0] = (0, 0, 0)
    cpx.pixels[1] = (0, 0, 0)
    cpx.pixels[2] = (0, 0, 0)
    cpx.pixels[3] = (0, 0, 0)
    cpx.pixels[4] = (0, 0, 0)
    cpx.pixels[5] = (0, 0, 0)
    cpx.pixels[6] = (0, 0, 0)
    cpx.pixels[7] = (0, 0, 0)
    cpx.pixels[8] = (0, 0, 0)
    cpx.pixels[9] = (0, 0, 0)