# Bioinfo_projects
The text file "Buried_exposed_beta.3line.txt":
It is the raw data obtained from teacher with
   - header
   - amino acid sequence
   - two-state labels "B"(buried) and "E"exposed
   
The python file"pssm_to_svm(v3).py":
1. Iterates over the pssm files generated from multiple sequence alignments of all sequences in the dataset
2. Converts them to svm.light format so that they can be interpreted by predictor
   - The frequency of each amino acid is normalized so that it is always between 0 and 1
   - For class label, "B"(buried) is regarded as +1 while "E"(exposed) is regarded as -1
3. Enables a flexible reading frame by changing the window size at the command line at the bottom\n
4. The window size used here is 13. By seting win = 13, a file name "svml_win13.txt" will be generated

The python file "final_predictor.py":
1. Using load_svm_light_file, it takes up "svml_win13.txt" as training set ("svml_win13.txt" is too large to be uploaded to Github)
2. Random forrest classifier is used, with no.estimator set as 35
3. It is equiped with a simple user-iterative surface: When a user types in an amino acid query sequence (must be capitalized), it returns the 2-state prediction of the query sequence. Otherwise, it can also be done through directly typing the query sequence on line 8 of the script inside the quotation marks.

The python file "week2_wloop.py":
1. It reads the sequences of raw data from "Buried_exposed_beta.3line.txt"
2. It converts the amino acid into binary labels in list
3. It converts "B" to 0 and "E" to 1
4. It loops over window sizes from 1 to 23
5. For each window size, it tests them with linear SVM at cv = 5, and records the accuracy scores for comparison


The text files ending with "pssm":
Those are pssm files generated from psi-blast of the my entire dataset aganist uniref50.


