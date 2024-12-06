import math

a, b, c = int(input()), int(input()), int(input())

T = b * b - 4 * a * c

if (T >= 0):
    T = math.sqrt(T)
    x1 = (-b + T) / (2 * a)
    x2 = (-b - T) / (2 * a)

    print("%.1f" %x1)
    print("%.1f" %x2)
else:
    T = math.sqrt(abs(T))
    x1 = (-b) / (2 * a)
    x2 = T / (2 * a)

    print("%.1f+%.1fi" %(x1,x2))
    print("%.1f-%.1fi" %(x1,x2))