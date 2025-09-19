cities = ('Solapur', 'Mumbai', 'Pune', 'Chennai')
print(cities)

# cities.insert(0,'Hyderabad')
# cities[10] = 'Hyderabad'

x = list(cities)
print(x)

x.append('Hyderabad')
print(x)

cities = tuple(x)
print(cities)