#1. Age Calculator:
#Ask the user for their birth year.
#Calculate their age in years and store it in a variable "age" (age = current_year - birth_year)
#Print: "You are [age] years old!"
birth_year=int(input("What is your birth year?"))
print("Your birth year is ",birth_year,".",sep="")

import time
current_year = time.localtime().tm_year
age = current_year - birth_year
print("You are", age, "years old!")

#2. Custom Greeting:
#Ask the user for their first and last name.
#Print a greeting: "Hello, [first name] [last name]! Welcome to Python programming."
first_name=input("What is your first name?")
last_name=input("What is your last name?")
print("Hello, ",first_name+ ' ' +last_name,"! Welcome to Python programming.",sep="")

#3. Distance Converter:
#Accept a distance in kilometers as float using type conversion with float()
#Convert it to miles and store it in a new variable. (Miles=Kilometers×0.621371)
#Print the distance in miles

# Accept distance in kilometers
kilometers = float(input("Enter distance in kilometers: "))

# Convert to miles
miles = kilometers * 0.621371

# Print the result
print("Distance in miles:", miles)