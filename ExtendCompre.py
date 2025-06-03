#This codes will show how to comprehened file contents and add if clauses in the syntax.
with open("DicIterators.py") as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in ("DicIterators.py") if line[0] == 'p']
    print(lines)
