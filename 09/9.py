length = list()

def position():
    x1, x2 = int(input()), int(input())

    for i in range(x1, x2):
        length[i+20] = 1

    return 0

def main():
    t = 0

    for i in range(41):
        length.append(0)

    position(), position(), position()

    for i in range(41):
        if (length[i] == 1):
            t = t + 1

    print(t)

if __name__ == "__main__":
    main()