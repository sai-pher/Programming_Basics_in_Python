intro_prompt = "Welcome to the CALCULATOR!.....NATOR!"  # Variable holding prompt to use the intro.
command_prompt = "Enter a command [add/exit]: "
control = "no"

print(intro_prompt)
while control != "yes":  # While loop based on user updated logical condition.
    print("The calculator-nator is active")  # Some code to be run on each iteration.
    """
    An input based logical control structure
    """
    command = input(command_prompt)  # Variable to hold user command input

    # 'if' based logical control structure
    if command == "add":
        x = int(input("x: "))
        y = int(input("y: "))
        print("{} + {} = {}".format(x, y, x + y))  # Code to run if command 'add' is given.
    elif command == "exit":
        print("Input command was 'exit' ")  # Code to run if command 'exit' is given.
        control = "yes"
    else:
        print("Invalid input")  # Code to run if no or an unknown command is given.
