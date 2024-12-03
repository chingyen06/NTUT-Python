import math

height = float(input())
weight = int(input())

bmi = weight / (height * height)

lastnum = math.floor(bmi * 1000) % 10
seclastnum = math.floor(bmi * 100) % 10

if (lastnum == 5):
    if (seclastnum % 2 == 0):
        bmi = round(bmi-0.001, 2)
    else:
        bmi = round(bmi+0.001, 2)
else:
    bmi = round(bmi, 2)

print("%.2f" %bmi)
