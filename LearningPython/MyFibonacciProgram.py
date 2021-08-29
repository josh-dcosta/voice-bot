import MyFibonacciModule as fib

print("This program prints the Fibonacci Sequence of numbers to 100.")
MaxNumber = int(input("Enter a number for the amount of numbers in the sequence to be generated : "))

FibGeneratorObject = fib.FibonacciGenerator()
FibGeneratorObject.GenerateFibonacciNumber(MaxNumber)




