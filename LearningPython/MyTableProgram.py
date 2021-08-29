import MyTableModule as tbl
print("This program prints the multiplication table of 2's.")

Num1 = input("Enter a number : ")
Multiple1 = input("Enter a multiple : ")

tblPrinter = tbl.TablePrinter()
tblPrinter.PrintTable(int(Num1),int(Multiple1))

   