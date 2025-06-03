#Dictionaries are used in mapping objects with keys and their values,
#Case 1.

F = {'Food':'Pizza','Quality':23,'Colour':'Brown'}
print(F['Food'])
F['Quality'] += 10
print(F['Quality'])


print('------------------------')

#The dictionaries can as well start with empty {}
#Case 2
D= {}
#The details to be inserted in the empty dictionary 
D['Name'] = 'Machio Promise'
D['Age'] = 20
D['Occupation'] = 'Programmer'
D['Location'] = 'Busia Kenya'

#Print outputs
print(D.__doc__)
print(D)

print('--------------------------')

#Nested revist in the dictionaries
#Case 3.
MACHIO = {'Name': {'First':'Machio', 'Second':'Promise', 'Third':'Arauna'},
          'Age' : 21,
          'Occupation' : ['Programmer', 'Microsoft'],
          'Location' : ['Kenya', 'Busia', 'Matayos']
          }
#Now you can go ahead and manipulate the dict.
print(MACHIO)
print(MACHIO['Name'])
print(MACHIO['Name']['Second'])
MACHIO['Age'] += 2
print(MACHIO['Age'])
print(MACHIO['Occupation'])
print(MACHIO['Occupation'][-1])
print(MACHIO['Occupation'].append('Director'))
print(MACHIO['Location'].append('Samia'))
print(MACHIO.__doc__)
print(MACHIO)

print('-----------------------------')
MACHIO = 0
print(MACHIO)

print('---------------------------------------')
#Now we sort the dict object first manualy then using the for loops.
#Case 4.1 steps:
#Step one create a dictionary
Patners = { 'FIRST': 'The Mirukas', 'SECOND' : 'The Machios', 'THIRD' : 'The Koulandas', 'FOURTH' : 'The Anderas'}

#Step two create another variable and assign it to be a list of your unordered objects.
Unordered = list(Patners.keys())
 # You can call the list if you fell like
print(Unordered)

#Now create the sorted or rather an ordered version of the Unordered created listt.
Unordered.sort()
# Call the now sorted
print(Unordered)

#Lets us the for loop instead

#Case 4.2
for key in Patners:
    print(key, '=>', Patners[key])

#Now with the sorted in the for loop.
print('-------------------------------------------')
for key in sorted(Patners):
    print(key, '=>', Patners[key])




