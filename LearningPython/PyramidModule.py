class PyramidPattern:
    def PyramidPatternPrinter(self, MaxRange, Spacer):
        Spacer = int(MaxRange) + 1
        for i in range(0, int(MaxRange)+1, 2):
            if (i > 0):
                print(' '*Spacer + '*' * (i-(i//2)) + str(i) + '*'*(i-(i//2)))
            else:
                print(' '*Spacer + '*')
            
            Spacer = Spacer - 1
