# Agho Osabuohiense
# 17th February 2023
# A program that calculates energy and gas bill of customers in diffrennt region in canada
# Constants
MONTHLY_FEE = 120.62
NATURAL_GAS_TRANSACTION_FEE = 1.32
# output
print("Welcome to the Global Energy bill calculator!\t")
# Inputs
input("Enter your account number\t")
input("Enter the month number (e.g., for January, enter 1).\t")
electricity_plan = input("Enter electricity plan (EFIR or EFLR):\t ")
electricity_consumption = float(
    input("Enter electricity consumption in kWh: \t"))
natural_gas_plan = input("Enter natural gas plan (GFIR or GFLR):\t ")
natural_gas_consumption = float(
    input("Enter natural gas consumption in GJ:\t "))
customer_province = input(
    "Enter customer province (AB, BC, MB, NT, NU, QC, SK, YT, ON, NB, NL, NS, PE\t")

# Calculations
electricity_price = 0
if electricity_plan == "EFIR":
    if electricity_consumption <= 1000:
        electricity_price = 8.36 * 0.01 * electricity_consumption
    else:
        electricity_price = ((electricity_consumption - 1000)
                             * 9.41 + (1000 * 8.36)) * 0.01
elif electricity_plan == "EFLR":
    electricity_price = 9.11 * electricity_consumption * 0.01
else:
    print("Invalid electricity plan.")

natural_gas_price = 0
if natural_gas_plan == "GFIR":
    if natural_gas_consumption <= 950:
        natural_gas_price = 4.56 * natural_gas_consumption * 0.01
    else:
        natural_gas_price = ((natural_gas_consumption - 950)
                             * 5.89 + (950 * 4.56)) * 0.01
elif natural_gas_plan == "GFLR":
    natural_gas_price = natural_gas_consumption * 3.93 * 0.01
else:
    print("Invalid natural gas plan.")
total = electricity_price + natural_gas_price + \
    MONTHLY_FEE + NATURAL_GAS_TRANSACTION_FEE

# Sales Tax
sales_tax_rate = 0
if customer_province in ["AB", "BC", "MB", "NT", "NU", "QC", "SK", "YT"]:
    sales_tax_rate = 0.05
elif customer_province == "ON":
    sales_tax_rate = 0.13
elif customer_province in ["NB", "NL", "NS", "PE"]:
    sales_tax_rate = 0.15
else:
    print("Invalid province.")

tax_rate = total * sales_tax_rate

bill = round(total + tax_rate, 2)
# Output
print("Thank you! Your total amount due now is: $", bill)
