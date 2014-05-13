sol = 0
for i in range(1, 1001):
    k = ('%04d' % i)[::-1]
    print k[::-1]
    temp = ''
    if k[3]=='1':
        sol = sol + len('one') + len('thousand')
        temp = temp + 'one thousand'
    if k[2]=='1':
        sol = sol + len('one') + len('hundred')
        temp = temp + 'one hundred '
    elif k[2]=='2':
        sol = sol + len('two') + len('hundred')
        temp = temp + 'two hundred '
    elif k[2]=='3':
        sol = sol + len('three') + len('hundred')
        temp = temp + 'three hundred '
    elif k[2]=='4':
        sol = sol + len('four') + len('hundred')
        temp = temp + 'four hundred '
    elif k[2]=='5':
        sol = sol + len('five') + len('hundred')
        temp = temp + 'five hundred '
    elif k[2]=='6':
        sol = sol + len('six') + len('hundred')
        temp = temp + 'six hundred '
    elif k[2]=='7':
        sol = sol + len('seven') + len('hundred')
        temp = temp + 'seven hundred '
    elif k[2]=='8':
        sol = sol + len('eight') + len('hundred')
        temp = temp + 'eight hundred '
    elif k[2]=='9':
        sol = sol + len('nine') + len('hundred')
        temp = temp + 'nine hundred '
    if (k[2]!='0')and((k[1]!='0')or(k[0]!='0')):
        sol = sol + len('and')
        temp = temp + 'and '
    if k[1]=='2':
        sol = sol + len('twenty')
        temp = temp + 'twenty '
    elif k[1]=='3':
        sol = sol + len('thirty')
        temp = temp + 'thirty '
    elif k[1]=='4':
        sol = sol + len('forty')
        temp = temp + 'forty '
    elif k[1]=='5':
        sol = sol + len('fifty')
        temp = temp + 'fifty '
    elif k[1]=='6':
        sol = sol + len('sixty')
        temp = temp + 'sixty '
    elif k[1]=='7':
        sol = sol + len('seventy')
        temp = temp + 'seventy '
    elif k[1]=='8':
        sol = sol + len('eighty')
        temp = temp + 'eighty '
    elif k[1]=='9':
        sol = sol + len('ninety')
        temp = temp + 'ninety '
    if k[1]!='1':
        if k[0]=='1':
            sol = sol + len('one')
            temp = temp + 'one '
        elif k[0]=='2':
            sol = sol + len('two')
            temp = temp + 'two '
        elif k[0]=='3':
            sol = sol + len('three')
            temp = temp + 'three '
        elif k[0]=='4':
            sol = sol + len('four')
            temp = temp + 'four '
        elif k[0]=='5':
            sol = sol + len('five')
            temp = temp + 'five '
        elif k[0]=='6':
            sol = sol + len('six')
            temp = temp + 'six '
        elif k[0]=='7':
            sol = sol + len('seven')
            temp = temp + 'seven '
        elif k[0]=='8':
            sol = sol + len('eight')
            temp = temp + 'eight '
        elif k[0]=='9':
            sol = sol + len('nine')
            temp = temp + 'nine '
    elif k[1]=='1':
        if k[0]=='0':
            sol = sol + len('ten')
            temp = temp + 'ten'
        elif k[0]=='1':
            sol = sol + len('eleven')
            temp = temp + 'eleven'
        elif k[0]=='2':
            sol = sol + len('twelve')
            temp = temp + 'twelve'
        elif k[0]=='3':
            sol = sol + len('thirteen')
            temp = temp + 'thirteen'
        elif k[0]=='4':
            sol = sol + len('fourteen')
            temp = temp + 'fourteen'
        elif k[0]=='5':
            sol = sol + len('fifteen')
            temp = temp + 'fifteen'
        elif k[0]=='6':
            sol = sol + len('sixteen')
            temp = temp + 'sixteen'
        elif k[0]=='7':
            sol = sol + len('seventeen')
            temp  =temp + 'seventeen'
        elif k[0]=='8':
            sol = sol + len('eighteen')
            temp = temp + 'eighteen'
        elif k[0]=='9':
            sol = sol + len('nineteen')
            temp = temp + 'nineteen'
    print temp
    print sol
