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