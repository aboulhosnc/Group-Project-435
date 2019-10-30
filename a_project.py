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


test_string = 'CGQGFSVKSDVITHQRTHTGEKLYVCRECGRGFSWKSHLLIHQRIHTGEKPYVCRECGRGFSWQSVLLTHQRTHTG'\
                + 'EKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSWQSVLL'\
                + 'THQRTHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSRQ'\
                + 'SVLLTHQRRHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRG'\
                + 'FSNKSHLLRHQRTHTGEKPYVCRECGRGFRDKSHLLSHQRTHTGEKPYVCRECGRGFRDKSNLLSHQRTHTGEKPYVCREC'\
                + 'GRGFSWQSVLLRHQRTHTGEKPYVCRECGRGFRDKSNLLSHQRTHTGEKPYVCRECGRGFRNKSHLLRHQRTHTGEKPYVCR'\
                + 'ECGRGFSDRSSLCYHQRTHTGEKPYVCREDE'

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

for i in sequenceLabel:
    # position = list.index(i)
    # print ('element {} has {} letters '.format(sequenceLabel.index(i),len(i)))
    feature_length.append(len(i))
    #ARNDCQEGHILKMFPSTWYV
    alanine_count.append(count_character(i,'A'))
    arginine_count.append(i.count('R'))
    asparagine_count.append(i.count('N'))
    aspartic_acid_count.append(i.count('D'))
    cysteine_count.append(count_character(i,'C'))
    glutamine_count.append(i.count('Q'))
    glutamic_count.append(i.count('E'))
    glycine_count.append(i.count('G'))
    histidine_count.append(i.count('H'))
    isoleucine_count.append(i.count('I'))
    leucine_count.append(i.count('L'))
    lysine_count.append(i.count('K'))
    methionine_count.append(i.count('M'))
    phenylalanine_count.append(i.count('F'))
    proline_count.append(i.count('P'))
    serine_count.append(i.count('S'))
    threonine_count.append(i.count('T'))
    tryptophan_count.append(i.count('W'))
    tyrosine_count.append(i.count('Y'))
    valine_count.append(i.count('V'))
    asp_or_asp_acid_count.append(i.count('B'))
    glutamine_or_glutamic_acid_count.append(i.count('Z'))






print

#feature for number of a in each drawLine


# insert columns into character
insert_column(data,'seq_len', feature_length, 1)
insert_column(data,'ala_count', alanine_count, 2)
insert_column(data,'cys_count', cysteine_count, 3)
insert_column(data,'asp_count', asparagine_count, 4)


# data.insert (1,'sequence length', feature_length)

#Export data frame to csv
data.to_csv("output.csv", index=False, header = True)

# print stuff
# print (sequenceLabel)
# print (dnaLabel)
# print (feature_length)
# print (data)
# print(test_string.count('C'))
# print(test_string.count('N'))
# print(test_string)
# print (sequence_letter_list)
print (feature_list)
