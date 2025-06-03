#Comments are the simplest form of documentation using docstring we can code coments.
#Checking on dir()
print(dir([]))
print('---------------------------------------------------------------')
print(dir(''))
print('---------------------------------------------------------------')
print(dir(str))
print('---------------------------------------------------------------')
print(dir())
#So in short dir() returns lists of attributes of an object. It's like a memory jogger it gives you the attribures but don't tell you what they mean.
#2. checking on docstring()
def greet(name):
    """ This is a python documentation on PEP
"""
    name = "Machio Promise Arauna"
    return f"Hello {name}!"
print(greet.__doc__)
print('----------------------------------------------------------------')
help(greet)
