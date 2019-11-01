import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import random as rand
import math
from cycler import cycler


# read the cv for the project
data = pd.read_csv('sequences_training(1).csv', header = None)
data.columns = ['sequence', 'label']



# test_string = 'CGQGFSVKSDVITHQRTHTGEKLYVCRECGRGFSWKSHLLIHQRIHTGEKPYVCRECGRGFSWQSVLLTHQRTHTG'\
#                 + 'EKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSWQSVLL'\
#                 + 'THQRTHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSRQ'\
#                 + 'SVLLTHQRRHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRG'\
#                 + 'FSNKSHLLRHQRTHTGEKPYVCRECGRGFRDKSHLLSHQRTHTGEKPYVCRECGRGFRDKSNLLSHQRTHTGEKPYVCREC'\
#                 + 'GRGFSWQSVLLRHQRTHTGEKPYVCRECGRGFRDKSNLLSHQRTHTGEKPYVCRECGRGFRNKSHLLRHQRTHTGEKPYVCR'\
#                 + 'ECGRGFSDRSSLCYHQRTHTGEKPYVCREDE'

# shuffle
# data = data.sample(frac=1).reset_index(drop=True)
# data = data.sample(frac=1).reset_index(drop=False)  # Does not drop index


# function to add columns to it
def insert_column (df, name, feature, col_position = 1):
    df.insert (col_position, name, feature)

#function to count specific character count in a string
def count_character(string,character):
    string.count(character)
    # return c_count

# def getMaxOccuringChar(str):
#     # Create array to keep the count of individual characters
#     # Initialize the count array to zero
#     count = [0] * ASCII_SIZE
#
#     # Utility variables
#     max = -1
#     c = ''

# add dna label to list
dnaLabel = list()
dnaLabel = data['label'].tolist()


# add sequence to a list
sequenceLabel = list()
sequenceLabel = data['sequence'].tolist()

#features added
feature_length = list() # count number of characters in a list
max_letter_list = list() # list of the max letter in the list
max_letter_count = list() # list of max num for each row
max_count_ratio = list() # ratio of max number of total number
least_letter_count = list() # least letter number
least_letter_list = list() # least letter description
no_letter_list = list() # list for all
list

#lists of counts of amino acids



alanine_count = list() # count number of alanine in a list (A)
arginine_count = list() # count number of arginine (R)
asparagine_count = list() #count number of asparagine  (N)
aspartic_acid_count = list() # count of asp acid (D)
cysteine_count =list() # count number of cysteine in a list (C)
glutamine_count = list() # count number of glutamine (Q)
glutamic_count = list() # count of glutaimic (E)
glycine_count = list() # count of glycine (G)
histidine_count = list() # (H)
isoleucine_count = list() #(I)
leucine_count = list() # (L)
lysine_count = list() # (K)
methionine_count = list() # (M)
phenylalanine_count = list() # (F)
proline_count = list() # (P)
serine_count = list() # (S)
threonine_count = list() # (T)
tryptophan_count = list() # (W)
tyrosine_count = list() # (Y)
valine_count = list() # (V)
#optional counts
# asp_or_asp_acid_count = list() # (B)
# glutamine_or_glutamic_acid_count = list() # (Z)

feature_list = [alanine_count,arginine_count,asparagine_count,aspartic_acid_count,cysteine_count,glutamine_count,glutamic_count,\
                glycine_count,histidine_count,isoleucine_count,leucine_count,lysine_count,methionine_count,phenylalanine_count,\
                proline_count,serine_count,threonine_count,tryptophan_count,tyrosine_count,valine_count]


sequence_letter_list = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']
seq_name_list = ['ala','arg','asn','asp','cys','gln','glu','gly','his','ile','leu','lys','met','phe',\
                'pro','ser','thr','trp','tyr','val']

# lists for features from the site

#Hydrophobicity
hydro_1 = ['R','K','E','D','Q','N']
hydro_2 = ['G','A','S','T','P','H','Y']
hydro_3 = ['C','L','V','I','M','F','W']

hydro_1r, hydro_2r, hydro_3r = list(), list(), list()

g4_series_ratios = [hydro_1r, hydro_2r, hydro_3r]


def g_series_count (val,seq_len,  list_all, list_ratio_all):
    for inner_list in list_all:
        for value in inner_list:
            if (val = value):
                list_ratio_all.append




#Normalized

g_series_list = [hydro_1, hydro_2, hydro_3]

# feature_tuple = merge(feature_list, sequence_letter_list)

for  seq_str in (sequenceLabel):

    str_len = len(seq_str)
    max_num = -1
    temp_num = 0
    least_num = 1300
    temp_str = ''
    temp_tot_none = ''
    max_num_str_temp = ''
    max_num_str_tot = ''
    least_num_str_tot = ''

    g_series_count(seq_str, str_len, g_series_list, g4_series_ratios)


    #loop to go through each character in string
    for num, value in  enumerate(feature_list):
        temp_num = seq_str.count(sequence_letter_list[num])
        feature_list[num].append(temp_num)
        temp_str = sequence_letter_list[num] #individual character
        
        
        

        #checks highest count for max number and index
        if(temp_num > max_num):
            max_num = temp_num
            max_num_str_tot = temp_str
            

        elif(temp_num == max_num):
            max_num_str_tot = max_num_str_tot + temp_str

        elif(temp_num < least_num and (temp_num != 0)):
            least_num_str_tot = temp_str
            least_num = temp_num
            
        
        elif(temp_num == least_num and (temp_num != 0)):
            lest_num_str_tot = least_num_str_tot + temp_str


        elif(temp_num == 0):
            temp_tot_none = temp_str + temp_tot_none


    feature_length.append(str_len)
    max_letter_list.append(max_num_str_tot) # all letters that are max
    max_letter_count.append(max_num) #highest count
    max_count_ratio.append(max_num/str_len) #ratio of highest over total
    least_letter_list.append(least_num_str_tot) # amount
    least_letter_count.append(least_num)
    no_letter_list.append(temp_tot_none)



    # print (count)


#feature for number of a in each drawLine



# for loop to insert column count into csv
for i in range(20):
    insert_column(data,seq_name_list[i] + '_count',feature_list[i],(i +1))
    # print (i)

# insert columns to df here
insert_column(data,'seq_len', feature_length, 21)
insert_column(data,'most freq amino',max_letter_list,22)
insert_column(data,'max_num',max_letter_count,23)
insert_column(data,'max ratio',max_count_ratio,24)
insert_column(data,'least freq amino',least_letter_list,25)
insert_column(data,'least_num',least_letter_count,26)
insert_column(data,'not in seq',no_letter_list,27)


#Export data frame to csv
data.to_csv("output.csv", index=False, header = True)

# print (data)
#



# print stuff
# print (sequenceLabel)
# print (dnaLabel)
# print (feature_length)
# print (data)
# print(test_string.count('C'))
# print(test_string.count('N'))
# print(test_string)
# print (sequence_letter_list)
# print (feature_list)
# print (feature_tuple)
# print (len(feature_list))
# print (len(sequence_letter_list))
# print(seq_name_list)
# print(len(seq_name_list))
# print(len(sequence_letter_list))
#test
# alanine_count.append('22')
# test_list = [['1','2','3'],['4','5,','6']]
# # glutamine_or_glutamic_acid_count = ['22']
# print (test_list)
# test_list[0].append('0')
# print (test_list)

# print(feature_list[0])
# print
# print(sequence_letter_list[0])
# feature_list[0].append(sequence_letter_list[0])
# print(feature_list[0])
# print (feature_list[0].append(sequence_letter_list[0]))
# print (feature_list[21].append(sequence_letter_list[21]))
# print(len(max_letter_count))
# print(len(max_letter_count))
# print(len(max_letter_list))
# print(max(max_letter_count))

# print(len(max_letter_count))
# print(len(max_letter_count))
# print(len(max_letter_list))
