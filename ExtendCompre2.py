with open("DicIterators.py") as f:
    res = []
    for line in open("DicIterators.py"):
        if line[0] == 'p':
            res.append(line.rstrip())
    print(res)
#This code compared to the first I wrote it clarifies and show all lines starting with 'p' in the file opened by the open().
