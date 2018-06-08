test = ['MISSISIPI']
test = ['M','I','S','S','I','S','I','P','I']
dict = dict( [ (i, test.count(i)) for i in set(test) ] )
print(dict)
