#Variables are container for storing data values. Think of them as labeled boxes where information is stored for later use.

#Example 1: Creating name and assigning a value.
name="Sajan"
age=20
height=5.7
is_student=True

print(name)
print(age)
print(height)
print(is_student)

#Example 2: Identifying data type for the variable. It can be done using type function.
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#Example 3: Assigning values to multiple variables in a single line
a=b=c=10
print(a)
print(b)
print(c)

name,age,height,is_student=("Sajina",25,5.5,False)
print(name)
print(age)
print(height)
print(is_student)

#Example 4: Swapping values of two variables
a,b=5,10
print(a)
print(b)

a,b=b,a
print(a)
print(b)

#Here we can see that the values of a and b have been interchanged. We did this without using any temporary variables. Python use unique feature called Tuple unpacking to do this.