def TaxCalculator(basic_salary,allowance):
    gross_sal = basic_salary + allowance
    if gross_sal > 20000:
        income_tax = gross_sal * 0.3
    elif gross_sal > 10000:
        income_tax = gross_sal * 0.2
    elif gross_sal > 5000:
        income_tax = gross_sal * 0.1
    else:
        income_tax = 0
    net_sal = gross_sal - income_tax

    return gross_sal,income_tax,net_sal

emp_id = input("enter emp id:")
basic_salary = int(input("enter basic salary:"))
allowance = int(input("enter allowance:"))

print('Emp_id : ',emp_id)
print('Basic Salary : ',basic_salary)
print('Allowance : ',allowance)
res = TaxCalculator(basic_salary,allowance)
print('Gross Salary : ',res[0])
print('Income Tax : ',res[1])
print('Net Salary : ',res[2])
