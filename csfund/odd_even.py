
'''a= int(input("Enter a number: "))
if a % 2 == 0:
    print(f"{a} is an even number.")
else:
    print(f"{a} is an odd number.")'''

'''PSEUDO CODES '''

'''
BEGIN
  Read a and b
  IF a > b:
    DISPLAY a is bigger than b
  ELSE IF a < b:
    DISPLAY a is smaller than b
  ELSE:
    DISPLAY a is equal to b
END   
'''

'''
BEGIN
    Read A
    IF A IS GREATER THAN OR EQUAL TO 3.5:
    PRINT ELIGIBLE FOR SCHOLARSHIP
    ELSE:
    PRINT NOT ELIGIBLE FOR SCHOLARSHIP
END
'''
'''
marks= int(input("Enter the marks:-"))
if marks >=90:
    Grade= "grade A"
elif 70 <= marks <= 89:
    Grade = "grade B" 
elif 40 <= marks <= 69:
    Grade = "grade c"
else:
    Grade= "Grade F"
print(Grade)
'''

#exam focused pdf 5th questiojn 100% in exam
'''
BEGIN
    NUMERIC h, amount
    PRINT "Enter number of parking hours:"
    INPUT h
    
    IF h <= 2 THEN
        amount = h * 20
    ELSE IF h <= 5 THEN
        amount = 40 + ((h - 2) * 30)
    ELSE
        amount = 130 + ((h - 5) * 50)  // 40 for first 2 hrs + 90 for next 3 hrs
    END IF
    PRINT "Total parking charge is: Rs.", amount
END'''
'''
h=int(input("Enter the number of hours:-"))
if h <= 2:
    amount = h * 20
elif h <= 5:
    amount = 40 + ((h - 2) * 30)
else:
    amount = 130 + ((h - 5) * 50) 
print("Total parking amount",amount)
'''

