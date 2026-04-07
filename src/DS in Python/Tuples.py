#A Tuple is an ordered collection of items.
#Their contents cannot be changed after creation.
#Useful for storing data that should not be modified.

my_tuple = (1, 2, 3,4,5)
print(my_tuple)

#Access tuple elements using index
print(my_tuple[1])

#Content of Tuples cannot be modified, but we can concatenate two or more tuples to create a new tuple.

tuple2=(6,7,8)
new_tuple=my_tuple+tuple2
print(new_tuple)