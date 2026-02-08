income = float(input("Enter annual income: "))
credit_score = int(input("Enter credit score (300-850): "))

if income < 0 or credit_score < 300 or credit_score > 850:
    print("Invalid input")

else:
    if credit_score >= 720 and income >= 60000:
        risk = "Low"
    elif credit_score >= 650 and income >= 40000:
        risk = "Medium"
    else:
        risk = "High"

    print("Risk Level Category: " + risk + " Risk")