#There are various ways to skip with some range in python below are cases of codes of the same.
s = 'MachioPromiseArauna'
list(range(0,len(s),2))
for i in range(0,len(s),2):print(s[i], end=' ')
print('------------------------')
#But there's a more simple way check out case 2.
d = 'MachioIsSoAwesome'
for c in d[::2]:print(c, end=' ')
#We can also code range and for together to give out a well precise code of.
l = [1,2,3,4,5]
for k in range(len(l)):
               l[k] += 3
               print(l)
