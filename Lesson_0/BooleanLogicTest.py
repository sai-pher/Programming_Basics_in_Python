a_1, a_2 = 1, 2

a_i = a_1 <= a_2
print("a i: {}".format(a_i))

a_1, a_2 = 2, 2

a_ii = a_1 <= a_2
print("a ii: {}".format(a_ii))

b_1, b_2 = 4, 2

b_i = (b_1 + b_2) * 3 > b_2 + (2 * b_1)
print("b i: {}".format(b_i))

b_1, b_2 = "4", "2"

b_ii = (b_1 + b_2) * 3 > b_2 + (2 * b_1)
print("b ii: {}".format(b_ii))

b_1, b_2 = 2, 4

b_iii = (b_1 + b_2) * 3 > b_2 + (2 * b_1)
print("b iii: {}".format(b_iii))
