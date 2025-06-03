L = [1,2,3,4,5]
for x in range(len(L)):
    
    L[x]+=  10
    print(L)

print('---------------------------')
A = [2,3,4,5,6]
k = [x + 10 for x in A]
print(k)

print('---------------------------')
p = [11,12,13,14,15]
res = []
for i in p:
    res.append(i + 10)
    print(res)
