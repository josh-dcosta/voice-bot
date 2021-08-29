class Calculator:
    def __init__(self, Num1, Num2): 
        self.Num1 = Num1
        self.Num2 = Num2

    def AddTwoNumbers(self):
        return int(self.Num1) + int(self.Num2)

    def SubTwoNumbers(self):
        return int(self.Num1) - int(self.Num2)

    def CounterTwoNumbers():
        if int(self.Num1)<int(self.Num2):
            for x in range(int(self.Num1), int(self.Num2), 1):
                print(x)
        else:
            for x in range(int(self.Num1), int(self.Num2), -1):
                print(x)

def PrintArray(Arg1):
    print(f"The length of array {Arg1} = " + str(len(Arg1)))
