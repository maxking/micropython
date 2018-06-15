from neopixel_helpers import cycle, bounce, fade_in_out, np_setup, COLORS


np = np_setup()
for i, color in enumerate(COLORS):
    cycle(np, color)
    bounce(np, COLORS[i-1])
    fade_in_out(np, COLORS[i-2])
