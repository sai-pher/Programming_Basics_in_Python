"""
=========Data Types and I/O test=========
"""

# Q1: what is the result of each of the following lines of code?
print("1a: ", type("What is this?"))
print("1b: ", type(15))
print("1c: ", type("15"))
print("1d: ", type(1.5))
print("1e: ", type(True))
print("1f: ", type("False"))

# Q2
name = "Ero"
age = 12
height = 5.3

# a: what is the order each value will be printed in in the following lines of code
print("2ai  : {}, {}, {}".format(name, age, height))
print("2aii : {}, {}, {}".format(name, age, name))
print("2aiii: {}, {}, {}".format(age, name, age))

# b: if given a number of your choosing, what will the following print statements output?
num_1 = input("Type in a number: ")
print("2bi : {}: {}".format(num_1, type(num_1)))

num_2 = int(input("Type in the same number: "))
print("2bii: {}: {}".format(num_2, type(num_2)))

# c: if given 6.233, what will the following print statement2 output?
num_3 = float(input("Type in a 6.233: "))
print("2ci  : {}: {}".format(num_3, type(num_3)))
print("2cii : {}: {}".format(int(num_3), type(int(num_3))))
print("2ciii: {}: {}".format(str(num_3), type(str(num_3))))

# Bonus!
# a: if given 4.5 as input, what will the following print statement output?
data_1 = eval(input("Type in 4.5: "))
print("B a: {}: {}".format(data_1, type(data_1)))

# b: if given True as input, what will the following print statement output?
data_2 = eval(input("Type in 'True': "))
print("B b: {}: {}".format(data_2, type(data_2)))

# c: if given True, 4.5 as input, what will the following print statement output?
data_3, data_4 = eval(input("Type in 'True, 4.5': "))
print("B c: {}: {}, {}: {}".format(data_3, type(data_3), data_4, type(data_4)))
