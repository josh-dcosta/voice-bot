import MyCalculatorModule as calc

print("This program adds two numbers")

Num1 = input("Enter a number from 0-10 : ")
Num2 = input("Enter another number from 0-10 : ")
Arr1 = ["Joshua", "Jiselle"]
Oper = input("Enter which operation (+) or (-) or (c) or (p) you would like to perform) ?")

#Create Object of class
calculator = calc.Calculator(Num1, Num2)

if Oper == "+":
    SumOfTwoNumbers = calculator.AddTwoNumbers()
    print(f"Sum of {Num1}, {Num2} = {SumOfTwoNumbers}")
elif Oper == "-":
    DiffOfTwoNumbers = calculator.SubTwoNumbers()
    print(f"Diff of {Num1}, {Num2} = {DiffOfTwoNumbers}")
elif Oper == "c":
    calculator.CounterTwoNumbers()
elif Oper == "p":
    calc.PrintArray(Arr1)
else:
    print(f"Invalid Operator {Oper}")






