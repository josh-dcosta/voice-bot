class TablePrinter:
    def PrintTable(self,Num1,Multiple1) :
        for x in range(1, int(Multiple1)+1):
            print(Num1, "*", x, "=", int(Num1) * int(x))
