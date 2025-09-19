l1 = ['Bottle','Computer','Board','Screen']
l2 = ['Clock','Fan','Light']

l3 = l2 + l1
print(l3)

l2.extend(l1)
print(l1)
print(l2)

l2.extend(['Chair'])
print(l2)

l4 = l1*20
print(l4)
print(l2)
x = l2[0:7]
print(x)