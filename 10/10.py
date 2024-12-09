def gameInput():
    point = list()
    game = 1

    point.append(int(input()))

    if (checkPoint(point) == 1):
        point.append(int(input()))
        game = game + 1 + checkPoint(point)

    return point, game

def checkPoint(game):
    if (sum(game) == 10):
        return 0
    return 1
    
def main():
    t = 0
    ninePoint, nine = gameInput()
    tenPoint, ten = gameInput()

    if (nine == 1):
        t = t + sum(tenPoint)
    elif (nine == 2):
        t = t + tenPoint[0]

    if (ten == 1):
        t = t + int(input()) + int(input())
    elif (ten == 2):
        t = t + int(input())

    t = t + sum(ninePoint) + sum(tenPoint)

    print(t)

if __name__ == "__main__":
    main()