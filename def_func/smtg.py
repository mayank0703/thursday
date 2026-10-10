'''def process_expense_menu(commands):
    category_amount = []
    for command in commands:
        if command == "ADD":
            category_amount.append(command)
    print(category_amount)
    return category_amount'''
'''
a=[13,22,73,24,51]
a.sort()
print(a[-1])'''
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    out=[[n,arr]]
    out.sort()
    print(out[-2])
    '''

'''a = input(": ")
print(type(a))
a = int(a)
print(type(a))
'''
'''
name = input("Enter your name: ")
DOB = input("Enter your date of birth (YYYY-MM-DD): ")
DOY = DOB[0:4]
age = 2026 - int(DOY) 
print(f"Hello {name}, you will be {age} years old in 2026.")'''
'''
vowels = ['a', 'e', 'i', 'o', 'u']
name = input("Enter your name: ")
vowel_count = 0
for char in name.lower():
    if char in vowels:
        vowel_count += 1
print(f"Hello {name}, you have {vowel_count} vowels in your name.")'''
'''
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list3 = dict(zip(list1, list2))
print(list3, type(list3))'''
'''
c = [1, 2, 3, 4, 5]
b = list(filter(lambda x: x % 2 == 0, c))
print(b)'''
'''
c = [1, 2, 3, 4, 5]
b = [b for b in c if b % 2 == 0]
print(b)'''

b = (1, 1, 2, 3, 4, 5, 5)
repeated_values = set()
num_counts = 0
# Find the repeated values
for i in b:
    if b.count(i) > 1:
        repeated_values.add(i)
        num_counts += 1
        num_counts = num_counts - len(repeated_values)  
# Update the count to the number of unique repeated values
# Check if we found any and print the result
if repeated_values:
    for val in repeated_values:
        print(tuple([val]), end=" ")
    print(f"Number of repeated values: {num_counts}")
else:
    print("no repeated values")