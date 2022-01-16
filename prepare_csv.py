#All 2021 data was very big, I downloaded it to my local pc and combined them in to one .csv file with a python script. 
#Checked for duplicates, there was none. 
#In total there are: 5595064 rows Then .csv file is uploaded to kaggle. 


import csv
from zipfile import ZipFile
import os
import sys
import glob
import pandas as pd


#unzip the csv files 
#Directory where raw data is
dir_name = 'C:\\Users\\bakig\\OneDrive\\Desktop\\CaseStudy\\RawData'
extension = ".zip"
extensioncsv="csv"
os.chdir(dir_name) # change directory from working one to raw data directory
def unzip_files():
    for item in os.listdir(dir_name): # loop through items in directory
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = ZipFile(file_name) # create zipfile object
            zip_ref.extractall(dir_name) # extract file to dir
            zip_ref.close() # close file

def combine_csv_files():
    all_filenames = [i for i in glob.glob('*.{}'.format(extensioncsv))]
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

def lines_in_combined_csv():
    file = open("combined_csv.csv")
    reader = csv.reader(file)
    lines= len(list(reader))
    print(lines)

def find_duplicates():
    df_state=pd.read_csv("combined_csv.csv")
    Dup_Rows = df_state[df_state.duplicated()]
    print("\n\nDuplicate Rows : \n {}".format(Dup_Rows))


# step 1 : 
unzip_files()

#step 2:
combine_csv_files()

#step 3:
lines_in_combined_csv()
# result= 5595064

#step 4:
find_duplicates()
#no duplicate found -rideid is unique










