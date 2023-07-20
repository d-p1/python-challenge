import os
import csv

#budget = os.path.join("Resources", "budget_data.csv")

budget = r"C:\Users\Diana\Desktop\python-challenge\PyBank\Resources\budget_data.csv"

#PyBank_analysis = os.path.join("analysis", "PyBank_results")
PyBank_analysis = r"C:\Users\Diana\Desktop\python-challenge\PyBank\analysis\PyBank_results.txt"

totalMonths = 0
monthChanges = []
changeValues = []  # Initialize as an empty list
greatestIncrease = ["", 0]
greatestDecrease = ["", 999]
totalProfit = 0

with open(budget) as csvdata:
    csvreader = csv.reader(csvdata)
    budget_header = next(csvreader)

    first_row = next(csvreader)
    totalMonths += 1
    totalProfit += int(first_row[1])
    previousTotal = int(first_row[1])

    for row in csvreader:
        totalMonths += 1
        totalProfit += int(row[1])

        totalChange = int(row[1]) - previousTotal
        previousTotal = int(row[1])
        changeValues.append(totalChange)  # Append to the list
        monthChanges.append(row[0])

        if totalChange > greatestIncrease[1]:
            greatestIncrease[0] = row[0]
            greatestIncrease[1] = totalChange

        if totalChange < greatestDecrease[1]:
            greatestDecrease[0] = row[0]
            greatestDecrease[1] = totalChange

monthlyNet_avg = sum(changeValues) / len(monthChanges)

print(monthlyNet_avg)

# Generate Output Summary
output = (
    f"Analysis:\n"
    f"------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${totalProfit}\n"
    f"Average Change: ${monthlyNet_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(PyBank_analysis, "w") as txt_file:
    txt_file.write(output)

