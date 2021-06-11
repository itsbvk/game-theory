# Code Credits : Anurag Muthyala
# Team Assignment

import numpy

n = int(input())

S = list(map(int, input().split(' ')))
counter = [0 for i in S]
utils = []
n_eq = []
v = []

l = input().split(' ')

def reset_counter():
    global counter
    counter = [0 for i in S]

def update_counter():

    for i in range(n):
        counter[i] += 1
        if counter[i] < S[i]:
            return True
        else:
            counter[i] = 0
    return False

def increment_counter(j):

    for i in range(n):
        if i == j:
            continue
        counter[i] += 1
        if counter[i] < S[i]:
            return True
        else:
            counter[i] = 0
    return False

def index(j, p):
    sum = 0
    if p == 0:
        sum += j
    else:
        sum += counter[0]
    for i in range(1, n):
        if p != i:
            sum += counter[i]*S[i-1]
    if p != 0:
        sum += j*S[p-1]
    return sum

i = 0

while i < len(l):

    u = list()
    j = 1
    while j <= n:
        u.append(int(l[i]))
        i += 1
        j += 1
    utils.append(tuple(u))

def PSNE():

    global S
    global utils

    for i in range(len(utils)):
        d = True
        for j in range(n):
            a = counter[j]
            c = True
            for k in range(S[j]):
                if a != k and utils[index(a,j)][j] < utils[index(k,j)][j]:
                    c = False
                    break
            if not c:
                d = False
                break
        if d:
            n_eq.append([str(i+1) for i in counter])
        update_counter()

def WDSE():

    global S
    global utils
    global v

    for i in range(n):
        reset_counter()
        group_max = -1
        while True:
            max = {0}
            val = utils[index(0,i)][i]
            c = True
            for j in range(1,S[i]):
                if val < utils[index(j,i)][i]:
                    max = {j}
                    val = utils[index(j,i)][i]
                elif val == utils[index(j,i)][i]:
                    max.add(j)
            if group_max == -1:
                group_max = max
                c = increment_counter(i)
            elif group_max.intersection(max) != set():
                group_max.intersection_update(max)
                c = increment_counter(i)
            else:
                c = False
                break
            if not c:
                c = True
                break
        if c:
            group_max = [str(i+1) for i in max]
            v.append(group_max)
        else:
            v = 0
            break

#print(utils)
PSNE()
print(len(n_eq))
for i in range(len(n_eq)):
    print(' '.join(n_eq[i]))
WDSE()
if v == 0:
    for i in range(n):
        print(v)
else:
    for i in range(len(v)):
        s = str(len(v[i]))+" "
        s += ' '.join(v[i])
        print(s)
