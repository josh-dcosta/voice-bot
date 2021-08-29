import WorkspaceModule as tbl
print("This Program Prints Multiplication Tables.")
Num = int(input("Please enter a number : "))
MaxMult = int(input("Please enter the Max Multiple : "))
tblPrinter = tbl.TableCreator()
tblPrinter.CreateTable(int(Num), int(MaxMult))
