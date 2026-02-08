salary = float(input("Enter annual salary: ")) # Get the annual salary from the user
per_score = int(input("Enter performance score (0-100): ")) # Get the performance score from the user

if per_score < 0 or per_score > 100:
    print("Invalid performance score") # Check if the performance score is valid

# Calculate the performance bonus based on the performance score
else:
    if per_score >= 90:
        bonus_per = 0.20
    elif per_score >= 80:
        bonus_per = 0.10
    elif per_score >= 70:
        bonus_per = 0.05
    else:
        bonus_per = 0.00

# Print the performance bonus percentage and the bonus amount
    print("Performance Bonus: " + str(bonus_per * 100) + "%")
    print("Bonus Amount: $" + str(salary * bonus_per))