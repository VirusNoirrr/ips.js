# fr ngl
import random
nvm = open("bytecode.txt").read()
def dyal(k):
    return chr((k & 4294967232) | (k * 39 & 63))
def tbh(v, u):
    O = ""
    L = v[u[0]]
    u[0] += 1
    n = 0
    
    for n in range(L):
        k = v[u[0]]
        u[0] += 1
        O += dyal(k)
        n += 1
    
    return O
def ngl(v, u, f):
    a = len(u)
    r = a - f
    t = []
    M = 0

    while M < len(v):
        h = 0
        l = 1
        while True:
            x = u.index(v[M])
            M += 1
            h += l * (x % f)
            
            if x < f:
                t.append(int(h))
                break
            
            h += f * l
            l *= r

    return t
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
nvm = ngl(nvm, chars, 50)
btw = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=28))
jk = nvm[len(nvm)+btw.find(".")] ^ len(nvm) + 4
sigmaData = nvm[jk:jk+nvm[jk+1]+2]
print(tbh(sigmaData, [1]))
