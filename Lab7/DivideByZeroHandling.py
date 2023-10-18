#64050037
def main():
    continue_loop = True  # Determines if more input is needed
    while continue_loop:
        try:
            numerator = int(input("Please enter an integer numerator: "))
            denominator = int(input("Please enter an integer denominator: "))
            result = quotient(numerator, denominator)
            print(f"\nResult: {numerator} / {denominator} = {result}")
            continue_loop = False  # Input successful; end looping
        except ValueError:
            input()  # Discard input so the user can try again
            print("You must enter integers. Please try again.\n")
        except ZeroDivisionError:
            print("Zero is an invalid denominator. Please try again.\n")

def quotient(numerator, denominator):
    if denominator == 0:
        raise ArithmeticError("Zero is an invalid denominator")
    return numerator / denominator

if __name__ == "__main__":
    main()
