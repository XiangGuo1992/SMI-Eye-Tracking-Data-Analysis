# SMI-Eye-Tracking-Data-Analysis
Python code for SMI eye tracking data analysis

Code to do data extraction and preprocessing of the Raw .txt data outputed by SMI eye tracking glasses.

## Data structure

In time syncronization.csv table, there is the start and end time for each experiment.

In "1.Raw txt data" folder, there is the Raw .txt data outputed from SMI software.

## 1_extract trials.py
This script is to extract different trials from the the .txt Raw data, and save as .csv files into "2.Exported trials" folder. Delete the useless files in "2.Exported trials", such as "... base 1.csv"

## 2_time sycronization.py
This script collects the start&end time from "time syncronization.csv" and slice the section for each .csv file in "2.Exported trials" and save to "3.Sycronized data" folder.

## 3_Converge subjects result.py
This script will converge the results from the same subject to one .csv file.

## To be done
How to analyze gaze vector, gaze behavior in Aeras-Of_Interests(AOIs).
