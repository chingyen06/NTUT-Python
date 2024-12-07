#不同天正確
times = ["4a", "3c", "11"]

times = sorted(times)

print(times)

############################

#同一天正確
times2 = ["4b", "4a", "41"]

times2 = sorted(times2)

print(times2)

############################

times3 = sorted(times + times2)

print(times3)
