TAX_PERCENTAGE = 5


def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def calculate_tax(gross_salary, tax_percentage):
    return gross_salary * tax_percentage / 100


def calculate_net_salary(gross_salary, tax):
    return gross_salary - tax


def read_amount(prompt):
    """Keep asking until the user enters a valid non-negative number."""
    while True:
        text = input(prompt)
        try:
            value = float(text)
        except ValueError:
            print("Invalid input: please enter a number.")
            continue
        if value < 0:
            print("Invalid input: amount cannot be negative.")
            continue
        return value


def main():
    employee_name = input("Enter employee name: ")
    basic_salary = read_amount("Enter basic salary: ")
    allowance = read_amount("Enter allowance: ")

    gross_salary = calculate_gross_salary(basic_salary, allowance)
    tax = calculate_tax(gross_salary, TAX_PERCENTAGE)
    net_salary = calculate_net_salary(gross_salary, tax)

    print(f"Employee: {employee_name}")
    print(f"Basic Salary: {basic_salary:.2f}")
    print(f"Allowance: {allowance:.2f}")
    print(f"Gross Salary: {gross_salary:.2f}")
    print(f"Tax (5%): {tax:.2f}")
    print(f"Net Salary: {net_salary:.2f}")


main()