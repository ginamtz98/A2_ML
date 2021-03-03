#-------------------------------------------------------------------------
# AUTHOR: Gina Martinez
# FILENAME: knn.py
# SPECIFICATION: reads the file binary_points.csv and outputs the LOO-CV error rate for 1NN 
# FOR: CS 4200- Assignment #2
# TIME SPENT: hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import csv
dataSet = ['binary_points.csv']
for ds in dataSet:
    db = []
    X = []
    Y = []
    #reading the data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0: #skipping the header
                db.append(row)

#X = db[['x','y']]
#Y = db['class']

    #loop your data to allow each instance to be your test set
    for i, instance in enumerate(db):

        #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]
        #--> add your Python code here
        # X =
        x = {
            "0": 1,
            "1": 2,
            "2": 3,
            "3": 4,
            "4": 5,
         }

        y = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
        }

        for data in db:
            X.append([x[data[0]], y[data[1]]])

        class_train = {
            "-": 1,
            "+": 2,
        }

        for data in db:
            Y.append(class_train[data[2]])

        X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.1)

    #x = {
     #   0, 1, 2, 3, 4,
    #}

    # = {
    #    1, 2, 3, 4, 5,
    #}

        for data in db:
            X_train.append([x[data[0]], y[data[1]]])


        #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]
        #--> add your Python code here
        # Y =
    # class_train = {
        #    "-": 1,
        #   "+": 2,
        #}

        for data in db:
            Y_train.append(class_train[data[2]])

        #store the test sample of this iteration in the vector testSample
        #--> add your Python code here
        #testSample =
        for data in db:
            X_test.append([x[data[0]], y[data[1]]])
            Y_test.append(class_train[data[2]])


        #fitting the knn to the data
        clf = KNeighborsClassifier(n_neighbors=1, p=2)
        clf = clf.fit(X, Y)

        #use your test sample in this iteration to make the class prediction. For instance:
        #class_predicted = clf.predict([[1, 2]])[0]
        #--> add your Python code here
        #class_predicted = clf.predict(X_test)
        #compare the prediction with the true label of the test instance to start calculating the error rate.
        #--> add your Python code here
        accuracy_score = clf.score(X_test, Y_test)
        error_rate = 1 - accuracy_score

    #print the error rate
    #--> add your Python code here
    print(accuracy_score)
    print(error_rate)


