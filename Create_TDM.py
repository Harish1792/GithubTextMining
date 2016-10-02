# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 21:07:49 2015

@author: aditya
"""
#import textmining
from Import_Packages import *
from Process_All_Articles import *
# Store the TermDocumentMatrix function from textmining package in the variable tdm
tdm = textmining.TermDocumentMatrix()

# Now create the TDM. 
# Note tot_text is a collection of Documents after lemmatization  
# relating to each article file in the folder
for text in tot_text:
    tdm.add_doc(text)

# Now the tdm object contains the TDM
# Let's write it to a csv

tdm.write_csv("my_first_tdm.csv")
print "my_first_tdm created" 

# This TDM will be really sparse with lots of zero values. Let's find out how sparse the TDM really is. 
#  Here, we encode all the zeroes in the csv file as NaNs (Missing Value in Python)

tdm_df=pd.read_csv('my_first_tdm.csv', na_values = 0)

# Calculate total number of missing values in the data frame
num_missing = tdm_df.isnull().values.ravel().sum()

# Calculate total number of values in the data frame

tot_values = tdm_df.shape[0]*tdm_df.shape[1]

# Calculate the proportion of missing values
missing_prop = num_missing/float(tot_values)
print missing_prop

# Let's now create a TF-IDF