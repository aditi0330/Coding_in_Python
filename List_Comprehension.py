# Squares

nums = range(11)
squares = [i*i for i in nums]

# Adding

nums = [4, 8, 15, 16, 23, 42]

add_ten = [i+10 for i in nums]

# Parity

nums = [4, 8, 15, 16, 23, 42]

parity = [i%2 for i in nums]

# Size 

names = ["Elaine", "George", "Jerry", "Cosmo"]

lengths = [len(i) for i in names]

# Not

booleans = [True, False, True]

opposite = [not i for i in booleans]

# same String

names = ["Elaine", "George", "Jerry", "Cosmo"]

is_Jerry = [ True if name == "Jerry" else False for name in names]

nums = [5, -10, 40, 20, 0]

greater_than_two = [True if i > 2 else False for i in nums]

#Nested List

nested_lists = [[4, 8], [15, 16], [23, 42]]

product = [item1 * item2 for (item1, item2) in nested_lists]

# Zip function

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
combine = zip(a, b)

sums = [i + j for (i, j) in combine]

names = ["Jon", "Arya", "Ned"]
ages = [14, 9, 35]

combine = zip(names, ages)
users = ["Name: "+ i+", Age: "+str(j) for (i, j) in combine]