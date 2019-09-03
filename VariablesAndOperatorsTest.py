"""
=========Variable and Operator test=========
"""

# 1: what's the value of a?
a = 1
b = 2

a = b
b += 1
print("#1 : a = {a}".format(a=a))  # 2

# 2: what's the value of c?
c = b + a
print("#2 : c = {c}".format(c=c))  # 5

# 3: what's the mathematical notation of d?
d = c ** c  # 5^5
d *= 2  # d = 5^5 * 2
print("#3 : d = {d}".format(d=d))

# 4: what's the value of b?
b = d
b -= d
print("#4 : b = {b}".format(b=b))  # 0

# 5: what are the values of the following e related values? Why?
e = c % a  # 1
e_test_1 = e > a  # F
e_test_2 = e == d  # F
e_test_3 = e - 1 < b ** 2  # F
e_test_4 = e - 1 <= b ** 2  # T
print("#5a: e = {e}\n"
      "#5b: e test 1 = {e1}\n"
      "#5c: e test 2 = {e2}\n"
      "#5d: e test 3 = {e3}\n"
      "#5e: e test 4 = {e4}"
      .format(e=e, e1=e_test_1, e2=e_test_2, e3=e_test_3, e4=e_test_4))

f = "3"
print("\n**BONUS**\n"
      "f = {f}\n"
      "f == 3 = {f1}\n"
      "Explain the answer.".format(f=f, f1=(f == 3)))  # T
