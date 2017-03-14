def week_1(file_input, feature_output, aa_output):
# W is the window size
    aa_dict = {"A":"10000000000000000000", "C":"01000000000000000000", "D":"00100000000000000000", "E":"00010000000000000000", "F":"00001000000000000000", "G":"00000100000000000000","H":"00000010000000000000", "I":"00000001000000000000", "K":"00000000100000000000", "L":"00000000010000000000", "M":"00000000001000000000", "N":"00000000000100000000", "P":"00000000000100000000", "Q":"00000000000001000000", "R":"00000000000000100000", "S":"00000000000000010000", "T":"00000000000000001000", "V":"00000000000000000100", "W":"00000000000000000010", "Y":"00000000000000000001"}

    with open(file_input, "r") as f_in:
        f1 = f_in.readlines()
        f2= open(feature_output,"w")
        fea_line = 2
        while fea_line < len(f1):
            for i in f1[fea_line]:
                if i == "B":
                    f2.write("0" + "\n")
                elif i == "E":
                    f2.write("1" + "\n")
            fea_line += 3
        f2.close()
    with open (feature_output,"r") as f2o:
        f2o_line = f2o.readlines()
        BE_list = []
        for p in range(len(f2o_line)):
            BE_list.append(f2o_line[p])
        print ("length of BE_list is", len(BE_list))
    for w in range (1,2):
        with open(file_input, "r") as f_in:
            f1 = f_in.readlines()
            f3= open(aa_output,"w")
            for aa_line in range(1, len(f1), 3):
                f3.write("00000000000000000000"*int(w/2))
                for item in f1[aa_line].strip():
                    f3.write(aa_dict[str(item)])
                f3.write("00000000000000000000"*int(w/2) + "\n")
            f3.close()

        #print (len(f2o))
        aa_list = []
        with open(aa_output) as f:
            for line in f:
                for i in range(0, len(line)- w*20, 20):
                    aa_list.append(line[i: i+w*20])


        aa_outsidelist = []
        for item in aa_list:
            aa_insidelist = []
            for number in range(len(item)):
            #print(item[number])
                aa_insidelist.append(item[number])
            aa_outsidelist.append(aa_insidelist)
    #print (aa_outsidelist)
        print ("length of aa_outsidelist is", len(aa_outsidelist))
        #from sklearn import svm
        #import numpy as np
        #from sklearn.model_selection import cross_val_score

        #clf = svm.SVC(kernel='rbf', C=1, random_state=314)
        #clf.fit(aa_outsidelist, BE_list)
        #scores = cross_val_score(clf, aa_outsidelist, BE_list, cv=5)
        #print (w)
        #print (scores)
        #print ("Accuracy: %0.7f(+/- %0.6f)" %(scores.mean(), scores.std() * 2))

week_1("buried_exposed_beta.3line.txt", "BE.txt", "aa.txt")


