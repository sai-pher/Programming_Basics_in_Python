"""
An input based control loop
"""
control_prompt = "End loop? [yes/no]: "  # Variable holding prompt to use for control loop conditional update.
control = input(control_prompt)  # Variable to hold user input used for control loop conditional update.

while control != "yes":  # While loop based on user updated logical condition.
    print("This loop is still active")  # Some code to be run on each iteration.
    control = input(control_prompt)  # Statement to update control loop conditional variable.

"""
An input based logical control structure
"""
command_prompt = "Enter a command [a/b/c/d]: "
command = input(command_prompt)  # Variable to hold user command input

# 'if' based logical control structure
if command == "a":
    print("Input command was 'a' ")  # Code to run if command 'a' is given.
elif command == "b":
    print("Input command was 'b' ")  # Code to run if command 'a' is given.
elif command == "c":
    print("Input command was 'c' ")  # Code to run if command 'a' is given.
elif command == "d":
    print("Input command was 'd' ")  # Code to run if command 'a' is given.
else:
    print("Invalid input")  # Code to run if no or an unknown command is given.
