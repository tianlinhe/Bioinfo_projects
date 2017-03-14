# Bioinfo_projects
The python file"pssm_to_svm(v3).py": 
a. Iterates over the pssm files generated from multiple sequence alignments of all sequences in the dataset 
b. Converts them to svm.light format so that they can be interpreted by predictor
   - The frequency of each amino acid is normalized so that it is always between 0 and 1
   - For class label, "B"(buried) is regarded as +1 while "E"(exposed) is regarded as -1
c. Enables a flexible reading frame by changing the window size at the command line at the bottom
d. The window size used here is 13. By seting win = 13, a file name "svml_win13.txt" will be generated

The python file "final_predictor.py":
a. Using load_svm_light_file, it takes up "svml_win13.txt" as training set
b. Random forrest classifier is used, with no.estimator set as 35
c. It is equiped with a simple user-iterative surface: When a user types in an amino acid query sequence (must be capitalized), it returns the 2-state prediction of the query sequence. Otherwise, it can also be done through directly typing the query sequence on line 8 of the script inside the quotation marks.

The text files ending with "pssm":
Those are pssm files generated from psi-blast of the my entire dataset aganist uniref50.

The text file "Buried_exposed_beta.3line.txt":
It is the raw data obtained from teacher with
   - header
   - amino acid sequence
   - two-state labels "B"(buried) and "E"exposed
