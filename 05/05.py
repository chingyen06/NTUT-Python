def getTriangle(a, b, c):
    if (a + b <= c or a + c <= b or b + c <= a):
        print("not a triangle")
    elif (a == b == c):
        print("equilateral triangle")
    elif ((a == b and a**2 + b**2 > c**2) or (a == c and a**2 + c**2 > b**2) or (b == c and b**2 + c**2 > a**2)):
        print("isosceles triangle")
    elif (c**2 > a**2 + b**2):
        print("obtuse triangle")
    elif (c**2 < a**2 + b**2):
        print("acute triangle")
    elif (c**2 == a**2 + b**2):
        print("right triangle")


def main():
    triangle = [0, 0, 0]
    triangle[0], triangle[1], triangle[2] = int(input()), int(input()), int(input())

    triangle = sorted(triangle)

    getTriangle(triangle[0], triangle[1], triangle[2])

if __name__ == "__main__":
    main()
