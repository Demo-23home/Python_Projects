def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")


def sub(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}")


def mul(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer}")


def div(a, b):
    answer = a / b
    print(f"{a} / {b} = {answer}")


def get_num():
    a = int(input("enter the first number"))
    b = int(input("enter the second number"))
    return a, b


while True:
    choice = input(
        """
        choose the opreation:
        A.Addition
        B.Subtraction
        c.Multiplication
        d.Division
        
    """
    ).upper()
    a, b = get_num()
    if choice == "A":
        add(a, b)

    if choice == "B":
        sub(a, b)

    if choice == "C":
        mul(a, b)

    if choice == "D":
        div(a, b)
    again = input("do you want to do math again ? y/n ")
    if again == "n":
        break
