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


# global variables
col_pos = 1 # for adding number
# test_string = 'CGQGFSVKSDVITHQRTHTGEKLYVCRECGRGFSWKSHLLIHQRIHTGEKPYVCRECGRGFSWQSVLLTHQRTHTG'\
#                 + 'EKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSWQSVLL'\
#                 + 'THQRTHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSRQ'\
#                 + 'SVLLTHQRRHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRG'\
#                 + 'FSNKSHLLRHQRTHTGEKPYVCRECGRGFRDKSHLLSHQRTHTGEKPYVCRECGRGFRDKSNLLSHQRTHTGEKPYVCREC'\
#                 + 'GRGFSWQSVLLRHQRTHTGEKPYVCRECGRGFRDKSNLLSHQRTHTGEKPYVCRECGRGFRNKSHLLRHQRTHTGEKPYVCR'\
#                 + 'ECGRGFSDRSSLCYHQRTHTGEKPYVCREDE'




# shuffle's the columns before performing all the functions
# depends on if we are doing it in rapid miner or not
data = data.sample(frac=1).reset_index(drop=True)
# data = data.sample(frac=1).reset_index(drop=False)  # Does not drop index


# function to add columns to it
def insert_column (df, name, feature, col_position):
    df.insert (col_position, name, feature)
    global col_pos
    col_pos = ( col_pos + 1)

#function for 72 custom features finds the ratio
def g_series_count (seq,seq_len,  list_all, list_ratio_all):
    for list_count , inner_list in enumerate(list_all):
        tem_num = 0
        for value in (inner_list):
            tem_num = seq.count(value) + tem_num

        tem_num = (tem_num / seq_len)
        list_ratio_all[list_count].append(tem_num)


#fill in missing data with vales
def fill_in(list):
    for n,  i in enumerate(list):
        if(i == ''):
            list[n] = 'None'

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
seq_start_list = list() # list for if it starts with m or not


#lists of counts of amino acids
# alanine_count = list() # count number of alanine in a list (A)
# arginine_count = list() # count number of arginine (R)
# asparagine_count = list() #count number of asparagine  (N)
# aspartic_acid_count = list() # count of asp acid (D)
# cysteine_count =list() # count number of cysteine in a list (C)
# glutamine_count = list() # count number of glutamine (Q)
# glutamic_count = list() # count of glutaimic (E)
# glycine_count = list() # count of glycine (G)
# histidine_count = list() # (H)
# isoleucine_count = list() #(I)
# leucine_count = list() # (L)
# lysine_count = list() # (K)
# methionine_count = list() # (M)
# phenylalanine_count = list() # (F)
# proline_count = list() # (P)
# serine_count = list() # (S)
# threonine_count = list() # (T)
# tryptophan_count = list() # (W)
# tyrosine_count = list() # (Y)
# valine_count = list() # (V)

alanine_count,arginine_count,asparagine_count,aspartic_acid_count,cysteine_count,glutamine_count,glutamic_count,\
glycine_count,histidine_count,isoleucine_count,leucine_count,lysine_count,methionine_count,phenylalanine_count,\
proline_count,serine_count,threonine_count,tryptophan_count,tyrosine_count,valine_count = ([] for i in range(20))
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

#Hydrophobicity 1
hydro_1 = ['R','K','E','D','Q','N'] # arg, lysine, glutamic_count, asp acid, glutamine, asparagine
hydro_2 = ['G','A','S','T','P','H','Y']
hydro_3 = ['C','L','V','I','M','F','W']
hydro_1r, hydro_2r, hydro_3r = list(), list(), list()

#normalized van der Wals Volume 2
n_van_vol_1 = ['G','A','S','T','P','D'] 
n_van_vol_2 = ['N','V','E','Q','I','L']
n_van_vol_3 = ['M','H','K','F','R','Y','W']
n_van_vol_1r, n_van_vol_2r, n_van_vol_3r = list(), list(), list()

#Polarity 3
polarity_1 = list('LIFWCMVY')
polarity_2 = list('PATGS')
polarity_3 = list('HQRKNED')
pol_1r, pol_2r, pol_3r = ([] for i in range(3))

#Polarizability 4
polarizability_1 = list('GASDT')
polarizability_2 = list('CPNVEQIL')
polarizability_3 = list('KMHFRYW')
polarize_1r, polarize_2r, polarize_3r = ([] for i in range(3))

#Charge 5
charge_1, charge_2, charge_3 = list('KR'), list('ANCQGHILMFPSTWYV'), list('DE')
charge_1r, charge_2r, charge_3r = ([] for i in range(3))

# Secondary Structure 6
second_1, second_2, second_3 = list('EALMQKRH'), list('VIYCWFT'), list('GNPSD')
second_1r, second_2r, second_3r = ([] for i in range(3))

#Solvent accessibility 7
solv_1, solv_2, solv_3 = list('ALFCGIVW'), list('PKQEND'), list('MPSTHY')
solv_1r, solv_2r, solv_3r = ([] for i in range(3))

# Surface Tension 8
sur_1, sur_2, sur_3 = list('GQDNAHR'), list('KTSEC'), list('ILMFPWYV')
sur_1r, sur_2r, sur_3r = ([] for i in range(3))

# Protein-protein interface hotspot propensity - Bogan 9
pro_bogan_1, pro_bogan_2, pro_bogan_3 = list('DHIKNPRWY'), list('EQSTGAMF'), list('CLV')
pro_bogan_1r, pro_bogan_2r, pro_bogan_3r = ([] for i in range(3))

# Protein-DNA interface propensity - Ma 10
pro_ma_1, pro_ma_2, pro_ma_3 = list('CDFMPQRWY'), list('AGHVLNST'), list('EIK')
pro_ma_1r, pro_ma_2r, pro_ma_3r = ([] for i in range(3))

# Protein-DNA interface propensity - Schneider 11
pro_sch_1, pro_sch_2, pro_sch_3 = list('GKNQRSTY'), list('ADEFHILVW'), list('CMP')
pro_sch_1r, pro_sch_2r, pro_sch_3r = ([] for i in range(3))

# Protein-DNA interface propensity - Ahmad 12
pro_ahmed_1, pro_ahmed_2, pro_ahmed_3 = list('GHKNQRSTY'), list('ADEFIPVW'), list('CLM')
pro_ahmed_1r, pro_ahmed_2r, pro_ahmed_3r = ([] for i in range(3))

# Protein-RNA interface propensity - Kim 13
pro_kim_1, pro_kim_2, pro_kim_3 = list('HKMRY'), list('FGILNPQSVW'), list('CDEAT')
pro_kim_1r, pro_kim_2r, pro_kim_3r = ([] for i in range(3))

# Protein-RNA interface propensity - Ellis 14
pro_ellis_1, pro_ellis_2, pro_ellis_3 = list('HGKMRSYW'), list('AFINPQT'), list('CDELV')
pro_ellis_1r, pro_ellis_2r, pro_ellis_3r = ([] for i in range(3))

# Protein-RNA interface propensity - Phipps 15
pro_phips_1, pro_phips_2, pro_phips_3 = list('HKMQRS'), list('ADEFGLNPVY'), list('CITW')
pro_phips_1r, pro_phips_2r, pro_phips_3r = ([] for i in range(3))

# Protein-ligand binding site propensity - Khazanov 16
pro_lig_khaz_1, pro_lig_khaz_2, pro_lig_khza_3 = list('CFHWY'), list('GILNMSTR'), list('AEDKPQV')
pro_lig_khaz_1r, pro_lig_khaz_2r, pro_lig_khaz_3r = ([] for i in range(3))

# Protein-ligand valid binding site propensity - Khazanov 17
pro_lig_val_khaz_1, pro_lig_val_khaz_2, pro_lig_val_khza_3 = list('CFHWYM'), list('DGILNSTV'), list('AEKPQR')
pro_lig_val_khaz_1r, pro_lig_val_khaz_2r, pro_lig_val_khaz_3r = ([] for i in range(3))

# Propensity for protein-ligand polar & aromatic nonbonded interactions - Imai 18
prop_imai_1, prop_imai_2, prop_imai_3 = list('DEHRY'), list('CFKMNQSTW'), list('AGILPV')
prop_imai_1r, prop_imai_2r, prop_imai_3r = ([] for i in range(3))

# Molecular Weight 19
mol_1, mol_2, mol_3 = list('AGS'), list('CDEHIKLMNQPTV'), list('FRWY')
mol_1r, mol_2r, mol_3r = ([] for i in range(3))

# cLogP  20
clog_1, clog_2, clog_3 = list('RKDNEQH'), list('PYSTGACV'), list('WMFLI')
clog_1r, clog_2r, clog_3r = ([] for i in range(3))

# No of hydrogen bond donor in side chain 21
no_hy_don_1, no_hy_don_2, no_hy_don_3 = list('HKNQR'), list('DESTWY'), list('ACGFILMPV')
no_hy_don_1r, no_hy_don_2r, no_hy_don_3r = ([] for i in range(3))

# No of hydrogen bond acceptor in side chain 22
no_hy_acpt_1, no_hy_acpt_2, no_hy_acpt_3 = list('DEHNQR'), list('KSTWY'), list('ACGFILMPV')
no_hy_acpt_1r, no_hy_acpt_2r, no_hy_acpt_3r = ([] for i in range(3))

# Solubility in water 23
sol_wat_1, sol_wat_2, sol_wat_3 = list('ACGKRT'), list('EFHILMNPQSVW'), list('DY')
sol_wat_1r, sol_wat_2r, sol_wat_3r = ([] for i in range(3))

# Amino acid flexibility index 24
acid_flex_1, acid_flex_2, acid_flex_3 = list('EGKNQS'), list('ADHIPRTV'), list('CFLMWY')
acid_flex_1r, acid_flex_2r, acid_flex_3r = ([] for i in range(3))

#list of list (each item in categor), 
g_series_list = [hydro_1, hydro_2, hydro_3, n_van_vol_1, n_van_vol_2, n_van_vol_3, polarity_1, polarity_2, polarity_3,polarizability_1, polarizability_2, polarizability_3, charge_1, charge_2, charge_3,\
                second_1, second_2, second_3, solv_1, solv_2, solv_3, sur_1, sur_2, sur_3, pro_bogan_1, pro_bogan_2, pro_bogan_3, pro_ma_1, pro_ma_2, pro_ma_3,\
                pro_sch_1, pro_sch_2, pro_sch_3, pro_ahmed_1, pro_ahmed_2, pro_ahmed_3, pro_kim_1, pro_kim_2, pro_kim_3, pro_ellis_1, pro_ellis_2, pro_ellis_3,\
                pro_phips_1, pro_phips_2, pro_phips_3, pro_lig_khaz_1, pro_lig_khaz_2, pro_lig_khza_3, pro_lig_val_khaz_1, pro_lig_val_khaz_2, pro_lig_val_khza_3,\
                prop_imai_1, prop_imai_2, prop_imai_3, mol_1, mol_2, mol_3, clog_1, clog_2, clog_3, no_hy_don_1, no_hy_don_2, no_hy_don_3,no_hy_acpt_1, no_hy_acpt_2, no_hy_acpt_3,\
                sol_wat_1, sol_wat_2, sol_wat_3, acid_flex_1, acid_flex_2, acid_flex_3]

#list of all list of ratios
g4_series_ratios = [hydro_1r, hydro_2r, hydro_3r, n_van_vol_1r, n_van_vol_2r, n_van_vol_3r,pol_1r, pol_2r, pol_3r, polarize_1r, polarize_2r, polarize_3r, charge_1r, charge_2r, charge_3r,\
                    second_1r, second_2r, second_3r, solv_1r, solv_2r, solv_3r, sur_1r, sur_2r, sur_3r, pro_bogan_1r, pro_bogan_2r, pro_bogan_3r, pro_ma_1r, pro_ma_2r, pro_ma_3r,\
                    pro_sch_1r, pro_sch_2r, pro_sch_3r, pro_ahmed_1r, pro_ahmed_2r, pro_ahmed_3r, pro_kim_1r, pro_kim_2r, pro_kim_3r, pro_ellis_1r, pro_ellis_2r, pro_ellis_3r,\
                    pro_phips_1r, pro_phips_2r, pro_phips_3r, pro_lig_khaz_1r, pro_lig_khaz_2r, pro_lig_khaz_3r, pro_lig_val_khaz_1r, pro_lig_val_khaz_2r, pro_lig_val_khaz_3r,\
                    prop_imai_1r, prop_imai_2r, prop_imai_3r, mol_1r, mol_2r, mol_3r, clog_1r, clog_2r, clog_3r, no_hy_don_1r, no_hy_don_2r, no_hy_don_3r,\
                    no_hy_acpt_1r, no_hy_acpt_2r, no_hy_acpt_3r, sol_wat_1r, sol_wat_2r, sol_wat_3r, acid_flex_1r, acid_flex_2r, acid_flex_3r]


# can add names of classes here
g_series_name_list = ['Polar','Neutral','Hydrophobicity','0-2.78','2.95-4.0','4.03-8.08','4.9-6.2','8.0-9.2','10.4-13.0','0-1.08','0.128-0.186','0.219-0.409',\
                    'Positive','Neutral','Negative','Helix','Strand','Coil',]


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

    # g_series_count(seq_str, str_len, g_series_list, g4_series_ratios)
    g_series_count(seq_str, str_len, g_series_list, g4_series_ratios)

    # can be eith Yes No or 1 0
    # (seq_start_list.append(1)if seq_str.startswith('M')else seq_start_list.append(0))
    (seq_start_list.append('Yes')if seq_str.startswith('M')else seq_start_list.append('No'))


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

#feature for number of a in each drawLine


#fill in missing data with none
fill_in(no_letter_list)


# for loop to insert column count into csv
# count of each letter in the sequence
for i in range(len(feature_list)):
    insert_column(data,sequence_letter_list[i] + '_count',feature_list[i],(col_pos))
    # print (i)


# features from slide in powerpoint 72 in total here
whole_id = 1
for i in range(len(g4_series_ratios)):
    increment = ((i %3) + 1)
    # insert_column(data,'G4.C.'+ str(whole_id) + '.' + str(increment) +'.' + g_series_name_list[i] , g4_series_ratios[i],(col_pos))
    insert_column(data,'G4.C.'+ str(whole_id) + '.' + str(increment) , g4_series_ratios[i],(col_pos))
    whole_id = ((whole_id + 1) if increment == 3 else (whole_id))


# insert columns to df here
# naive columns based purely on counts of numbers
insert_column(data,'seq_len', feature_length, col_pos)
insert_column(data,'most freq amino',max_letter_list,col_pos)
insert_column(data,'max_num',max_letter_count,col_pos)
insert_column(data,'max ratio',max_count_ratio,col_pos)
insert_column(data,'least freq amino',least_letter_list,col_pos)
insert_column(data,'least_num',least_letter_count,col_pos)
insert_column(data,'not in seq',no_letter_list,col_pos)
insert_column(data,'start with M',seq_start_list,col_pos)


#Export data frame to csv
data.to_csv("output.csv", index=False, header = True)

# print (data)
#



