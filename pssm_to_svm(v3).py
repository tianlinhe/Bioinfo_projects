# convert pssm to svmlight in multiple sliding window (successful now!!!)
#this one can be corrected read by svmlight!!!  :)
def pssm_to_svm(win, file_input, svml_output):
    with open(file_input, "r") as f_0:
        f0 = f_0.readlines()
        seq_list = []
        for i in range(0,len(f0),3):
            seq_list.append(" ".join(f0[i:i+3]))
        seq_list.sort()
        label_list = []
        for item in seq_list:
            label_list.append(item.split()[2])
        label = "".join(label_list)
#it is important to convert label from a big string to list with individual labels, so that they can be read
        labellist = []
        for item in label:
            if item == "B":
                labellist.append(int(1))
            elif item == "E":
                labellist.append(int(-1))

    svml_outsidelist = []
    import os
    for filename in os.listdir(os.getcwd()):
        if filename.endswith ("pssm"):#if True:
            with open (filename, "r") as f:
                f1 = f.readlines()
                outside_list = []
                for i in range (3, len(f1)-6):

                    inside_list = f1[i].split()[22:42]
                    #print (inside_list)
                    inside_list.append('0')

                    outside_list.append(inside_list)
                paddling= ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0','0','0','100']*int(win/2)
                outside_list.append(paddling)

                outsidelist =['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0','0','0','100']*int(win/2)
                for item in outside_list:
                    outsidelist += item

                #print (len(outsidelist))

                for i in range (0, len(f1)-9):
                    svmlinsidelist = []
                    for b in range(21*win):
                        svmlinsidelist.append(str(b) + str(":") + str(float(outsidelist[21*i+b])/100))
                    svml_outsidelist.append(svmlinsidelist)


    #print (svml_outsidelist)
    print (len(svml_outsidelist))
    print (len(labellist))
    with open(svml_output, "w") as f2:
            for i in range(len(labellist)):
                f2.write(str(labellist[i]) + " " + str(" ".join(svml_outsidelist[i])) + "\n")

pssm_to_svm(13, "buried_exposed_beta.3line.txt","svml_win13.txt")
