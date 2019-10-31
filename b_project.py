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

# add dna label to list
dnaLabel = list()
dnaLabel = data['label'].tolist()


# add sequence to a list
sequenceLabel = list()
sequenceLabel = data['sequence'].tolist()

feature_length = list() # count number of characters in a list

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
asp_or_asp_acid_count = list() # (B)
glutamine_or_glutamic_acid_count = list() # (Z)

feature_list = [alanine_count,arginine_count,asparagine_count,aspartic_acid_count,cysteine_count,glutamine_count,glutamic_count,\
                glycine_count,histidine_count,isoleucine_count,leucine_count,lysine_count,methionine_count,phenylalanine_count,\
                proline_count,serine_count,threonine_count,tryptophan_count,tyrosine_count,valine_count,asp_or_asp_acid_count,\
                glutamine_or_glutamic_acid_count]

sequence_letter_list = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z']
seq_name_list = ['ala','arg','asn','asp','cys','gln','glu','gly','his','ile','leu','lys','met','phe',\
                'pro','ser','thr','trp','tyr','val','asx','glx']

# feature_tuple = merge(feature_list, sequence_letter_list)
# for loop to count each
for  i in (sequenceLabel):
    feature_length.append(len(i))

    for count, value in  enumerate(feature_list):
        feature_list[count].append(i.count(sequence_letter_list[count]))

#feature for number of a in each drawLine


# # insert columns with letter count  character
for i in range(20):
    insert_column(data,seq_name_list[i] + '_count',feature_list[i],(i +1))
    # print (i)

insert_column(data,'seq_len', feature_length, 21)
# data.insert (1,'sequence length', feature_length)

#Export data frame to csv
data.to_csv("output.csv", index=False, header = True)

print (data)
