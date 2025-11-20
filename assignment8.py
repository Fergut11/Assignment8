def main():
    print("This is the main function")
    print(parse_input())
    print("This is a test for git")

def parse_input():
    user_input = input("Input either a hex or decimal value here")
    if user_input.lower().startswith("0x"):
        return (int(user_input, 16))
    else:
        return(int(user_input))

main()