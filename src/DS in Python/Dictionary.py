#A dictionary is a collection of key-value pairs.
#Keys are unique and they map to specific values.
#Dictionary are mutable so you can modify them by adding or removing key-values pairs.

my_dict={'name':'John','age':25,'city':'New York'}
print(my_dict)

#Dictionary Operations
#Access dictionary key values.
print(my_dict['name'])

#Add new key values pairs
my_dict['job']='Engineer'
print(my_dict)

#Remove a key value pair
del my_dict['age']
print(my_dict)

#Replace a key value pair
my_dict['city']='Texas'
print(my_dict)