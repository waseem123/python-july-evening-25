mylist = ['Solapur','Pune','Mumbai','Chennai','Solapur','Kolkata','Delhi','Hyderabad','Nasik']
print(mylist)

print(mylist[0])
print(mylist[6])
print(mylist[6-3])
print("---------------")

for i in mylist:
    print(i,end='-')
print("_______________")   

mylist = ['Madiha','Taha','Munawwar','Abhijeet','Shardul','Gufran','Farhan','Nihal']
for i in range(0,len(mylist)):
    print((i+1),mylist[i])