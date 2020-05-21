# Contains letter

contains_a = lambda my_input: True if "a" in my_input else False

print contains_a("banana")
print contains_a("apple")
print contains_a("cherry")

ends_in_a = lambda str: True if str[-1] == "a" else False

print ends_in_a("data")
print ends_in_a("aardvark")

double_or_zero = lambda num: num*2 if num > 10 else 0
print double_or_zero(15)
print double_or_zero(5)

multiple_of_three = lambda num: "multiple of three" if num%3==0 else "not a multiple" 
print multiple_of_three(9)
print multiple_of_three(10)

import random

add_random = lambda num: num+random.randint(1,10)
print add_random(5)
print add_random(100)