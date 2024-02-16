#Use print function for output
print("Hello World")

#Create a variable
message = "Hello World Message"
print(message)

#Can change the value of a variable at any time
message = "I changed the message"
print(message)

#Change Case in Strings with Methods
#Title() capitalizes first letter of words
name = "marco muniz"
print(name.title())

#upper()
print(name.upper())

#lower()
print(name.lower())

#Using Variables as Strings
firstName = "Marco"
lastName = "Muniz"
#f"" combines strings and variables into a single string
fullName = f"{firstName} {lastName}"
print(fullName)
print(f"Hello, {fullName.title()}!")
message = f"Hello, {fullName.title()}!"
print(message)

#Adding whitespaces to strings
#\t -> tabs
text = "Hello There!"
print(text)
tabText = f"\t{text}"
print(tabText)

#\n -> new line
text = "Programming Languages:\n\tPython\n\tC#\n\tJavaScript"
print(text)

#Stripping Whitespace
favoriteLanguage = "    Python    "
#lstrinp -> strips left whitespace
print(favoriteLanguage.lstrip())
#rstrip -> strips right whitespace
print(favoriteLanguage.rstrip())
#strip -> strips all whitespace
print(favoriteLanguage.strip())

#remove prefixes
noStarchURL = "https://nostarch.com"
print(noStarchURL.removeprefix("https://"))

#Maths
#** -> used for exponents
answer = 3**3
print(answer)

#Integers -> 1,2,3...
#Floats -> 1.0,2.0,3.0
#Math calculations will always come out as float
#can use underscores in numbers for better readability
#multiple assignments
x, y, z = 0,0,0

#Constants
MAX_CONNECTIONS = 5000
