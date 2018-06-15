import time

RED = (0x10, 0, 0)
YELLOW = (0x10, 0x10, 0)
GREEN = (0, 0x10, 0)
AQUA = (0, 0x10, 0x10)
BLUE = (0, 0, 0x10)
PURPLE = (0x10, 0, 0x10)
BLACK = (0, 0, 0)

COLORS = (RED, YELLOW, GREEN, AQUA, BLUE, PURPLE, BLACK)

def cycle(np, color, num=4):
    import time
    n = np.n
    for i in range(num * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = color
        np.write()
        time.sleep_ms(25)


def bounce(np, color):
    n = np.n
    for i in range(4 * n):
        for j in range(n):
            np[j] = color
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)


def fade_in_out(np, color):
    n = np.n
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
                np[j] = (val, 0, 0)
        np.write()


def clear(np, color=(0, 0, 0)):
    # clear
    for i in range(n):
        np[i] = color
    np.write()

def np_setup():
    import neopixel, machine
    np = neopixel.NeoPixel(machine.Pin(12), 12)
    return np
