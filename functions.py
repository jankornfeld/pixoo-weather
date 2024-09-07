from colors import blue, light_blue, yellow, orange, black

# height: 6, width: 8
def cloud(x,y):
    return [
        ((x+2,y), blue),
        ((x+3,y), blue),
        ((x+1,y+1), blue),
        ((x+1,y+2), blue),
        ((x,y+3), blue),
        ((x,y+4), blue),
        ((x+1,y+5), blue),
        ((x+2,y+5), blue),
        ((x+3,y+5), blue),
        ((x+4,y+5), blue),
        ((x+5,y+5), blue),
        ((x+6,y+5), blue),
        ((x+4,y+1), blue),
        ((x+4,y+2), blue),
        ((x+5,y+1), blue),
        ((x+6,y+2), blue),
        ((x+7,y+3), blue),
        ((x+7,y+4), blue),

        ((x+2,y+1), light_blue),
        ((x+3,y+1), light_blue),
        ((x+2,y+2), light_blue),
        ((x+3,y+2), light_blue),
        ((x+1,y+3), light_blue),
        ((x+2,y+3), light_blue),
        ((x+3,y+3), light_blue),
        ((x+4,y+3), light_blue),
        ((x+5,y+3), light_blue),
        ((x+6,y+3), light_blue),
        ((x+1,y+4), light_blue),
        ((x+2,y+4), light_blue),
        ((x+3,y+4), light_blue),
        ((x+4,y+4), light_blue),
        ((x+5,y+4), light_blue),
        ((x+6,y+4), light_blue),
        ((x+5,y+2), light_blue),
    ]

def rainy(x,y):
    return cloud(x,y) + [
        ((x+1,y+6), light_blue),
        ((x+5,y+6), light_blue),
        ((x+3,y+7), light_blue),
        ((x+7,y+7), light_blue),
    ]

def dizzle(x,y):
    return cloud(x,y) + [
        ((x+2,y+6), light_blue),
        ((x+5,y+7), light_blue),
    ]

# height: 8, width: 8
def sun(x,y):
    return [
        ((x+3,y), yellow),
        ((x+4,y), yellow),
        ((x+1,y+1), yellow),
        ((x,y+3), yellow),
        ((x,y+4), yellow),
        ((x+1,y+6), yellow),
        ((x+3,y+7), yellow),
        ((x+4,y+7), yellow),
        ((x+4,y+7), yellow),
        ((x+6,y+1), yellow),
        ((x+7,y+3), yellow),
        ((x+7,y+4), yellow),
        ((x+6,y+6), yellow),
        ((x+3,y+2), yellow),
        ((x+4,y+2), yellow),
        ((x+2,y+3), yellow),
        ((x+3,y+3), yellow),
        ((x+4,y+3), yellow),
        ((x+5,y+3), yellow),
        ((x+2,y+4), yellow),
        ((x+3,y+4), yellow),
        ((x+4,y+4), yellow),
        ((x+5,y+4), orange),
        ((x+3,y+5), orange),
        ((x+4,y+5), orange),
    ]

def lineX(x_start,length,y):
    i = x_start
    result = []
    while i < length:
        result = result + [(i,y)]
        i += 1
    return result

def lineY(y_start,length,x):
    i = 0
    result = []
    while i < length:
        result = result + [(x,y_start)]
        y_start += 1
        i += 1
    return result

# 19
def bigSun(x,y):
    return [
        ((x+9,y), yellow),
        ((x+9,y+1), yellow),

        ((x+9,y+17), orange),
        ((x+9,y+18), orange),

        ((x,y+9), yellow),
        ((x+1,y+9), yellow),
        
        ((x+17,y+9), orange),
        ((x+18,y+9), orange),

        ((x+1,y+1), yellow),
        ((x+2,y+2), yellow),
        ((x+3,y+3), yellow),

        ((x+17,y+1), yellow),
        ((x+16,y+2), yellow),
        ((x+15,y+3), yellow),

        ((x+17,y+17), orange),
        ((x+16,y+16), orange),
        ((x+15,y+15), orange),

        ((x+1,y+17), yellow),
        ((x+2,y+16), yellow),
        ((x+3,y+15), yellow),

        ((x+7,y+3), yellow),
        ((x+8,y+3), yellow),
        ((x+9,y+3), yellow),
        ((x+10,y+3), yellow),
        ((x+11,y+3), yellow),

        ((x+5,y+4), yellow),
        ((x+6,y+4), yellow),
        ((x+7,y+4), yellow),
        ((x+8,y+4), yellow),
        ((x+9,y+4), yellow),
        ((x+10,y+4), yellow),
        ((x+11,y+4), yellow),
        ((x+12,y+4), yellow),
        ((x+13,y+4), yellow),

        ((x+4,y+5), yellow),
        ((x+5,y+5), yellow),
        ((x+6,y+5), black),
        ((x+7,y+5), yellow),
        ((x+8,y+5), yellow),
        ((x+9,y+5), yellow),
        ((x+10,y+5), yellow),
        ((x+11,y+5), black),
        ((x+12,y+5), yellow),
        ((x+13,y+5), yellow),
        ((x+14,y+5), orange),

        ((x+4,y+6), yellow),
        ((x+5,y+6), yellow),
        ((x+6,y+6), black),
        ((x+7,y+6), yellow),
        ((x+8,y+6), yellow),
        ((x+9,y+6), yellow),
        ((x+10,y+6), yellow),
        ((x+11,y+6), black),
        ((x+12,y+6), yellow),
        ((x+13,y+6), yellow),
        ((x+14,y+6), orange),

        ((x+3,y+7), yellow),
        ((x+4,y+7), yellow),
        ((x+5,y+7), yellow),
        ((x+6,y+7), black),
        ((x+7,y+7), yellow),
        ((x+8,y+7), yellow),
        ((x+9,y+7), yellow),
        ((x+10,y+7), yellow),
        ((x+11,y+7), black),
        ((x+12,y+7), yellow),
        ((x+13,y+7), yellow),
        ((x+14,y+7), yellow),
        ((x+15,y+7), orange),

        ((x+3,y+8), yellow),
        ((x+4,y+8), yellow),
        ((x+5,y+8), yellow),
        ((x+6,y+8), black),
        ((x+7,y+8), yellow),
        ((x+8,y+8), yellow),
        ((x+9,y+8), yellow),
        ((x+10,y+8), yellow),
        ((x+11,y+8), black),
        ((x+12,y+8), yellow),
        ((x+13,y+8), yellow),
        ((x+14,y+8), yellow),
        ((x+15,y+8), orange),

        ((x+3,y+9), yellow),
        ((x+4,y+9), yellow),
        ((x+5,y+9), yellow),
        ((x+6,y+9), yellow),
        ((x+7,y+9), yellow),
        ((x+8,y+9), yellow),
        ((x+9,y+9), yellow),
        ((x+10,y+9), yellow),
        ((x+11,y+9), yellow),
        ((x+12,y+9), yellow),
        ((x+13,y+9), yellow),
        ((x+14,y+9), yellow),
        ((x+15,y+9), orange),

        ((x+3,y+10), yellow),
        ((x+4,y+10), yellow),
        ((x+5,y+10), yellow),
        ((x+6,y+10), yellow),
        ((x+7,y+10), yellow),
        ((x+8,y+10), yellow),
        ((x+9,y+10), yellow),
        ((x+10,y+10), yellow),
        ((x+11,y+10), yellow),
        ((x+12,y+10), yellow),
        ((x+13,y+10), yellow),
        ((x+14,y+10), yellow),
        ((x+15,y+10), orange),

        ((x+3,y+11), yellow),
        ((x+4,y+11), yellow),
        ((x+5,y+11), yellow),
        ((x+6,y+11), yellow),
        ((x+7,y+11), yellow),
        ((x+8,y+11), yellow),
        ((x+9,y+11), yellow),
        ((x+10,y+11), yellow),
        ((x+11,y+11), yellow),
        ((x+12,y+11), yellow),
        ((x+13,y+11), yellow),
        ((x+14,y+11), yellow),
        ((x+15,y+11), orange),

        ((x+4,y+12), yellow),
        ((x+5,y+12), yellow),
        ((x+6,y+12), black),
        ((x+7,y+12), yellow),
        ((x+8,y+12), yellow),
        ((x+9,y+12), yellow),
        ((x+10,y+12), yellow),
        ((x+11,y+12), black),
        ((x+12,y+12), yellow),
        ((x+13,y+12), yellow),
        ((x+14,y+12), orange),

        ((x+4,y+13), yellow),
        ((x+5,y+13), yellow),
        ((x+6,y+13), yellow),
        ((x+7,y+13), black),
        ((x+8,y+13), black),
        ((x+9,y+13), black),
        ((x+10,y+13), black),
        ((x+11,y+13), yellow),
        ((x+12,y+13), yellow),
        ((x+13,y+13), yellow),
        ((x+14,y+13), orange),

        ((x+5,y+14), yellow),
        ((x+6,y+14), yellow),
        ((x+7,y+14), yellow),
        ((x+8,y+14), yellow),
        ((x+9,y+14), yellow),
        ((x+10,y+14), yellow),
        ((x+11,y+14), yellow),
        ((x+12,y+14), yellow),
        ((x+13,y+14), orange),

        ((x+7,y+15), orange),
        ((x+8,y+15), orange),
        ((x+9,y+15), orange),
        ((x+10,y+15), orange),
        ((x+11,y+15), orange),
    ]