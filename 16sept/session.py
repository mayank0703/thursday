'''def display_expense_records(records):
  for i in range(0,4):
    category = 50
    amount = 15
    date = 11
    d= category, amount, date
    print(d)
'''
'''
def display_expense_records(records):
  for record in records:
    category = record.get('category', 'N/A')
    amount = record.get('amount', 'N/A')
    date = record.get('date', 'N/A')
    print(f"Category: {category}, Amount: {amount}, Date: {date}")'''
def display_expense_records(records):
    # Print the exact heading required by the instructions
    print("No Category Amount Date")
    
    # Set the starting record number
    count = 1
    
    for item in records:
        # Split the single text line and instantly name the 3 pieces
        category, amount, date = item.split()
        
        # Turn the amount text into a decimal number
        amount = float(amount)
        
        # Print the formatted line with the count and 2 decimal places (.2f)
        print(f"{count} {category} {amount:.2f} {date}")
        
        # Increase the record number for the next loop
        count = count + 1