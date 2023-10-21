from operator import xor

def not_f(n):
    if n == 0:
        n = 1
    else:
        n = 1
    return n

def fix(n):
    if n > 1:
        n = 1
    return n

for a in range(2):
    for b in range(2):
        for c in range(2):
                print(a,b,c)
                Cout = fix(not_f(fix(not_f(a) * b + a * not_f(b))) * fix(c + not_f(c)) * fix(not_f(a) * b + a * not_f(b)))
                S = not_f( fix(not_f(a) * b + not_f(b) * a) * not_f(c) + (not_f(fix(not_f(a) * b + not_f(b) * a) * c)))
                print(Cout,S)

