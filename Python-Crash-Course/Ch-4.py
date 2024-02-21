#Looping Entire List
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    #indented lines mean they are in the for loop
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

message = "Thank you, everyone! That was a great magic show!"
print(message)

#Making numerical lists
for num in range(1,5):
    print(num)

for value in range(1,6):
    print(value)

#Using range() to make list of numbers
numbers = list(range(1,6))
print(numbers)

#skipping numbers using range()
evenNumbers = list(range(2,11, 2))
print(evenNumbers)

squares = []
for num in range(1,11):
    square = num ** 2
    squares.append(square)
print(squares)

#Cleaner version
cleanSquares = []
for value in range(1,11):
    cleanSquares.append(value ** 2)
print(cleanSquares)

#Simple Statistics with a List of numbers
digits = [0]
for digit in range(1,10):
    digits.append(digit)

print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

#List Comprehensions -> simplying blocks of code into simple lines
compSquares = [value ** 2 for value in range(1,11)]
print(compSquares)

#Working with Part of a List
#Slicing a list
players = ["charles", "martina", "michael", "florence", "eli"]
print(players)
print(players[0:3])
print(players[1:4])
#without first index, starts at beginning
print(players[:4])
#without second index, includes end of list
print(players[2:])
#prints out last 3 players, regardless of size
print(players[-3:])

#Looping through slice
message = "Here are the first 3 players on my team:"
print(message)
for player in players[:3]:
    print(player.title())

#Copying a List
myFoods = ["pizza", "falafel", "carrot cake"]
#[:] -> entire list
friendFoods = myFoods[:]

myFoods.append("cannoli")
friendFoods.append("ice cream")

print("My favorite foods are:")
print(myFoods)

print("\nMy friend's favorite foods are:")
print(friendFoods)

#Tuples
#Immutable -> does not change
#tuple -> immutable list
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#Looping through all values in a tuple
for dimension in dimensions:
    print(dimension)

#Writing over a tuple
print("Original dimensions:")
print(dimensions)

dimensions = (400,100)
print("\nModified dimensions:")
print(dimensions)
