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
max_amino =


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

def getMaxOccuringChar(str):
    # Create array to keep the count of individual characters
    # Initialize the count array to zero
    count = [0] * ASCII_SIZE

    # Utility variables
    max = -1
    c = ''

# add dna label to list
dnaLabel = list()
dnaLabel = data['label'].tolist()


# add sequence to a list
sequenceLabel = list()
sequenceLabel = data['sequence'].tolist()

feature_length = list() # count number of characters in a list
max_letter_list = list() # list of the max letter in the list
max_letter_count = list()


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
# alanine - ala - A (gif, interactive)
# arginine - arg - R (gif, interactive)
# asparagine - asn - N (gif, interactive)
# aspartic acid - asp - D (gif, interactive)
# cysteine - cys - C (gif, interactive)
# glutamine - gln - Q (gif, interactive)
# glutamic acid - glu - E (gif, interactive)
# glycine - gly - G (gif, interactive)
# histidine - his - H (gif, interactive)
# isoleucine - ile - I (gif, interactive)
# leucine - leu - L (gif, interactive)
# lysine - lys - K (gif, interactive)
# methionine - met - M (gif, interactive)
# phenylalanine - phe - F (gif, interactive)
# proline - pro - P (gif, interactive)
# serine - ser - S (gif, interactive)
# threonine - thr - T (gif, interactive)
# tryptophan - trp - W (gif, interactive)
# tyrosine - tyr - Y (gif, interactive)
# valine - val - V (gif, interactive)
# Sometimes it is not possible two differentiate two closely related amino acids, therefore we have the special cases:
# asparagine/aspartic acid - asx - B
# glutamine/glutamic acid - glx - Z

# feature_tuple = merge(feature_list, sequence_letter_list)

for  seq_str in (sequenceLabel):
    feature_length.append(len(seq_str))

    for num, value in  enumerate(feature_list):
        feature_list[num].append(seq_str.count(sequence_letter_list[num]))
        # max_letter_list.append()

    max_letter_list.append(feature_list.sort())



    # print (count)




# position = list.index(i)
# print ('element {} has {} letters '.format(sequenceLabel.index(i),len(i)))
# feature_length.append(len(i))
# #ARNDCQEGHILKMFPSTWYV
# alanine_count.append(count_character(i,'A'))
# arginine_count.append(i.count('R'))
# asparagine_count.append(i.count('N'))
# aspartic_acid_count.append(i.count('D'))
# cysteine_count.append(count_character(i,'C'))
# glutamine_count.append(i.count('Q'))
# glutamic_count.append(i.count('E'))
# glycine_count.append(i.count('G'))
# histidine_count.append(i.count('H'))
# isoleucine_count.append(i.count('I'))
# leucine_count.append(i.count('L'))
# lysine_count.append(i.count('K'))
# methionine_count.append(i.count('M'))
# phenylalanine_count.append(i.count('F'))
# proline_count.append(i.count('P'))
# serine_count.append(i.count('S'))
# threonine_count.append(i.count('T'))
# tryptophan_count.append(i.count('W'))
# tyrosine_count.append(i.count('Y'))
# valine_count.append(i.count('V'))
# asp_or_asp_acid_count.append(i.count('B'))
# glutamine_or_glutamic_acid_count.append(i.count('Z'))

#feature for number of a in each drawLine


# # insert columns into character
# insert_column(data,'seq_len', feature_length, 1)
# insert_column(data,'ala_count', alanine_count, 2)
# insert_column(data,'arg_count', arginine_count, 3)
# insert_column(data,'asp_count', asparagine_count, 4)
# insert_column(data,'cys_count', cysteine_count, 5)

for i in range(20):
    insert_column(data,seq_name_list[i] + '_count',feature_list[i],(i +1))
    # print (i)

insert_column(data,'seq_len', feature_length, 21)
# data.insert (1,'sequence length', feature_length)

#Export data frame to csv
data.to_csv("output.csv", index=False, header = True)

print (data)


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
