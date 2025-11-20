def main():
    print("This is the main function")
    print(parse_input())

def parse_input():
    user_input = input("Input either a hex or decimal value here")
    if user_input.lower().startswith("0x") or user_input.startswith("#"):
        try:
            converted_input = int(user_input, 16)
            return ("hex", converted_input)
        except ValueError:
            converted_input = "invalid"
            return("invalid", converted_input)

    try:
        converted_input = int(user_input, 10)
        return("decimal", converted_input)
    except ValueError:
        converted_input = "invalid"
        return("invalid", converted_input) 

main()