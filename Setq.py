#Difference of Sets

seta = set(['Iron_man','War_Machine','Spider_Man'])
setb = set(['Spider_Man','Venom','Hulk'])

print('Difference is :', seta - setb)

#Intersection of Two Sets
seta = set(['Iron_man','War_Machine','Spider_Man'])
setb = set(['Spider_Man','Venom','Hulk'])

print('Intersection is :', seta & setb)



#Comparing Two Sets
seta = set(['Iron_man','War_Machine','Spider_Man','Venom','Hulk'])
setb = set(['Spider_Man','Venom','Hulk'])
ifsubeset = seta <= setb
print('If set a is subset of set b :',ifsubeset)
ifsuperset = seta >= setb
print('If set b is subset of set a :',ifsuperset)
