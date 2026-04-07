#A list is an ordered collection of items.
#Contents can be changed after creation
#Lists can store elements of types e.g. int,str,etc.

my_list=[1,2,3,4,5,'black','pink','purple','red']
print(my_list)

#Accessing elements of the list
print(my_list[0])
print(my_list[1])
print(my_list[6])

#Append (Add element to the list)
my_list.append('white')
print(my_list)

#Remove elements from the list
my_list.remove(3)
print(my_list)

#Retrive part of the list
print(my_list[1:4])

#Replac
#There is no replace method in python
#can be achieved by replacing list item manually

print(my_list[5])
my_list[5]='blue'
print(my_list)