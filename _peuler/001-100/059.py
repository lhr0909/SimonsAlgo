cipher = map(int, open('059.txt', 'r').read()[:-1].split(','))
f = open('059.out.txt', 'w')

maxSpace = 0
maxCombo = [97,97,97]
for i in xrange(97, 97+26):
    for j in xrange(97, 97+26):
        for k in xrange(97, 97+26):
            key = [i, j, k]
            decryption = []
            for m in xrange(len(cipher)):
                decryption += [cipher[m] ^ key[m%3]]
            n = decryption.count(32)
            if n > maxSpace:
                maxSpace = n
                maxCombo = key
print maxCombo
key = maxCombo
decryption = ""
ans = 0
for m in xrange(len(cipher)):
    decryption += chr(cipher[m] ^ key[m%3])
    ans += cipher[m] ^ key[m%3]
print decryption
print ans

#Somewhat cheating solution:
'''
key = [103, 111, 100]
decryption = ""
ans = 0
for m in xrange(len(cipher)):
    decryption += chr(cipher[m] ^ key[m%3])
    ans += cipher[m] ^ key[m%3]
print decryption
print ans
'''

#use the following code, to generate the file, and check by hand. found out the key is 103, 111, and 100. ("god") (line 4424)
'''
for i in xrange(97, 97+26):
    for j in xrange(97, 97+26):
        for k in xrange(97, 97+26):
            key = [i, j, k]
            decryption = ""
            for m in xrange(len(cipher)):
                decryption += chr(cipher[m] ^ key[m%3])
            f.write(str(i) + ' ' + str(j) + ' ' + str(k) + ' ' + decryption + '\r\n')    
f.close()
'''
