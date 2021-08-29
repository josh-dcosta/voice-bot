class FibonacciGenerator:
    def GenerateFibonacciNumber(self,MaxRange):
    
        Num1 = 0
        Num2 = 1
        Temp = 0
    
        for i in range(1,int(MaxRange),1):
            print(int(Num1))
            Temp = int(Num1)
            Num1 = int(Num2)
            Num2 = int(Temp)+int(Num2)
 