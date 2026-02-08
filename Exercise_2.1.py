amount = float(input("Enter purchase amount: ")) #input amount from user
membership = input("Are you a member? (yes/no): ").strip().lower() #input membership status from user and convert to lowercase

if amount < 0:
    print("Invalid amount") #check if the amount is negative and print an error message
else:
    discount_per = 0.0 #initialize discount percentage to 0.0

# Determine discount based on membership status and amount
    if membership == 'yes':
        if amount >= 100:
            discount_per = 0.15
        else:
            discount_per = 0.05
    else:
        if amount >= 150:
            discount_per = 0.10

# Calculate final amount after applying discount and print the results
    final_amount = amount * (1 - discount_per)
    print("Discount applied: " + str(discount_per * 100) + "%")
    print("Final price: $" + str(final_amount))