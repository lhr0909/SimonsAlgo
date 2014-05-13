def fall(cX, cY, config):
    if len(config) == 0:
        yield {0: {0}}
    elif cY == 0:
        if cX not in config:
            config[cX] = {cY}
        else:
            config[cX].add(cY)
        yield config
    else:
        if cX-1 in config and cY-1 in config[cX-1]:
            if cX+1 in config and cY-1 in config[cX+1]:
                #stuck
                config[cX].add(cY)
                yield config
            else:
                #slide right
                yield fall(cX+1, cY-1, config)
        else:
            if cX+1 in config and cY-1 in config[cX+1]:
                #slide left
                yield fall(cX-1, cY-1, config)
            else:
                #straight down 2
                yield fall(cX, cY-2, config)







def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    T = int(fin.readline())
    for case in xrange(T):
        answer = float(0)
        N, X, Y = map(int, fin.readline().strip().split(' '))
        for config in fall(0, 2, {0: {0}}):
            print config

        print answer
        fout.write(('Case #%d: ' % (case + 1)) + str(answer) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve("B-tiny")
    # solve("B-small-attempt0")
    # solve("B-large")