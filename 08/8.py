Class = ["", "", ""]
hours = [0, 0, 0]
times = [["99", "99", "99"], ["99", "99", "99"], ["99", "99", "99"]]
defined = ["11", "1c", "21", "2c", "31", "3c", "41", "4c", "51", "5c"]
check = 1
searched = 0

for i in range(3):
    Class[i] = input()
    hours[i] = int(input())

    if (hours[i] < 1 or hours[i] > 3):
        check = 0

    for j in range(hours[i]):
        times[i][j] = input()

        if (check == 1):
            check = 0
            for k in range(0, 9, 2):
                if (defined[k] <= times[i][j] <= defined[k+1]):
                    check = 1
                    break

if (check == 1):
    for i in range(3):
        for j in range(hours[i]):
            for k in range(i, 3):
                for l in range(hours[k]):
                    if (i != k and times[i][j] == times[k][l] and times[i][j] != "99"):
                        print(Class[i] + "," + Class[k] + "," + times[i][j])
                        searched = 1

    if (searched == 0):
        print("correct")
else:
    print("-1")