# banking/loan.py - Loan EMI calculation
def calculate_emi(principal, rate_per_annum, months):
    """Calculate monthly EMI using standard formula."""
    r = rate_per_annum / (12 * 100)
    if r == 0:
        return principal / months
    emi = principal * r * (1 + r)**months / ((1 + r)**months - 1)
    return round(emi, 2)

def total_payment(emi, months):
    return round(emi * months, 2)
