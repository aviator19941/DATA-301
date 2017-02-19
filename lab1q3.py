# James Ly
# Avinash Sharma
# Purpose : reports the count of baby names with "Emma" throughout the years
#           to a text file named "question3.txt"
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
outputFile = open("question3.txt", 'w')
outputFile.write("Question 3: How does the popularity of Emma change over the years?\n\n")
outputFile.write("Results for popularity of Emma over the years\n\n")

yearList = []
#check for instances of "Emma" in each year
for i in range(0, len(namesList)):
    #separate by year
    if namesList[i].year not in yearList:
        yearNum = namesList[i].year
        yearList.append(yearNum)

        #check if baby name is "Emma"
        for j in range(0, len(namesList)):
            if (namesList[j].name == 'Emma') and (namesList[j].year == yearNum):
                outputFile.write(str(yearNum) + " count: " + str(namesList[j].count))

#close files
inputFile.close()
outputFile.close()

                    
