# DBSCAN-Clustering-Algorithm
The DBSCAN Clustering Algorithm implemented in Python

This readme file provides you a brief description of the contents of this directory.

--Data:

psrnvsn2_assign5_data

         Input file for DBSCAN algorithm
         
         data_normalized.txt
         
         truth_normalized.txt
         
         data_normalized.arff(arff files in Weka-friendly format)
         
=======
psrnvsn2_assign5_codes

        dbscan.py
        
                Code to implement the dBscan Algorithm
                
                Input files : Dataset File <dFile> , Output File <resultFile>,eps <eps> and minPts <minPoints>
                
                Output file is generated in the "../psrnvsn2_assign3_results/"
                
                Execution : python dbscan.py <dFile> <resultFile> <minPoints> <eps>
                
                Example command : python dbscan.py data_normalized.txt step1.txt 25 0.065
                
        bcubed.py
                Code to implement B-Cubed Evaluation
                
                Input files : ClusterOutputFile and GroundTruthFile
                
                Output : standard output,precision,recall,f1-measure,
                                
                Execution :        python bcubed.py <clusterOutputFile> <truthFile>
                
                Example Usage: python bcubed.py step1.txt truth_normalized.txt
                
        dbScan_Step2.py
        
                Tuned Parameters for dBScan algorithm
                
                Execution : python dbscan_Step2.py
                

=======
psrnvsn2_assign5_results

        step1.txt
        step2a.txt
        step2b.txt
        

