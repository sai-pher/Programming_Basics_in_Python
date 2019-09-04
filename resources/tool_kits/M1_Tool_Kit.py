# Statement to take some string input from the user
name = input("What is your name?: ")
age = input("age?: ")

# Statement to print some variable to console
print("welcome: {}".format(name))
print("your age: {}".format(eval(age)))
print("age + 1 = {}".format(eval(age) + 1))

# Multiple assignment from user input.
# Note: eval returns the literal value of the input data.
num_1, num_2 = eval(input("num 1 and num 2?: "))

# statement to print multiple variables to console
print("num 1: {}, num 2: {}".format(num_1, num_2))

# Statement to perform some operation and print the result
#     to console.
ans = num_1 + num_2
print("num 1 + num 2 = {}".format(ans))
