import os 
import csv

st1 = "total months: "

totalmonth = 0
totalrevenue = 0
RevenueChange = []
date=[]

def mean(numbers):
   return float(sum(numbers)) / max(len(numbers), 1)

BankData = os.path.join("data","budget_data_1.csv")
outputTXT = os.path.join("data", "solution1.txt")
with open(BankData, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")

   next(csvreader, None)

   for row in csvreader:
       date.append(row[0])
       totalmonth = totalmonth + 1
       totalrevenue = totalrevenue + int(row[1])

       if (totalmonth == 1):
           PrRev = int(row[1])
       else:
           Change = (int(row[1]) - int(PrRev))
           RevenueChange.append(Change)
           
       
       PrRev = row[1]
       
   maximum=max(RevenueChange)
   minimum=min(RevenueChange)
   maximum_index=RevenueChange.index(maximum)
   minimum_index=RevenueChange.index(minimum)
   month_max=date[maximum_index +1]
   month_min=date[minimum_index +1]
   print("total months: " + str(totalmonth))
   print("total revenue: " + str(totalrevenue))
   print("average revenue change: " + str(mean(RevenueChange)))
   print("greatest increase in revenue: " + month_max + "(" +str(maximum)+")")
   print("greatest decrease in revenue: " + month_min + "(" +str(minimum)+")")

   with open(outputTXT, 'w',) as textFile:
       textFile.write("financial office")
       textFile.write("\n----------------------------------------")
       textFile.write("\ntotal months = "+ str(totalmonth))
       textFile.write("\ntotal revenue = " +str(totalrevenue))
       textFile.write("\naverage revenue change =" +str(mean(RevenueChange)))
       textFile.write("\ngreatest increase in revenue ="+ month_min + "(" +str(minimum)+ ")")
       textFile.write("\ngreatest decrease in revenue ="+ month_max + "(" +str(maximum)+")")
     