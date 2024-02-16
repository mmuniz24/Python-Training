#Lists
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

#Access Elements in List
print(bicycles[0].title())
print(bicycles[2].title())

#Access last item
print(bicycles[-1].title())

message = f"My first bicycle was a {bicycles[-1].title()}"
print(message)

#Modifying Lists
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = "toyota"
print(motorcycles)

#Append
motorcycles.append("ducati")
print(motorcycles)

movies = []
movies.append("star wars")
movies.append("goodfellas")
movies.append("godfather")
print(movies)

#Insert
movies.insert(1, "mad max")
print(movies)

#Deleting
print(motorcycles)
del motorcycles[3]
print(motorcycles)

#Pop
print(movies)
movieSelected = movies.pop(1)
print(movies)
print(f"You have selected {movieSelected.title()}")

#Removing
print(motorcycles)
motorcycles.remove("toyota")
print(motorcycles)

#Organizing a List
cars = ["bmw", "audi", "toyota", "subaru"]
#Sort -> Alphabetical
print(cars)
cars.sort()
print(cars)
#sort(reverse=true) -> reverse alphabetical
#cars.sort(reverse=True)
print(cars)

#Sorted() -> sort temporarily
print("Here's the original list:")
print(cars)
print("\nHere's the sorted list:")
print(sorted(cars))
print("\nHere's the original list again:")
print(cars)

#Reverse
print(cars)
cars.reverse()
print(cars)

#Length of list
print(len(cars))