#Your task is to create a Python script that analyzes the records to calculate each of the following:

  # The total number of months included in the dataset

import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
budget_data_csv_path= os.path.join('..', 'Resources', 'budget_data.csv')
with open(budget_data_csv_path) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)
    month=[]
    profit=[]
    profit_change=[]
    total_profit=[]
    monthly_change=[]
    

    #print(f"header: {csv_header}")

    #The total number of months included in the dataset
    for row in csvreader:
      month.append(row[0])
      profit.append(int(row[1]))
    #print(len(month))

    for i in range (len(profit)-1):
      profit_loss= (profit[i+1] - (profit[i]))
      profit_change.append(profit_loss)
    total= sum(profit_change)
    #print(profit_change)
    monthly_change= total/len(profit_change)
   # print(total)
    #The net total amount of "Profit/Losses" over the entire period

    profit_amount= map(int,profit)
    total_profit=(sum(profit_amount))
   # print(total_profit)

    #The average of the changes in "Profit/Losses" over the entire period
    total=(int(total_profit))/len(month)
   # print(total)

    #The greatest increase in profits (date and amount) over the entire period
    profit_increase= max(profit_change)
   # print(profit_increase)
    j = profit_change.index(profit_increase)
    mon_increase= month[j+1]
   # print(mon_increase)

    #The greatest decrease in losses (date and amount) over the entire period
    profit_decrease = min(profit_change)
   # print(profit_decrease)
    p = profit_change.index(profit_decrease)
    mon_decrease= month[p+1]
   # print(mon_decrease)

    print("Financial Analysis")
    print(f'-------------------')
    print("Total Months: " + str(len(month)))
    print("Total: " + "$" + str(int(total_profit)))
    print("Average Change: " + "$" + str(int(total)))
    print("Greatest Increase in Profits: " + str(mon_increase) + " $" + str(int(profit_increase)))
    print("Greatest Decrease in Profits: " + str(mon_decrease) + " $" + str(int(profit_decrease)))

