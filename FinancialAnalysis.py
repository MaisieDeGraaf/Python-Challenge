import os
import csv

csv_path = r'Resources\budget_data.csv'


change_in_profits = []
dates = []
profitsloss = []


with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        dates.append (row[0])
        total_dates = len(dates)
        profitsloss.append (row[1])
    for i in range(len(profitsloss)-1):
        change_in_profits.append(int(profitsloss[i+1])-int(profitsloss[i]))

        total = 0
        for i in profitsloss:
            total += int(i)
            
    maximum_average = change_in_profits[0]
    for maximum in change_in_profits:
        if maximum > maximum_average:
            maximum_average = maximum
            
    minimum_average = change_in_profits[0]
    for minimum in change_in_profits:
        if minimum < minimum_average:
            minimum_average = minimum

print("Financial Analysis")
print('-------------------------------')
print(f"Total Months: {total_dates}")
print(f"Total: ${total}")
print(f"Average Change: ${round(sum(change_in_profits)/len(change_in_profits), 2)}")
print(f"Greatest Increase in Profits: {dates[change_in_profits.index(maximum_average) + 1]} (${maximum_average})")
print(f"Greatest Decrease in Profits: {dates[change_in_profits.index(minimum_average) + 1]} (${minimum_average})")


with open('Financial_Ouptut.txt', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Financial Analysis'])
    writer.writerow(['--------------------------'])
    writer.writerow([f"Total Months: {total_dates}"])
    writer.writerow([f"Total: ${total}"])
    writer.writerow([f"Average Change: ${round(sum(change_in_profits)/len(change_in_profits), 2)}"])
    writer.writerow([f"Greatest Increase in Profits: {dates[change_in_profits.index(maximum_average) + 1]} (${maximum_average})"])
    writer.writerow([f"Greatest Decrease in Profits: {dates[change_in_profits.index(minimum_average) + 1]} (${minimum_average})"])





        

