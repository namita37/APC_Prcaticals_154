def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da


print(gross_salary(30000))
