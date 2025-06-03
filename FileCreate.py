with open("Machio.txt", "w") as f:
    f.write("My name is Machio Promise Arauna.\n")
    f.write('An aspiriant programmer and a web designer.\n')
    f.write('Just entered the world of programming under Mr Miruka as my mentor.\n')
    f.write('Learning Python and Java meanwhile with great skills in debbuging and code writing and skilled in Githubbing.\n')
    f.write('Anyways, pleasure to start it up and straighten the path to success\n')
    f.close()
print('----------------------------------------')
with open("Machio.txt", "r") as f:
    print(f.read())
