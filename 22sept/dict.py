#tuple should be in curly braces 
'''
l=(1,2,3,4,5)
print(l)'''

#list should be in square brackets
'''l=[1,2,3,4,5]
print(l)'''


#dict should be in curly braces and in key and value form
'''dict1={"name":"Mayank","age":,"city":"GGN"}
print(dict1)    
print(dict1["name"])
print(dict1["age"])
print(dict1["city"])
dict1["age"]=19
dict1["city"]="Delhi"
print(dict1)
'''

#if and else statment for different conditions u can use elif also for further more conditions
'''a= int(input("Enter a number: "))
b= int(input("Enter another number: "))
if a<b:
    print("a is less than b")
elif a==b:
    print("a is equal to b")
else:
    print("a is not less than b")
#continuing with else if more conditions are there
'''
'''for i in range(6):
    for j in range(7):
        if (i == 0 and j % 3 != 0) or \
           (i == 1 and j % 3 == 0) or \
           (i - j == 2) or \
           (i + j == 8):
            print("*", end=" ") 
        else:
            print(" ", end=" ") 
    print() 
#faltu ka code h ye toh vaise bus isme loops bataye the ye bhi loops hi h but a little harder to learn 
'''

'''total = 0
for i in range(1,6):
    total = total + i
print(total)
'''
#count in given string number of values HW
'''

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
input_string = input("Enter a string: ")
for char in input_string:
    if char.lower() in vowels:
        count += 1
print("Number of vowels in the string:", count)
'''
#homework for counting number of vowels in given string