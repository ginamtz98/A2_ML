#-------------------------------------------------------------------------
# AUTHOR: Gina Martinez
# FILENAME: naive_bayes.py
# SPECIFICATION: reads the file weather_training.csv(training set) and outputs the classification of each test instance from the
#file weather_test(test set) if the classification confidence is >= .75
# FOR: CS 4200- Assignment #2
# TIME SPENT: hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
import csv

dataSet = ['weather_training.csv']

for ds in dataSet:
    dbTraining = []
    X = []
    Y = []

#reading the training data
#--> add your Python code here
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)

#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =

    outlook = {
        "Sunny": 1,
        "Overcast": 2,
        "Rain": 3,
    }

    temperature = {
        "Hot": 1,
        "Mild": 2,
        "Cool": 3,
    }

    humidity = {
        "Normal": 1,
        "High": 2,
    }

    wind = {
        "Weak": 1,
        "Strong": 2,
    }

    for data in dbTraining:
        X.append([outlook[data[0]], temperature[data[1]], humidity[data[2]], wind[data[3]]])
#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
    playTennis = {
        "Yes": 1,
        "No": 2,
    }

    for data in dbTraining:
        Y.append(playTennis[data[4]])

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
dbTest = ['weather_test.csv']
for dt in dbTest:
    dbTesting = []
    XTest = []
    YTest = []

    with open(dt, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for j, row in enumerate(reader):
            if j > 0:  # skipping the header
                dbTesting.append(row)
    outlook = {
        "Sunny": 1,
        "Overcast": 2,
        "Rain": 3,
    }

    temperature = {
        "Hot": 1,
        "Mild": 2,
        "Cool": 3,
    }

    humidity = {
        "Normal": 1,
        "High": 2,
    }

    wind = {
        "Weak": 1,
        "Strong": 2,
    }

    for data in dbTesting:
        XTest.append([outlook[data[0]], temperature[data[1]], humidity[data[2]], wind[data[3]]])


#printing the header os the solution
    print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
    for data in dbTest:
        class_predicted = clf.predict(XTest)
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]


