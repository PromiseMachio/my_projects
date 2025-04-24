#There are several examples of FOR statements
#Ex1
numbers = [12, 13, 4, 23, 71, 18, 9 ,10]# Create a list
#For instance we want to find even numbers
for n in numbers:
    if n %2 == 0:
        print("The following are even numbers:", n)


#Now you can still find odd numbers from the same code.
for n in numbers:
    if n %2 != 0:
        print("The following are odd numbers:", n)

print("-------------------------------------------------")
#Ex 2.
word = 'communication'
vowel = 'aeiou'
vowel_count = 0

for w in word:
    for w in vowel:
        vowel_count += 1
        print(f"The word has {vowel_count} of vowels")# This code specifially deals with the giving the number of vowels in the word.

print("-------------------------------------------------")
#Ex 3.
#In this example we are to build several things with the help of FOR.
#Building a list
scores = [4, 3, 6, 7, 9, 10]
square = []
for s in scores:
    square.append(s**2)
    print("Squares:", square)

#Building strings
Name = "Promise"
reversed_name  = " "
for letter in name:
    reversed_name = letter + reversed_name:
    print(reversed_name)# In this example there was creation of a new string.
#Building the sum and maybe finding there mean
results= [20,30,50,90,40,60,70]
#In summation we assign an empty value to total
total =0
for r in results:
    total += r
    print(results)
#Now find the mean now that you have the total
#To avoid error messages
ages = [12,14,17,18,19,21,25]
total = 0
count = 0
for a in ages:
    total += ages:
    count += 1:
    mean = total/count
    print(mean)
print("-------------------------------------------------")

#Ex 4.
#In this example we want to find the maximum value without using max()
bullets = [120, 567, 127, 983, 777, 567, 907, 124]
max_value = [0]
for b in bullets:
    if b > max > bullets:
        max_value = b
        print(max_value)
