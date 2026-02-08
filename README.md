# Assignment 2: Conditionals

## Exercise 1: Customer Discount Eligibility

### Description:

This program calculates the discount applied to a customer’s purchase based on their membership status and purchase amount.

### Features:

* Accepts purchase amount and membership status as user input
* Validates purchase amount to prevent negative values
* Applies correct discount rules using conditional statements
* Calculates and displays the final price after discount

### How the Program Works:

1. Prompts the user to enter a purchase amount.
2. Prompts the user to specify whether they are a member.
3. Checks for invalid purchase amounts.
4. Determines the discount percentage based on membership status and purchase amount.
5. Calculates and displays the discount percentage and final price.

### Sample Run:

**Input:**

```
Enter purchase amount: 150
Are you a member? (yes/no): yes
```

**Output:**

```
Discount applied: 15.0%
Final price: $127.5
```

---

## Exercise 2: Employee Performance Bonus

### Description:

This program determines an employee’s annual bonus based on their performance score.

### Features:

* Accepts annual salary and performance score as input
* Validates the performance score range (0–100)
* Uses conditional logic to assign bonus percentages
* Calculates and displays the bonus percentage and bonus amount

### How the Program Works:

1. Prompts the user to enter their annual salary.
2. Prompts the user to enter their performance score.
3. Validates that the performance score is within the acceptable range.
4. Determines the bonus percentage using if / elif / else statements.
5. Calculates and displays the bonus percentage and bonus amount.

### Sample Run:

**Input:**

```
Enter annual salary: 65000
Enter performance score (0-100): 85
```

**Output:**

```
Performance Bonus: 10.0%
Bonus Amount: $6500.0
```

---

## Exercise 3: Loan Risk Classification

### Description:

This program classifies loan applicants into risk categories based on their credit score and annual income.

### Features:

* Accepts credit score and annual income as input
* Validates input ranges for credit score and income
* Uses logical operators and conditional statements to classify risk
* Displays the loan risk category

### How the Program Works:

1. Prompts the user to enter their annual income.
2. Prompts the user to enter their credit score.
3. Validates that income is non-negative and credit score is within range.
4. Evaluates risk level using predefined criteria.
5. Displays the loan risk category.

### Sample Run:

**Input:**

```
Enter annual income: 50000
Enter credit score (300-850): 680
```

**Output:**

```
Loan Level Category: Medium Risk
```