from gmpy import mpf
x = 1
y = 1
s = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
k = 2
gr = mpf(1.6180339887498948482045868343656381)
gr_1 = 1 - gr
gs = gr * gr
gs_1 = gr_1 * gr_1
sqrt5 = mpf(2.23606797749978969640917366873)
print gr, gs, gr_1, gs_1, (gs - gs_1) / sqrt5

while True:
    k += 1
    gr = gs + gr
    gr_1 = gs_1 + gr_1
    x = (x + y) % 1000000000
    if set(str(x)) == s:
        f = str(int((gr - gr_1) / sqrt5))[:9]
        print "candidate", k, x, f
        if set(f) == s:            
            print k
            break
    k += 1
    gs = gr + gs
    gs_1 = gr_1 + gs_1
    y = (x + y) % 1000000000
    if set(str(y)) == s:
        f = str(int((gs - gs_1) / sqrt5))[:9]
        print "candidate", k, y, f
        if set(f) == s:            
            print k
            break

