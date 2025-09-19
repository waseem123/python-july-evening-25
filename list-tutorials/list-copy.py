l1 = ['Bottle','Computer','Board','Screen']

l2 = l1
print(l2)

l3 = l1.copy()
print(l3)

l2[0] = 'Water Bottle'
print(l2)
print(l1)

l3[2] = 'White Board'
print(l3)
print(l1)