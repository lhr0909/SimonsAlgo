#A module for calling Maple commands

from subprocess import Popen, PIPE

class Maple:
    maple = None
    
    def __init__(self):
        self.maple = Popen(['maple', '-t', '-u', '-q'], stdin=PIPE, stdout=PIPE, stderr=None, close_fds=True)
    
    def __del__(self):
        self.maple.terminate()
        
    def run(self, command):
        #run commands whose outputs have been supressed with colons
        self.maple.stdin.write(command + ':\n')
        
    def execute(self, command):
        #add EndofLine as an indicator for maple.stdin
        #there is a deadlock issue when calling maple.stdout.readline() too much
        #always remember that you need a semicolon or colon after every command
        self.maple.stdin.write(command + ';EndofLine;\n')
        t = ""
        t = self.maple.stdout.readline().strip()
        k = self.maple.stdout.readline().strip()
        while k !='EndofLine':
            t += k
            k = self.maple.stdout.readline().strip()
        return t

#some Maple Commands that can be called
def openNumTheory(maple):
    maple.run('with(numtheory)')

def divisors(maple, n):
    #before use this, remember to call openNumTheory first
    t = maple.execute('divisors(%d)' % n)
    t = t.replace('{', '[').replace('}', ']').replace('\n', '')
    return eval(t)
    
def primeFactors(maple, n):
    pf = eval(maple.execute('ifactors(%d)' % n))[1]
    factors = []
    for item in pf:
        for i in xrange(item[1]):
            factors.append(item[0])
    return factors

def totient(maple, n):
    #before use this, remember to call openNumTheory first
    return int(maple.execute('phi(%d)' % n))
    
def nextPrime(maple, n):
    return int(maple.execute('nextprime(%d)' % n))