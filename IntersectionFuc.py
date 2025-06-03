#create a function called intersection
def intersection(seq1, seq2):
    """ 
>> This intersection seq code returns elements common in both seq1 and seq2.
      .....
>> The code starts on the built-in def <name> (agr1, arg2):
>> The creation of an empty list for storing the element created : res
      ....
>>Then we nest this function using the for clause to iterate the elements in it.
..the for statement : 
                      for <target> in <object>:
... this checks the elements in the seq1 first 
>> Since the elements in seq1 will be compared with those of seq2 no need to break the for nest 
..so using the if statement to check if the elements in seq2 are in seq1 we use the same target (x) in the i statement either. 
>> If found they are added to the empty list res created earlier.
... remember the res will later be called  in the program
>> The return function means the call has just send the message of the function and now the return value if it has commands for this case will return the value.
   ....
printing function to display the function the later on.
    print(intersection([1,2,3,4], [3,5,4,3])

"""
    #Here we are creating an empty list to store the seq generated.
    res = []
    for x in seq1:#This checks objects in 
        if x in seq2:
            res.append(x)
    return res
print(intersection([1,2,3,4,5], [1,6,6,2,3]))
print(intersection.__doc__)
print(help(intersection))
