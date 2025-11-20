def main():
    intro = (
        "This program takes either a Hexidecimal number or a Decimal number and converts it to Binary.\n"
        "Hex values should include either 0x or # at the beginning.\n"
        "Decimal numbers can be input regularly.\n"
    )

    print(intro)

    while True:
        # This will run the parse_input() function 
        # and set the return values to result_type and result_value
        result_type, result_value = parse_input()

        # If the result is invalid and the input was not correct
        # the user will be asked for another input
        if result_type != "invalid":
            print(f"\nYour original value was {result_type} and converts {result_value} in Binary. ")
            break
        else:
            print("\nPlease input a valid value to be converted.\n")


def parse_input():
    # Gets the user's input. It should be either hex or decimal
    user_input = input("Input your number here : ")

    # The if statement is checking if the input is hexidecimal or not
    # hex should start with either "0x" or "#"
    if user_input.lower().startswith("0x"):
        # will call the function that converts the actual inputs, in this case hex is True
        return(convert_inputs(user_input, True))
    if user_input.startswith("#"):
        return(convert_inputs(user_input[1:], True))

    else:
        return(convert_inputs(user_input, False))

def convert_inputs(input_to_convert, is_hex):
    # When this function is called it is passed either True or False for is_hex
    if is_hex:
        try: # if unable to convert the input to binary it will throw an exception
            converted_input = bin(int(input_to_convert, 16))[2:] # the [2:] removes the 0b python adds
            return ("Hexidecimal", converted_input)
        except ValueError: # this is the exception, will force user to input another value
            converted_input = "invalid"
            return("invalid", converted_input)

    else:
        try:
            converted_input = bin(int(input_to_convert, 10))[2:]
            return("Decimal", converted_input)
        except ValueError:
            converted_input = "invalid"
            return("invalid", converted_input) 

# this will simply run the main() function
main()