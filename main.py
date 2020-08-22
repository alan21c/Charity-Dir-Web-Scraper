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
	
# finished program
print("main.py finished running")
input()
