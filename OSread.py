import os
p = os.popen('dir')
print(p.__next__())
print(p.__next__())
