income = float(input("Enter annual income: ")) # Get user input for annual income
credit_score = int(input("Enter credit score (300-850): ")) # Get user input for credit score

if income < 0 or credit_score < 300 or credit_score > 850:
    print("Invalid input") # Check for invalid input

# Determine risk category based on income and credit score
else:
    if credit_score >= 720 and income >= 60000:
        risk = "Low"
    elif credit_score >= 650 and income >= 40000:
        risk = "Medium"
    else:
        risk = "High"

# Output the risk category
    print("Loan Level Category: " + risk + " Risk")