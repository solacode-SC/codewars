# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))

def rgb(r, g, b):
    r = int(r)
    g = int(g)
    b = int(b)
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    return ("%02x%02x%02x" % (r, g, b)).upper()

print(rgb(255, 255, 255))