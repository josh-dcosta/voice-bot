class TableCreator:
    def CreateTable(self, Num, MaxMult):
                for x in range(1, int(MaxMult)+1):
                    print(Num, "*", x, "=", int(Num) * int(x))

