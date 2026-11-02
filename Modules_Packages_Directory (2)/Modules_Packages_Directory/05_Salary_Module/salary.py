# Module: salary.py - Salary calculations

def gross_salary(basic, hra_pct=0.40, da_pct=0.20):
    """Calculate gross salary."""
    hra = basic * hra_pct
    da  = basic * da_pct
    return basic + hra + da

def deductions(gross, pf_pct=0.12, tax_pct=0.10):
    """Calculate total deductions."""
    pf  = gross * pf_pct
    tax = gross * tax_pct
    return pf + tax

def net_salary(basic):
    """Calculate net salary after deductions."""
    gross = gross_salary(basic)
    total_deductions = deductions(gross)
    return gross - total_deductions
