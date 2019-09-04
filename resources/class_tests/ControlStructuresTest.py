"""
=========Control Structures test=========
"""

# What are the final values of the variables used in following loops.
a = 0
while a < -1 or a > 4:
    print("a is {}".format(a))
    a -= 1
    a //= 2
print("1: a final value is {a}\n".format(a=a))

b = a
while b != 15:
    print("b is {}".format(b))
    b += 3
print("2: b final value is {b}\n".format(b=b))

c = b
while c < -1 or c > 4:
    print("c is {}".format(c))
    c -= 1
    c //= 2
print("3: c final value is {c}\n".format(c=c))

d = c
while d != "3" and d > 3:
    print("d is {}".format(d))
    d = "3"
print("4: d final value is {d}\n".format(d=d))

e = str(d * 4)
e_count_1 = 0
for i in e:
    e_count_1 += 1
print("5: e count 1 final value is {ec}".format(ec=e_count_1))

e_count_2 = 0
for i in e * 2:
    if i == "2":
        e_count_2 += 1
print("5: e count 2 final value is {ec}".format(ec=e_count_2))

# Select the correct printed statement for each if/else block.
f = "the quick brown fox"

# Question 6
if f == "fox":
    print("6a: f is fox")
else:
    print("6b: f is not fox")

# Question 7
if "fox" in f:
    print("7a: fox is in f")
else:
    print("7b: fox is not in f")

# Question 8
if "fox" in f and "brown " not in f:
    print("8a: fox is in f and brown is not in f")

elif "fox" in f and "brown " is f:
    print("8b: fox is in f and brown is f")

elif "fox" not in f and "brown " is f:
    print("8c: fox is not in f and brown is f")

elif "fox" in f and "brown " is not f:
    print("8d: fox is in f and brown is not f")

# Question 8: Select a word to exit the guess_1 loop
f += " jumped over the very large dog"
print(f, "\n")

guess_1 = input("Guess a word to break the curse: ")

while guess_1 not in f:
    print("HA-HA-HA! you are stuck with me!")
    guess_1 = input("Guess again")
print("you escaped the curse!")

# Question 9: Select 3 words to exit the guess_2 loop
guess_2 = input("Guess 3 words to escape the curse!\nfirst word?: ")
guessed = ""
count = 0

while (guess_2 not in f) or (count < 3):
    if guess_2 in f and guess_2 not in guessed:
        print("Hm. you've found a word.")
        guessed += " " + guess_2
        count += 1
    else:
        print("HA-HA-HA! Try again!")

    print(count, (guess_2 not in f), (count < 3), (guess_2 not in f) and (count < 3), guessed)
    if count < 3:
        guess_2 = input("\nWhat's your next word?: ")
    else:
        print("You have beaten the curse.")
