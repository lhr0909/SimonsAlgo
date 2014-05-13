romans = open('089.txt', 'r').read().strip().split('\r\n')

origin = 0
final = 0

for roman in romans:
    origin += len(roman)
    short = roman
    short = short.replace('DCCCC', 'CM')
    short = short.replace('CCCC', 'CD')
    short = short.replace('LXXXX', 'XC')
    short = short.replace('XXXX', 'XL')
    short = short.replace('VIIII', 'IX')
    short = short.replace('IIII', 'IV')
    final += len(short)
print origin - final

#safer method
'''
numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
for roman in romans:
    i = 0
    value = 0
    origin += len(roman)
    while i < len(roman):
        if roman[i] == 'M':
            value += 1000
        elif roman[i] == 'D':
            value += 500
        elif roman[i] == 'C':
            if i+1 < len(roman):
                if roman[i+1] == 'D':
                    value += 500 - 100
                    i += 1
                elif roman[i+1] == 'M':
                    value += 1000 - 100
                    i += 1
                else:
                    value += 100
            else:
                value += 100
        elif roman[i] == 'L':
            value += 50
        elif roman[i] == 'X':
            if i+1 < len(roman):
                if roman[i+1] == 'L':
                    value += 50 - 10
                    i += 1
                elif roman[i+1] == 'C':
                    value += 100 - 10
                    i += 1
                else:
                    value += 10
            else:
                value += 10
        elif roman[i] == 'V':
            value += 5
        elif roman[i] == 'I':
            if i+1 < len(roman):
                if roman[i+1] == 'V':
                    value += 5 - 1
                    i += 1
                elif roman[i+1] == 'X':
                    value += 10 - 1
                    i += 1
                else:
                    value += 1
            else:
                value += 1
        i += 1
    k = value
    short = ""
    i = 0
    for i in xrange(len(values)):
        while k >= values[i]:
            short += numerals[i]
            k -= values[i]
    final += len(short)
    #print roman, short, value
#print origin
#print final
print origin - final
'''