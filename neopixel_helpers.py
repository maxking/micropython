import time

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
AQUA = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (148, 0, 211)
INDIGO = (75, 0, 130)
ORANGE = (255, 127, 0)

COLORS = (RED, YELLOW, GREEN, AQUA, BLUE, PURPLE)

RAINBOWS = (PURPLE, INDIGO, BLUE, GREEN, YELLOW, ORANGE, RED)


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
    for i in range(0, 4 * 256, n):
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


def np_setup(pin_no=12, num_pixels=12):
    import neopixel, machine
    np = neopixel.NeoPixel(machine.Pin(pin_no), num_pixels)
    return np


def clear(np):
    np.fill((0, 0, 0))
    np.write()


def rainbow(np, wait=0.5):
    for color in RAINBOWS:
        np.fill(color)
        np.write()
        time.sleep(wait)
    clear(np)
