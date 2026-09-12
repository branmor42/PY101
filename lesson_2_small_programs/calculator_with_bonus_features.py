# X Ask the user for the first number.
# X Ask the user for the second number.
# X Ask the user for an operation to perform.
# X Perform the operation on the two numbers.
# X Print the result to the terminal.
"""A simple calculator program."""

def repeat(response):
    if response == "yes":
        return True
    else:
        return False

go_again = "yes"
counter = 0

while repeat(go_again):

    def prompt(message):
        """Display a formatted prompt message."""
        print(f'==> {message}')

    def invalid_number(number_str):
        """Does something...."""
        try:
            float(number_str)
        except ValueError:
            return True

        return False

    if counter < 1:
        prompt('Welcome to Calculator!')

    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()

    prompt("What's the second number?")
    number2 = input()


    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
        number2 = input()

    prompt('What operation would you like to perform?\n'
        '1) Add 2) Subtract 3) Multiply 4) Divide')
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()

    match operation:
        case '1':   # '1' represents addition
            output = float(number1) + float(number2)
        case '2': # '2' represents subtraction
            output = float(number1) - float(number2)
        case '3': # '3' represents multiplication
            output = float(number1) * float(number2)
        case '4': # '4' represents division
            output = float(number1) / float(number2)

    prompt(f'The result is: {output}')
    prompt(f'Would you like to perform another calculation? (type "yes" if so)')
    go_again = input()
    counter += 1