import copy

x1 = [1, [9, 7, 5], 3]
x2 = x1
x3 = copy.copy(x1)
x4 = copy.deepcopy(x1)

#x1.pop(0)  #reference vs copy
#x1[1].pop(1)  #deepcopy vs copy

print(x1, x2, x3, x4)
