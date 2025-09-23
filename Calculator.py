Option = int(input("Enter Your Option \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Nothing\n."))

match Option:
    case 1:
        print("We Are Going To Perform Addition")
        Num1 = int(input("Enter First Number:- "))
        Num2 = int(input("Enter Second Number:- "))
        Sum = Num1 + Num2
        print("Addition Of Two Numbers:- ",Sum)
    case 2:
        print("We Are Going To Perform Subtraction")
        Num1 = int(input("Enter First Number:- "))
        Num2 = int(input("Enter Second Number:- "))
        Sub = Num1 - Num2
        print("Subtraction Of Two Numbers:- ",Sub)
    case 3:
        print("We Are Going To Perform Multiplication")
        Num1 = int(input("Enter First Number:- "))
        Num2 = int(input("Enter Second Number:- "))
        Mul = Num1 * Num2
        print("Addition Of Two Numbers:- ",Mul)
    case 4:
        print("We Are Going To Perform Division")
        Num1 = int(input("Enter First Number:- "))
        Num2 = int(input("Enter Second Number:- "))
        Div = Num1 / Num2
        print("Addition Of Two Numbers:- ",Div)
    case _:
        print("Invalid Operation")