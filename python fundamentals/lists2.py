# Chapter 4: working with lists and looping through an entire list 
brands = ["logitech","razer", "zowie", "steelseries"]
for brand in brands:
    print(brand.title() + ", is a great brand! ")
    print("what is " + brand.title() + "'s best product?")
print("ah okay thank you for the recommendation! ")

#using the range() function
for value in range(1,6):
    print(value)

#using range to make a list of numbers, fr this we start at 2 and add 2 to that value until it reaches 11 
even_numbers = list(range(2,11,2))
print(even_numbers)

#in python two ** represents exponents
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#different way of building lists with exponents
cubes = [value**3 for value in range (1,6)]
print(cubes)

#simple statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#slicing a list , python stops one item before the second index specified
fruits = ["banana","apple","watermelon", "kiwi", "tomato", "cherry"]
print(fruits[1:4]) 
#if first index is omitted python auto starts slice at the beginning of the list
#if second index is omitted python returns chosen item through to the last item 
print(fruits[:5]) 
print(fruits[2:])
#this syntax allows you to output all elements from any point of list to the end
print(fruits[-3:])

#looping thru a slice
cars = ["mercedes", "audi", "porsche", "ferrari","mustang"]
print("here are my top 3 car brands:")
for car in cars[:3]:
    print(car.title())

#copying a list
my_bubbletea = ["sanchen", "playmade", "koi", "gongcha", "liho"]
my_bubbletea.append("the alley")
friends_bubbletea = my_bubbletea[2:]
friends_bubbletea.append("sweettalk")
print("my favourite bubbleteas are:")
print(my_bubbletea)
print("my friends favourite bubbleteas are:")
print(friends_bubbletea)

#defining a tuple 
dimensions = (490, 420, 500, 700)
print(dimensions[1])
for dimension in dimensions:
    print (dimension)
dimensions = (420,390,450,470)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#while loop