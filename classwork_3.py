# Write a function that calculates EMI on a loan.

def calculate_emi(principal, rate, time):
    r = rate / 12
    n = time

    # Calculate EMI using the formula
    emi = principal * r * (pow(1 + r, n)) / (pow(1 + r, n) - 1)

    return emi

# Example usage:
principal_amount = 1000
annual_interest_rate = 0.08  # Replace with the actual annual interest rate
loan_tenure_months = 60

emi_amount = calculate_emi(principal_amount, annual_interest_rate, loan_tenure_months)
print(f"EMI Amount: {emi_amount:.2f} INR")
