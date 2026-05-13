# Ask for project details
project_name = input("Enter the Project Name: ")
days = int(input("Enter the number of Days the project lasted: "))
hours_per_day = float(input("Enter the average Hours worked per day: "))

# Calculate total hours and minutes worked
total_hours = days * hours_per_day
total_minutes = total_hours * 60

# Calculate cost of labor
labor_cost = total_hours * 50.00

# Print summary
print("\n--- Project Summary ---")
print("Project Name:", project_name)
print("Days Worked:", days)
print("Average Hours per Day:", hours_per_day)
print("Total Minutes Worked:", total_minutes)
print("Cost of Labor: $", format(labor_cost, ".2f"))