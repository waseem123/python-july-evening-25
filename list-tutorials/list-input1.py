mylist = []
n = int(input('ENTER THE NO. OF ELEMENTS YOU WANT TO INSERT - '))

for i in range(n):
    x = input(f'ENTER ELEMENT {i+1}- ')
    mylist.append(x)
    
print(mylist)