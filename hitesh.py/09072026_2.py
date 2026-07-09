# This function will be tested by the evaluation system. Do not modify the function name or parameters.
def check_loan_eligibility(age: int, income: float) -> str:
    # Write your code below this line
    # Check age condition first
    if age >= 21:
        # Check income condition if age is valid
        if income >= 25000:
            return "Eligible for loan"
        else:
            return "Not eligible: Income too low"
    else:
        return "Not eligible: Age must be 21 or above"

    pass