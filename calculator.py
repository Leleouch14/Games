def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

opp = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}
def calc():
    from logo_calc import logo
    print(logo)
    num1 = float(input("Enter first number: "))
    conti = True
    while conti:
        for i in opp:
            print(i)
        operation = input("Select operation: ")
        num2 = float(input("Enter second number: "))
        result = opp[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result} \n \ndo you wish to continue with {result}: press y \n or start a new calculation: press n \n press q to quit")
        choice = input("\ny/n/q: ")
        if choice == "y":
            num1 = result
        elif choice == "n":
            conti = False
            calc()
        else:
            print("\nGoodbye \n:3 ")
            break
calc()
