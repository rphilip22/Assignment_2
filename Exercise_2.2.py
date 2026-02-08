salary = float(input("Enter annual salary: "))
per_score = int(input("Enter performance score (0-100): "))

if per_score < 0 or per_score > 100:
    print("Invalid performance score")

else:
    if per_score >= 90:
        bonus_per = 0.20
    elif per_score >= 80:
        bonus_per = 0.10
    elif per_score >= 70:
        bonus_per = 0.05
    else:
        bonus_per = 0.00

    print("Performance Bonus: " + str(bonus_per * 100) + "%")
    print("Bonus Amount: $" + str(salary * bonus_per))