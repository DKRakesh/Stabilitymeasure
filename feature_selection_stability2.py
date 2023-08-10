# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import random
import xlsxwriter
#import numpy as np

#from Feature_selection import Anova_based, infogain, t_test 
#from General_code import feature_ranking_as_values as feature

#method for finding stability
#feature_rank_position=feature.feature_position()

#print("feature_rank_position",feature_rank_position)


def feature_sel_stability(path,initial):

    data=pd.read_excel(path,header=None)
    data=np.array(data)
    instance,features=np.shape(data)
    subset_size=int(initial*features)
    print("in,fea",instance,features)
    no_of_iteration=50
    
    subset_iterated_feature_rank_values=data[:,0:subset_size]
    
    '''
    iterated_feature_rank_values=feature.feature_position(no_of_iteration)
    instances,dimension=np.shape(iterated_feature_rank_values)
    
    
    print("jfg",iterated_feature_rank_values)
    subset_iterated_feature_rank_values=np.zeros((no_of_iteration,subset_size))
    
    for i in range(no_of_iteration):
        
        for j in range(subset_size):
            subset_iterated_feature_rank_values[i][j]=iterated_feature_rank_values[i][j]
    
    '''        
        
    print("subset",subset_iterated_feature_rank_values)
    unique_value=np.unique(subset_iterated_feature_rank_values)
    print("unique features stability",unique_value)
    
    N=0
    summation=0
    C_s_summ=0
    F_max=no_of_iteration
    F_min=1
    consistency_for_feature_ranking=[]
    
    for i in range(len(unique_value)):
        temp=unique_value[i]
        length=0
        for j in range(no_of_iteration):
            for k in range(subset_size):
                if subset_iterated_feature_rank_values[j][k]==temp:
                    length=length+1
        
        c_f=((length-1)/(F_max-F_min))
        consistency_for_feature_ranking.append(c_f)        
        mul=length*(length-1)
        C_s_summ=C_s_summ+(length-1)
        #nprint("length",length)
        #nprint("mul",mul)
        N=N+length
        summation=summation+mul
        
    
    #nprint("N",N)
    #nprint("lengthN",length)
    
    Y=features
    
    '''
    Set of all features in the dataset.
    
    '''
    
    n=no_of_iteration
    #nprint("summation",summation)
        # D = N mod |y|, H=N mod n
    D=np.mod(N,features)
    #nprint("D",D)
    H=np.mod(N,no_of_iteration)
    #nprint("H",H)
    summation=summation
    N=N
    X=len(unique_value)
    
    cw_rel=(Y*(N-D+summation)-np.square(N)+np.square(D))/(Y*(np.square(H)+n*(N-H)-D)-np.square(N)+np.square(D))
    #nprint("cw_rel",cw_rel)
    C_s=(C_s_summ/(F_max-F_min))*(1/X)
    #nprint("consistency of system",C_s)
        
        
    CW_s=(1/(N*(n-1)))*summation
    #nprint("weighted consistency of system",CW_s)
    #nprint("Individual feature consistency",consistency_for_feature_ranking)
    
    return cw_rel, CW_s, C_s

#feature_sel_stability(8)