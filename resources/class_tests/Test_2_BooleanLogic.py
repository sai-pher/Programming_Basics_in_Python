"""
=========Boolean Logic test=========
"""

# Q1: what will the following print statements output?
a_1, a_2 = 1, 2

a_i = a_1 <= a_2
print("a i: {}".format(a_i))

a_1, a_2 = 2, 2

a_ii = a_1 <= a_2
print("a ii: {}".format(a_ii))

# Q2: read the following boolean operations. What will they resolve to?
b_1, b_2 = 4, 2

b_i = (b_1 + b_2) * 3 > b_2 + (2 * b_1)
print("b i: {}".format(b_i))

b_1, b_2 = "4", "2"

b_ii = (b_1 + b_2) * 3 < b_2 + (2 * b_1)
print("b ii: {}".format(b_ii))

b_1, b_2 = 2, 4

b_iii = (b_1 + b_2) * 3 == b_2 + (2 * b_1)
print("b iii: {}".format(b_iii))

# Q3: What will be the results of the following statements?
# TODO: C questions using `in`
red, to, is_a, _, c_test = "red", "to", "is a", " ", "The colour red is a primary colour"

c_i = red in c_test
print("c i: {}".format(c_i))

c_ii = red in c_test and to not in c_test
print("c ii: {}".format(c_ii))

c_iii = to in is_a or _ in red
print("c iii: {}".format(c_iii))

c_iv = (red not in c_test) and (_ in c_test or _ in red)
print("c iv: {}".format(c_iv))

c_v = red in to or to in _ or (_ in is_a and _ in c_test)
print("c v: {}".format(c_v))

# TODO: D questions using `is`


# TODO: E questions using multiple combinations (up to 5 subs)
