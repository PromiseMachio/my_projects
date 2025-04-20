Python 3.10.12 (main, Nov  6 2024, 20:22:13) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = ['cats','hen','monkeys','parrots']
for i in range(len(a)):
    print(i, a[i])
>>> ... ... 
0 cats
1 hen
2 monkeys
3 parrots
>>> 
#for instance want to determine even numbers
for numbers in range(0,21):
    if numbers% 2==0:
        print(f"{numbers}is even")
    
>>> >>> ... ...   File "<stdin>", line 3
    print(f{numbers}"is even")
          ^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> >>> #for instance want to determine even numbers
for numbers in range(0,21):
    if numbers% 2==0:
        print(f"{numbers}is even")
    
>>> ... ... ... ... 
0is even
2is even
4is even
6is even
8is even
10is even
12is even
14is even
16is even
18is even
20is even
>>> #Here lets say we are sorting names with their first letters.
names = ['Promy','Derick','Angela','Paul','Peter','Benta','Agnes']
for name in names:
    if name.Startswith("P"):
        print(f"{name} starts with letter P in the beginning")
        
>>> >>> ... ... ... ... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'str' object has no attribute 'Startswith'. Did you mean: 'startswith'?
>>> print("------------------------------------------------------------------")
#Here lets say we are sorting names with their first letters.
names = ['Promy','Derick','Angela','Paul','Peter','Benta','Agnes']
for name in names:
    if name.startswith("P"):
        print(f"{name} starts with letter P in the beginning")
        
------------------------------------------------------------------
>>> >>> >>> ... ... ... ... 
Promy starts with letter P in the beginning
Paul starts with letter P in the beginning
Peter starts with letter P in the beginning
>>> 