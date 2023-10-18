#64050037
class MyException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def func1():
    raise MyException("My Exception")


def func():
    try:
        func1()
    except MyException as e:
        print(e)
        raise e


def main():
    try:
        print("Before Call func")
        func()
        print("After Call func")
    except MyException as e:
        print(e)
    print("Goodbye")


if __name__ == "__main__":
    main()
