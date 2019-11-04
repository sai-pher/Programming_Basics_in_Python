rubs = 0

print("rub the lamp 5 times....")

input("....")
rubs += 1
input("{}".format("*rub* " * rubs))

rubs += 1
input("{}".format("*rub* " * rubs))

rubs += 1
input("{}".format("*rub* " * rubs))

rubs += 1
input("{}".format("*rub* " * rubs))

rubs += 1
input("{}".format("*rub* " * rubs))

print("Hi there! I'm the python junior Gini!\n"
      "Your wish is my command!\n"
      "So long as you wish for exactly what i ask you to ah-ha-ha....\n"
      "The good news is though that you get 5 wishes! yay!\n"
      "Let us begin.....")

add_num_1, add_num_2 = eval(input("which two numbers do you WISH to add? (use a comma to separate them): "))
add_res = add_num_1 + add_num_2

print("Your numbers were {} and {}.\n"
      "The answer was......{}".format(add_num_1, add_num_2, add_res))
