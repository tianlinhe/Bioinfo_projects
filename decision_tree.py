from sklearn.datasets import load_svmlight_file
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

import os
for filename in os.listdir(os.getcwd()):
    if filename.startswith ("svml_win13"):#if True:
        testdata = load_svmlight_file(filename)
        clf = DecisionTreeClassifier(random_state=314)
        #clf = RandomForestClassifier(n_estimators=35, random_state=314)
        clf.fit(testdata[0], testdata[1])
        scores = cross_val_score(clf, testdata[0], testdata[1], cv=5)
        print(filename)
        print (scores)
        print ("Accuracy: %0.7f(+/- %0.6f)" %(scores.mean(), scores.std() * 2))
