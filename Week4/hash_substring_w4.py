import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def PolyHash(S,p,x):
    hash = 0
    for i in reversed(S):
        hash = (hash*x+ord(i)) % p
    return hash

# H ← array of length |T| − |P| + 1
# S ← T[|T| − |P|..|T| − 1]
# H[|T| − |P|] ← PolyHash(S, p, x)
# y ← 1
# for i from 1 to |P|:
# y ← (y × x) mod p
# for i from |T| − |P| − 1 down to 0:
# H[i] ← (xH[i + 1] + T[i] − yT[i + |P|]) mod p
# return H

def PrecomputeHashes(text,pattern,p,x):
    T = len(text)
    P = len(pattern)
    H = [0]*(T-P+1)
    S = text[-P:]
    H[T-P] = PolyHash(S,p,x)
    y = 1
    for i in range(1,P+1):
        y = (y*x) % p
    for i in reversed(range(0,T-P)):
        temp = (x*H[i+1]+ord(text[i])-y*ord(text[i+P]))
        while (temp < 0):
            temp += p
        H[i] = temp % p
    return H

# p ← big prime, x ← random(1, p − 1)
# result ← empty list
# pHash ← PolyHash(P, p, x)
# H ← PrecomputeHashes(T, |P|, p, x)
# for i from 0 to |T| − |P|:
# if pHash ̸= H[i]:
# continue
# if AreEqual(T[i..i + |P| − 1], P):
# result.Append(i)
# return result

def RabinKarp(pattern,text):
    p = 1000000007
    x = random.randint(1, p)
    result = []
    pHash = PolyHash(pattern,p,x)
    H = PrecomputeHashes(text,pattern,p,x)
    for i in range(len(text)-len(pattern)+1):
        if (pHash == H[i]) and (text[i:i+len(pattern)] == pattern):
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(RabinKarp(*read_input()))