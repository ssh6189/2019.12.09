color1 = ['red', 'green', 'blue']
color2 = ['yellow', 'purple', 'orange']

total = color1 + color2
print(total)

print('blue' in color1)


color1.append('white')
print(color1)
color1.extend(color2)
print(color1)
color1.insert(0,'black')
print(color1)

color3 = ['red', 'blue', 'red']
color3.remove('red')
print(color3)

str(input())
