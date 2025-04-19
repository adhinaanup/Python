# Get user input
principal = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = float(input("Enter the rate as a %: "))

# Convert rate to decimal
rate /= 100

# Print table headers
print("\nYear   Starting Balance   Interest   Ending Balance")
print("---------------------------------------------------")

# Initialize balance
balance = principal

# Loop through each year
for year in range(1, years + 1):
    interest = balance * rate  # Calculate interest
    ending_balance = balance + interest  # Compute new balance

    # Print the details for each year
    print(f"{year:<6} {balance:<18.2f} {interest:<10.2f} {ending_balance:<.2f}")

    # Update balance for next year
    balance = ending_balance
# Print final report summary
total_interest = balance - principal
print(f"\nEnding balance: ${balance:.2f}")
print(f"Total interest earned: ${total_interest:.2f}")
