# -------------------------------------------------------------------------
# AUTHOR: Gina Martinez
# FILENAME: decision_tree.py
# SPECIFICATION: trains, tests, and outputs the performance of the models created by using each training set on the test set provided
# FOR: CS 4200- Assignment #2
# TIME SPENT: 2 days
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)
                #print(row)

    # transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here
    # X =
    age = {
        "Young": 1,
        "Presbyopic": 2,
        "Prepresbyopic": 3,
    }

    spectacle = {
        "Myope": 1,
        "Hypermetrope": 2,
    }

    astigmatism = {
        "Yes": 1,
        "No": 2,
    }

    tear = {
        "Normal": 1,
        "Reduced": 2,
    }

    for data in dbTraining:
        X.append([age[data[0]], spectacle[data[1]], astigmatism[data[2]], tear[data[3]]])

    # transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    # --> add your Python code here
    # Y =

    lenses = {
        "Yes": 1,
        "No": 2,
    }

    for data in dbTraining:
        Y.append(lenses[data[4]])

    # loop your training and test tasks 10 times here
    for i in range(10):

        # fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)

        # read the test data and add this data to dbTest
        # --> add your Python code here
        # dbTest =

        dbTest = ['contact_lens_test.csv']
        for dt in dbTest:
            dbTesting = []
            XTest = []
            YTest = []

            with open(dt, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for j, row in enumerate(reader):
                    if j > 0:  # skipping the header
                        dbTesting.append(row)
                        #print(row)
            age = {
                "Young": 1,
                "Presbyopic": 2,
                "Prepresbyopic": 3,
            }

            spectacle = {
                "Myope": 1,
                "Hypermetrope": 2,
            }

            astigmatism = {
                "Yes": 1,
                "No": 2,
            }

            tear = {
                "Normal": 1,
                "Reduced": 2,
            }

            for dataTest in dbTesting:
                XTest.append([age[dataTest[0]], spectacle[dataTest[1]], astigmatism[dataTest[2]], tear[dataTest[3]]])

            lenses = {
                "Yes": 1,
                "No": 2,
            }

            for dataTest in dbTesting:
                YTest.append(lenses[dataTest[4]])
            # transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
            # class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            # --> add your Python code here

            for data in dbTest:
                class_predicted = clf.predict(XTest)

            # compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            # --> add your Python code here
                #print("final accuracy when training on contact_lens_training_1.csv: ")
                print(clf.score(XTest, YTest))

            # find the lowest accuracy of this model during the 10 runs (training and test set)
            # --> add your Python code here

    # print the lowest accuracy of this model during the 10 runs (training and test set).
    # your output should be something like that:
    # final accuracy when training on contact_lens_training_1.csv: 0.2
    # final accuracy when training on contact_lens_training_2.csv: 0.3
    # final accuracy when training on contact_lens_training_3.csv: 0.4
    # --> add your Python code here

