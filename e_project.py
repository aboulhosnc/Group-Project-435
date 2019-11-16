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

df = pd.DataFrame()
# df_dna = pd.DataFrame()
# df_rna = pd.DataFrame()
# df_drna = pd.DataFrame()
# df_nondrna = pd.DataFrame()

# global variables
col_pos = 0 # for adding number
test_string = 'CGQGFSVKSDVITHQRTHTGEKLYVCRECGRGFSWKSHLLIHQRIHTGEKPYVCRECGRGFSWQSVLLTHQRTHTG'\
                + 'EKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSWQSVLL'\
                + 'THQRTHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRGFSRQ'\
                + 'SVLLTHQRRHTGEKPYVCRECGRGFSRQSVLLTHQRRHTGEKPYVCRECGRGFSWQSVLLTHQRTHTGEKPYVCRECGRG'\
                + 'FSNKSHLLRHQRTHTGEKPYVCRECGRGFRDKSHLLSHQRTHTGEKPYVCRECGRGFRDKSNLLSHQRTHTGEKPYVCREC'\
                + 'GRGFSWQSVLLRHQRTHTGEKPYVCRECGRGFRDKSNLLSHQRTHTGEKPYVCRECGRGFRNKSHLLRHQRTHTGEKPYVCR'\
                + 'ECGRGFSDRSSLCYHQRTHTGEKPYVCREDE'





# shuffle's the columns before performing all the functions
# depends on if we are doing it in rapid miner or not
data = data.sample(frac=1).reset_index(drop=True)
# data = data.sample(frac=1).reset_index(drop=False)  # Does not drop index


# function to add columns to it
def insert_column (df_1, name, feature, col_position):
    df_1.insert (col_position, name, feature)
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

#convert label  for each type DNA RNA etc
# can switch between 1 and 0 and yes and no
def  convertLabel (list, word, temp_list):
    temp_list.clear()
    for i in list:
        if ( i == word):
            temp_list.append(1)
            # temp_list.append('Yes')
        else:
            temp_list.append(0)
            # temp_list.append('No')
    return temp_list

# inserts column of value only
# resets colummn reset_index
# deletes value
def output_column(data_2,label_col_list,lab_list,value):
    global col_pos
    # print('value is :', value)
    temp_list = convertLabel(label_col_list,value,lab_list)
    insert_column(data_2, value, temp_list, (col_pos))
    # data_2.to_csv("output_" +(value) + ".csv", index=False, header = True)
    # print(value)

    #when adding columns and deleting comment out this part
    # col_pos = col_pos - 1
    # del df[value]

def g_transition_function(str_test, list_result):
    count = 0
    str_len = len(str_test)
    for i in range(len(str_test)-1):
        if str_test[i]!=str_test[i+1]:
            count = count + 1
    tem_val = count / str_len

    list_result.append(tem_val)
        # print(test_count)



         

def g_number_convert (g_list, result_list, seq_test,g_trans,g_dest):
    seq_copy = ''
    # seq_len = len(seq_test)
    for i in range(0, (24*3), 3):
        list_1, list_2, list_3 = g_list[i], g_list[i+1], g_list[i+2]
        for element in (seq_test):
            # print (element)
            if(element in list_1):
                # result_list.append(1)
                seq_copy = seq_copy + '1'
                # print('1')
            elif(element in list_2):
                # result_list.append(2)
                seq_copy = seq_copy + '2'
                # print('2')
            elif(element in list_3):
                # result_list.append(3)
                seq_copy = seq_copy + '3'
                # print('3')
        
    result_list.append(seq_copy)
    g_transition_function(seq_copy,g_trans)
    # g_destribution_function(result_list,g_dest,seq_len)
    
    


# def


# add sequence to a list
sequenceLabel = list()
sequenceLabel = data['sequence'].tolist()

#features added
feature_length = list() # count number of characters in a list
max_letter_list = list() # list of the max letter in the list
max_letter_count = list() # list of max num for each row
max_count_ratio = list() # ratio of max number of total number
least_letter_count = list() # least letter number
least_letter_list = list() # least letter descriptionstring2 = string2 + ' ' + word
no_letter_list = list() # list for all
seq_start_list = list() # list for if it starts with m or not
seq_num_category_list = list() # list of sequences with number values instead 
g_transition_column = list() # column for transition numbers
g_distribution_column = list() #column for distribution numbers


#lists of counts of amino acids
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


hydro_t,n_van_vol_t,polarity_t,polarization_t,charge_t,second_t,solv_t,sur_t,pro_b_t,pro_m_t,pro_s_t,pro_a_t,pro_k_t,pro_eli_t,pro_ph_t,pro_lig_k_t,pro_lig_v_t,\
pro_im_t,mol_t,clog_t,no_hy_d_t,no_hy_a_t,sol_t,acid_t = ([] for i in range(24))

g4_transtion_list = [hydro_t,n_van_vol_t,polarity_t,polarization_t,charge_t,second_t,solv_t,sur_t,pro_b_t,pro_m_t,pro_s_t,pro_a_t,pro_k_t,pro_eli_t,pro_ph_t,pro_lig_k_t,pro_lig_v_t,\
pro_im_t,mol_t,clog_t,no_hy_d_t,no_hy_a_t,sol_t,acid_t]

# print(len(g4_transtion_list))
# test_list = list()
test_seq = 'MTEITAAMVKELRESTGAGA'
test_result = '32132223311311222222'

# for count  in range(len(g4_transtion_list)):
# for num, value  in enumerate(g_series_list):
#     for element in range(0, len(test_seq)): 
#         if(num % 3 == 0):
#             if(element in value):
#                 g4_transtion_list[0].append(1)
#         elif(num %3 == 1):
#             if(element in value):
#                 g4_transition_list[0].append(2)
#         elif(num % 3 == 2):
#             if(element in value):
#                 g4_t

# for i in range(72, 3):
    # print(i)



# can add names of classes here
g_series_name_list = ['Polar','Neutral','Hydrophobicity','0-2.78','2.95-4.0','4.03-8.08','4.9-6.2','8.0-9.2','10.4-13.0','0-1.08','0.128-0.186','0.219-0.409',\
                    'Positive','Neutral','Negative','Helix','Strand','Coil','Buried','Exposed','Intermediate','-0.20~0.16','-0.3~ -0.52','-0.98~ -2.46','High (5-21%)',\
                    'Medium (1.12-3.64%)','Low (0-0.83%)','High (1.21-2.02)','Medium (0.63-1.12)','Low (0.14-0.29)','High (4-30%)','Medium (1-3%)','Low (0-1%)',\
                    'High (25-100%)','Medium (5-18%)','Low (0-4%)','High (0.25-11)','Medium (-0.25 – 0.17)','Low (-0.3 - -0.8)','High (1.18-2.07)','Medium (0.84-1.16)',\
                    'Low (0.41-0.8)','High (0.95-1.8)','Medium (0.5-0.95)','Low (0-0.5)','High (≥2.25)','Medium (1.6-2.3)','Low (≤1.5)','High (≥1.4)','Medium (0.79-1.21)',\
                    'Low (≤0.76)','High (477-1197)','Medium (95-423)','Low (<95)','Low (75-105)','Medium (115-155)','High (165-204)','-4.2 - -3.3','-3.07 – 2.26','-1.78 - -1.05',\
                    '>1','1','0','>1','1','0','High (9-65 g/100g)','Medium (1.14-7.44 g/100g)','Low (0.048-0.82g/100g)','Very flexible','Moderately flexible','Less flexible',]

# g_series_transition(test_string, len(test_string), g_series_list, g4_transtion_list)



# def g_series_transition (seq, seq_len, list_all, list_ratio_all)


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
    (seq_start_list.append(1)if seq_str.startswith('M')else seq_start_list.append(0))
    # (seq_start_list.append('Yes')if seq_str.startswith('M')else seq_start_list.append('No'))


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

         
    # print(len(seq_num_category_list))
    # g_number_convert(g_series_list,seq_num_category_list,g_transition_column, g_distribution_column, seq_str,str_len)  
    g_number_convert(g_series_list,seq_num_category_list,seq_str, g_transition_column, g_distribution_column)   


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
    insert_column(df,sequence_letter_list[i] + '_count',feature_list[i],(col_pos))
    # print (i)


# features from slide in powerpoint 72 in total here
whole_id = 1
for i in range(len(g4_series_ratios)):
    increment = ((i %3) + 1)
    # insert_column(data,'G4.C.'+ str(whole_id) + '.' + str(increment) +'.' + g_series_name_list[i] , g4_series_ratios[i],(col_pos))
    insert_column(df,'G4.C.'+ str(whole_id) + '.' + str(increment) , g4_series_ratios[i],(col_pos))
    whole_id = ((whole_id + 1) if increment == 3 else (whole_id))



# insert columns to df here
# naive columns based purely on counts of numbers
insert_column(df,'seq_len', feature_length, col_pos)
insert_column(df,'max_num',max_letter_count,col_pos)
insert_column(df,'least_num',least_letter_count,col_pos)
insert_column(df,'start_with_M',seq_start_list,col_pos)
# insert_column(df,'col_cat_num',seq_num_category_list,col_pos)
insert_column(df,'g_t_ratio',g_transition_column,col_pos)
# insert_column(df,'g_d_ratio',g_distribution_column,col_pos)

#final column for labels
# insert_column(df,'Label',dnaLabel,col_pos)

label_list = ['DNA','RNA','DRNA','nonDRNA']

#a column for each label
output_column(df,dnaLabel,label_list,'DNA')
output_column(df,dnaLabel,label_list,'RNA')
output_column(df,dnaLabel,label_list,'DRNA')
output_column(df,dnaLabel,label_list,'nonDRNA')


# for version d removed output to d labels are all on one file
df.to_csv("input.csv", index=False, header = True)





# print table
# print (df)
#
