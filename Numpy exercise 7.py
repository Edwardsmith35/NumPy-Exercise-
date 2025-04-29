# Mini Project: 1D Slicing and Indexing with NumPy

## Objective

#In this mini-project, you will practice 1D slicing and indexing techniques using NumPy. We'll work on a dataset that represents monthly sales data for a retail store and perform various data manipulation tasks.

## Dataset

#Let's assume we have a 1D NumPy array that represents the monthly sales for a retail store for one year, in thousands of dollars.



import numpy as np

monthly_sales = np.array([200, 220, 250, 275, 300, 320, 350, 370, 400, 420, 450, 475])


## Tasks

### Task 1: Basic Indexing

#1. Access and print the sales data for January (the first month).
#2. Access and print the sales data for December (the last month).
print(monthly_sales[0])
print(monthly_sales[-1])

print("Q1 Sales ",monthly_sales[0:3])
print("Q2 Sales ",monthly_sales[3:6])
print("Q3 Sales ",monthly_sales[6:9])
print("Q4 Sales ",monthly_sales[9:12])

### Task 3: Modify Sales Data

#1. Assume that there was an error in the data entry for the month of April. The correct sales figure is $280,000. Update this value in the array.
#2. Print the updated array to confirm the change

monthly_sales[3] = 280
print(monthly_sales)

#### Task 4: Summer Sales

#1. Extract and print the sales data for the summer months (June, July, August).
#2. Calculate and print the average sales for the summer months.
Summer_sales = monthly_sales[4:7]
print(Summer_sales)
Avg_summer = np.mean(Summer_sales)
print(Avg_summer)

### Task 5: Above Average Months

#1. Calculate the average monthly sales for the entire year.
#2. Identify and print the months where the sales were above average.

Avg = np.mean(monthly_sales)
Above_average_binary = monthly_sales > Avg
Months = np.array(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])

#Two Methods to solve this, the first is better:
print("Months with above average sales: ")
for i in range(len(Months)):
    if Above_average_binary[i]:
       print(f"{Months[i]}: {monthly_sales[i]}")
       
#Or: 
print("Months with above average sales: ")
for month, sale, state in zip(Months, monthly_sales, Above_average_binary):
    if state:
      print(f"{month} {sale}")






