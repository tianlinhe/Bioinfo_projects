from sklearn.datasets import load_svmlight_file
from sklearn.ensemble import RandomForestClassifier

testdata = load_svmlight_file("svml_win13.txt")
clf = RandomForestClassifier(n_estimators=25, random_state=314)
clf.fit(testdata[0], testdata[1])

#query = "ACDD"
query = input("Please type the query sequence here (in CAPITAL letter):")

aa_dict = {"A":0, "C":1, "D":2, "E":3, "F":4, "G":5,"H":6, "I":7, "K":8, "L":9, "M":10, "N":11, "P":12, "Q":13, "R":14, "S":15, "T":16, "V":17, "W":18, "Y":19, "U":20}
query_plus = "U"*6 + str(query) + "U"*6
query_plus = query_plus.replace(" ", "")
import numpy as np
outside_list = []
for cycle in range(0,len(query_plus)-12):
    inside_list = []
    zero_list = np.zeros((13,21))
    for win in range(0,13):
        zero_list[win][aa_dict[query_plus[win+cycle]]] = 1.0
    inside_list.append(zero_list.reshape([1,273]))
    outside_list.append(inside_list)
input_list = np.array(outside_list)
final_input = []
for item in input_list:
    final_input.append(item[0][0])

import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)



test = clf2.predict(np.array(final_input))
prediction = []
for item in test:
    if item == 1:
        prediction.append("B")
    elif item == -1:
        prediction.append("E")
print ("Predicted state is: " + "".join(prediction))
