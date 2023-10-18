#64050037
def main():
    try:
        fahrenheit = float(input("Please enter degrees in Fahrenheit: "))
        celsius = (5.0 / 9.0) * (fahrenheit - 32)
        print("Fahrenheit is", fahrenheit)
        print("Celsius is", celsius)
    except ValueError as ex:
        print("Your input is not valid:", ex)
    finally:
        print("Finally")

    print("Goodbye")

if __name__ == "__main__":
    main()
