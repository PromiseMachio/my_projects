#Create a for loop to output the ASCII of a string.
Names = "Machio Promise Arauna"
for s in Names:
    print(f"Character: {s} = ASCII: {ord(s)}")

#Print out the sumof all the ASCII char in the above loop
print('-------------------------------------------')
ascii_sum = 0
for s in Names:
    ascii_sum += ord(s)

print("The sum of ASCII codes:",ascii_sum)
#Modify the codes to bring a list of ASCII codes.
print('-------------------------------------------')
ascii_code =[]
for s in Names:
    ascii_code.append(ord(s))

print(ascii_code)

#For enumerating the code too.
for index, s in enumerate(Names):
    print(f"{index}: Character: {s} -> ASCII: {ord(s)}")
