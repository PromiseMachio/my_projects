with open("Comprehesion.py") as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    print(lines)
print('-----------------------------------------------')
#The above code is quite a comprehension on the code but check out this.
with open("ForLooptst.py") as f:
    lines = [line.rstrip() for line in open("ForLooptst.py")]
    print(lines)
