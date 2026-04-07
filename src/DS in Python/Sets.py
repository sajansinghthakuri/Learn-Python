#Set is an unordered collection of unique elements
#Set do not allow duplicate values, and the elements are not indexed.

my_set={1,2,3,4,5}
print(my_set)

#Adding new values to the set with add method
my_set.add(6)
print(my_set)

#Remove elements
my_set.remove(3)
print(my_set)

#Fundamentals of Set Operations (Union, Intersection, Difference)

#Union Operator combines two set and return all unique element from both.
set1={1,2,3}
set2={3,4,5,6,7}

#union=set1.union(set2)
union=set1|set2
print(union)

#Intersection returns only the common elements between two sets
intersection=set1&set2
print(intersection)

#Difference operator returns the elements that are in the first set, but not in the second set.
difference1=set1-set2
difference2=set2-set1
print(difference1)
print(difference2)