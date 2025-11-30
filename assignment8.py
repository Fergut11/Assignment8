import sys

def main():
    intro = (
        "This program takes either a Hexidecimal, Octodecimal, or Decimal number and converts it to Binary.\n"
        "Hex values should include either '0x' or '#' at the beginning. (0-F)\n"
        "Octodecimal numbers should begin with '0o'.(0-7)\n"
        "Decimal numbers can be input regularly.(0-9)\n"
    )

    print(intro)

    while True:
        # This will run the parse_input() function 
        # and set the return values to result_type and result_value
        result_type, result_value = parse_input()

        # If the result is invalid and the input was not correct
        # the user will be asked for another input
        if result_value != "invalid":
            print(f"\nYour original value was {result_type} and converts {result_value} in Binary. ")
            break
        else:
            print(f"\n !!!{result_type}")
            print("\nPlease input a valid value to be converted.\n")


def parse_input():
    # Gets the user's input. It should be either hex or decimal
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = input("Input your number here : ")

    # hex should start with either "0x" or "#"
    # octo is 0o and decimal is regular
    if user_input.lower().startswith("0x"):
        return(convert_inputs(user_input, "hex"))

    elif user_input.startswith("#"):
        return(convert_inputs(user_input[1:], "hex"))

    elif user_input.startswith("0o"):
        return(convert_inputs(user_input, "octo"))

    else:
        return(convert_inputs(user_input, "decimal"))

def convert_inputs(input_to_convert, input_type):
    # When this function is calledc it is passed either True or False for is_hex
    if input_type == "hex":
        try: # if unable to convert the input to binary it will throw an exception
            converted_input = bin(int(input_to_convert, 16))[2:] # the [2:] removes the 0b python adds
            return ("Hexidecimal", converted_input)
        except ValueError: # this is the exception, will force user to input another value
            converted_input = "invalid"
            return("Your input was invalid. Remember Hex digits can only be 0-F.", converted_input)

    elif input_type == "octo":
        try:
            converted_input = bin(int(input_to_convert, 8))[2:]
            return("Octodecimal", converted_input)
        except ValueError:
            converted_input = "invalid"
            return("Your input was invalid. Remember Octo digits can only be 0-7.", converted_input) 

    else: # decimal and all other cases
        try:
            converted_input = bin(int(input_to_convert, 10))[2:]
            return("Decimal", converted_input)
        except ValueError:
            converted_input = "invalid"
            return("Your input was not Hex or Octo so it was either not a number or formatted incorrectly.", converted_input) 
    

# this will simply run the main() function
main()