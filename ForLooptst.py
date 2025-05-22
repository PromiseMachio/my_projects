#This code wants to try out the for_loop.
#A simple code of the same.
for names in ['machio','promise','arauna']:
    print(names, end=' ')
print('---------------------')
#Example 2 of the same.
sum = 0
for x in [1,2,3,4]:
    sum = sum + x
    print(sum)

print('--------------------')
#Example 3 tuple assignments.
t = [(1,2),(3,4),(5,6)]
for (a,b) in t:
    print(a,b)

print('-------------------')
#Example 3 show iteration in for loops to print both keys in a dictionary.
Names = {'First Name': 'Promise', 'Second Name':'Arauna','Surname':'Machio'}
for key in Names:
    print(key, '=>',Names[key])

print('---------------------------')
#This is the same as the above iteration in the dictionaries.
D = {'a':1, 'b':2, 'c':3}
print(list(D.items()))

for (key,value) in D.items():
    print(key, '=>', value)

print('--------------------------------')
#There's a special way in which python3 helps in assignment of tuples.
for (a,*b,c) in ([1,2,3,4],[5,6,7,8]):
    print(a,b,c)

print('--------------------------------')
#This is the same as the assignment in below.
(a,b,c,d) = (1,2,3,4)
print(a,b,c)
print('--------------------------------')
#Example manual sclicing in for loops.
for all in [(1,2,3,4),(5,6,7,8)]:
    a,b,c = all[0],all[1:3],all[3]
    print(a,b,c)

#Example 4. Lets get a liitle bit sophisticated.Nested for loops.
#Check out this code.
#The code is to check wether items and tests  matches.
#The code contains loop clauses,break too
items = ['aaa', 111, (4,5), 2.1]
tests =[(4,5),3.14]

#Calling both keys and items.
for key in tests:
    for item in items:
        if item ==key:
            print(key, 'Was found')
            break
        else:
            print(key,'Was not found')
"""What you'll notice in this code that the inner loop runs keys all through the items matching them so.This is to be able to find the matches and what ain't matching in the outer loop after the break."""
print('----------------------------------')
#In this example we are going to see a simple example of the above.
items = ['aaa', 111, (4,5), 2.1]
tests =[(4,5),3.14]


#Here we don't call all of them instead we only focus on the one we are to print out.
for key in tests:
    if key in items:
        print(key,'Was found')
    else:
        print(key, 'was not found')

print('-------------------------------------------')
#This is a test code for a for loop to check the enumatation method or rather function.
fruits = ['Apples','Banana']
for index, fruit in enumerate(fruits):
    print(index, fruits)

