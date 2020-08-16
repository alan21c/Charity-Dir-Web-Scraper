import csv

# function skeleton to be fleshed out
def arrayToCSV(filename, array):
        f = open(filename, "w")
        for i in range(len(array)):
                for j in range(len(array[i])):
                        f.write(str(array[i][j]))
                        f.write(",")
                f.write("\n")
        f.close()
        return

# test data
sampleArray = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]
arrayToCSV("output.csv", sampleArray)

# sample CSV writing code
with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
	
# finished program
print("main.py finished running")
input()
