def main():
    intro = (
        "This program takes either a Hexidecimal number or a Decimal number and converts it to Binary.\n"
        "Hex values should include either 0x or # at the beginning.\n"
        "Decimal numbers can be input regularly.\n"
    )
    print(intro)
    print(parse_input())

def parse_input():
    user_input = input("Input your number here : ")
    if user_input.lower().startswith("0x") or user_input.startswith("#"):
        return(convert_inputs(user_input, True))

    else:
        return(convert_inputs(user_input, False))

def convert_inputs(input_to_convert, is_hex):
    if is_hex:
        try:
            converted_input = bin(int(input_to_convert, 16))[2:]
            return ("hex", converted_input)
        except ValueError:
            converted_input = "invalid"
            return("invalid", converted_input)
    else:
        try:
            converted_input = bin(int(input_to_convert, 10))[2:]
            return("decimal", converted_input)
        except ValueError:
            converted_input = "invalid"
            return("invalid", converted_input) 


main()