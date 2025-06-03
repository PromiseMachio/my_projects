#Assignment in python is advanced in a way that unlike just the basic form of assignment there're other forms that are a bit advanced. For instance Sequence Assignment
wink = 1
pink = 2
(a,b)= wink,pink
print(a,b)
print('----------------------------')
#Tuple assignment with splitting and with loops in it.
L = [1,2,3,4]
while L:
    front,L = L[0], L[1:]#front gets the first part and [1:] gets the rest.
    print(front,L)#output will be:
                                  # 1 [2, 3, 4]
                                  # 2 [3, 4]
                                  # 4 [4]
                                  # 4 []
