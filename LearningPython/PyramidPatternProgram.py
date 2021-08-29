import PyramidModule as pyra
print("This program prints a pattern in the form of a Pyramid.")
MaxRange = input("Please enter the Max Range for the Pyramid = ")
Spacer = int(MaxRange) + 1
PyraPrinter = pyra.PyramidPattern()
PyraPrinter.PyramidPatternPrinter(int(MaxRange), int(Spacer))