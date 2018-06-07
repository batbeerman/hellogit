test = [13,22,30,42,53,61,73,86,98]
even_counter= 0
odd_counter = 0

for x in test:
    if (x % 2 == 0):
        even_counter += 1
    else:
        odd_counter += 1

print('Total even num. in list :' , even_counter)
print('Total odd num. in list :' , odd_counter)
