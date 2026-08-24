from finance_tools.tax import calculate_tax
from finance_tools.loan import calculate_emi


def main():
    try:
        income = float(input("Enter your annual income: "))
        tax_rate = float(input("Enter tax rate (%): "))
        tax = calculate_tax(income, tax_rate)
        print(f"\nTax amount: {tax:.2f}")
        print(f"Income after tax: {income - tax:.2f}")


        principal = float(input("\nEnter loan amount: "))
        annual_rate = float(input("Enter annual interest rate (%): "))
        years = int(input("Enter loan duration (years): "))

        emi = calculate_emi(
            principal,
            annual_rate,
            years
        )

        print(f"\nMonthly EMI: {emi:.2f}")

    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")


if __name__ == "__main__":
    main()