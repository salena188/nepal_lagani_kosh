# Program to calculate total investment from monthly deposits
print("hello")

# Ask user for details
investor_name = input("Enter investor name: ")
monthly_deposit = float(input("Enter monthly deposit amount: "))
years = int(input("Enter number of years: "))

# Initialize total investment
total_investment = 0

# Loop over each year
for year in range(1, years + 1):
    total_investment += monthly_deposit * 12  # 12 months per year
    print(f"Year {year}: Total Investment = {total_investment}")

# Final summary
print(f"\nInvestor {investor_name} will have a total investment of {total_investment} after {years} years.")