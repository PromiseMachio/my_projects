print("Name and location infomation.".upper())
User_details = {'Name:':'Machio','Age:':20,'Nationality:':'Kenya'}
for key in User_details.keys():
    print(key, User_details[key])

print('---------------------------------')
print("Educational Infomation About you.".upper())
User_info = {"School":"The Cooperative Uni of Kenya","Course":"Bachelors in Statistics and Information Technology","Year of Study":3.1}
I = iter(User_info)
print(next(I))
print(next(I))
print(next(I))
#This has been quite clear as one can see using the manual method in dictionaries in iteration of DIctionaries will not work well as compared to using key and value in for loop method.
