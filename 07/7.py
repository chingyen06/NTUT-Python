a, b, c, d, e, f = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())

cheap = a * 0.08 + b * 0.139 + c * 0.135 + d * 1.128 + e * 1.483 
middle = a * 0.07 + b * 0.130 + c * 0.121 + d * 1.128 + e * 1.483
expensive = a * 0.06 + b * 0.108 + c * 0.101 + d * 1.128 + e * 1.483
horrible = a * 0.05 + b * 0.100 + c * 0.090 + d * 1.128 + e * 1.483

if (f > 1):
    cheap = cheap + (f - 1) * 250
if (f > 3):
    middle = middle + (f - 3) * 200
if (f > 5):
    expensive = expensive + (f - 5) * 150

if (cheap < 183):
    cheap = 183
if (middle < 383):
    middle = 383
if (expensive < 983):
    expensive = 983
if (horrible < 1283):
    horrible = 1283

price = sorted([cheap, middle, expensive, horrible])

if (cheap == price[0]):
    print(str(int(cheap)) + "\n183")
elif (middle == price[0]):
    print(str(int(middle//1)) + "\n383")
elif (expensive == price[0]):
    print(str(int(expensive//1)) + "\n983")
else:
    print(str(int(horrible//1)) + "\n1283")