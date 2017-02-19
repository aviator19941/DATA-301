# James Ly
# Avinash Sharma
# Purpose : reports number of male and female births in each year
#           to a file named "question2.txt"
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
outputFile = open("question2.txt", 'w')
outputFile.write("Question 2: How did the number of births change over the years for males and females?\n\n")
outputFile.write("Results for number of male and female births over the years\n\n")

yearList = []
#sum up number of births in each year
for i in range(0, len(namesList)):

    #separate by year
    if namesList[i].year not in yearList:
        yearNum = namesList[i].year
        yearList.append(yearNum)
        maleList = []
        femaleList = []

        #separate by male or female
        #into male or female lists
        for j in range(0, len(namesList)):
            if yearNum == namesList[j].year:
                if namesList[j].gender == 'M':
                    maleList.append(namesList[j])
                else:
                    femaleList.append(namesList[j])

        #add up all the male counts      
        if len(maleList) > 0:
            maleSum = 0
            for x in range(1, len(maleList)): 
                item = maleList[x].count
                item.replace("\n", "")
                maleSum += int(item)

            outputFile.write(str(yearNum) + " m: " + str(maleSum))

        #add up all the female counts      
        if len(femaleList) > 0:
            femaleSum = 0
            for x in range(1, len(femaleList)):
                item = femaleList[x].count
                item.replace("\n","")
                femaleSum += int(item)
            
            outputFile.write(" f: " + str(femaleSum) + "\n")
                
#close files
inputFile.close()
outputFile.close()
