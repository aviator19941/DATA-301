# James Ly
# Avinash Sharma
# Purpose : reports the amount of unique names over the years to a file
#           named "question1.txt"
# input file is names1000.csv

#object for baby names
class BabyName:
    def __init__(self, in_name, in_year, in_gender, in_count) :
        self.name = in_name
        self.year = in_year
        self.gender = in_gender
        self.count = in_count


#blank list
namesList = []

#read through whole file
inputFile = open("names1000.csv", 'r')
while True:
    line = inputFile.readline()
    if len(line) == 0:
        break
    data = line.split(',')
    #add data to list
    namesList.append(BabyName(data[1],data[2],data[3],data[4]))

#open file to be written to
outputFile = open("question1.txt", 'w')
outputFile.write("Question 1: Which year has the most unique names?\n\n")
outputFile.write("Results for the amount of unique names over the years\n\n")

yearList = []
#check for unique names
for i in range(0, len(namesList)):
    #separate by year
    if namesList[i].year not in yearList:
        yearNum = namesList[i].year
        yearList.append(yearNum)
        
        #create a list of unique names
        uniqueAmount = []

        #add all unique names that are in the same year
        for j in range(0, len(namesList)):
            if yearNum == namesList[j].year:
                uniqueAmount.append(namesList[j].name)
        outputFile.write(str(yearNum) + ": " + str(len(uniqueAmount)) + " unique names\n")
            
#write total # of names and years in file
outputFile.write("\n")       
outputFile.write("total names in names1000: " + str(len(namesList)) + "\n")
outputFile.write("# of years in names1000: " + str(len(yearList)) + "\n")

#close files
inputFile.close()
outputFile.close()




