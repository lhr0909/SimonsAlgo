def solve():
    i = 1
    min = 2000000
    absMin = 0
    while True:
        j = 1
        while j <= i:
            '''
            count = 0
            for row in xrange(i):
                for col in xrange(j):
                    count += (i - row) * (j - col)
            '''
            #or directly use a formula (Super speed-up):
            #  Since each rectangle formed on the grid is made up
            #  of two vertical lines and two horizontal lines.
            #  As there are (i+1 choose 2) = i * (i+1) / 2 ways
            #  of picking two vertical lines, and, similarly, 
            #  j * (j+1) / 2 ways of picking two horizontal
            #  lines. Hence, there are i * (i+1) * j * (j+1) / 4
            #  rectangles on a (i by j) rectangular grid.
            count = i * (i+1) * j * (j+1) / 4
            absMin = abs(2000000 - count)
            if absMin < min:
                min = absMin
                strDimension = "%d x %d" % (i, j)
                printStr = "Dimension = %s, " % strDimension
                printStr += "Rectangle Count = %d, " % count
                printStr += "Area = %d" % (i * j)
                #print printStr
                #I don't know this limit until I run this program infinitely
                if min == 2: return (i * j)
            j += 1
        i += 1
        
print solve()