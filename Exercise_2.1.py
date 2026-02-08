amount = float(input("Enter purchase amount: "))
membership = input("Are you a member? (yes/no): ").strip().lower()
if amount < 0: 
    print("Invalid amount")

else:
    if membership == 'yes':
        if amount < 100:
            discount_per = 0.05
        else:
            discount_per = 0.15
    else:
        if amount >= 150:
            discount_per = 0.1
        else:
            discount_per = 0.00

    final_amount = amount * (1 - discount_per)
    print("Discount applied: " + str(discount_per * 100) + "%")
    print("Final price: $" + str(final_amount))