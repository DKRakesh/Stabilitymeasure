# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import xlsxwriter
#from Feature_selection import Anova_based, infogain, t_test 
#from General_code import feature_ranking_as_values as feature

# This array we got after getting feature rank of each features in each iteration

#array=[[1,2,3,4,5],[1,2,4,3,5],[1,4,3,2,5],[1,2,3,4,5],[1,3,2,4,5],[4,1,2,3,5],[2,1,3,4,5],[4,3,5,1,2],[2,5,1,3,4],[3,4,5,1,2]]
#array_ideal=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]






def feature_ra_stability(path,path_2):
    
    data=pd.read_excel(path,header=None)
    data=np.array(data)
    instance,features=np.shape(data)
    subset_size=int(0.50*features)
    print("subset size",subset_size)
    
    data_2=pd.read_excel(path_2,header=None)
    data_2=np.array(data_2)
    
    print(data_2)
    
    subset_iterated_feature_rank_values=data[:,0:subset_size]
    
    '''
    subset_size=subset_size_passed
    
    no_of_iteration=10
    
    
    iterated_feature_rank_values=feature.feature_position(no_of_iteration)
    instances,dimension=np.shape(iterated_feature_rank_values)
    
    
    print("jfg",iterated_feature_rank_values)
    subset_iterated_feature_rank_values=np.zeros((no_of_iteration,subset_size))
    
    for i in range(no_of_iteration):
        
        for j in range(subset_size):
            subset_iterated_feature_rank_values[i][j]=iterated_feature_rank_values[i][j]
            
    ''' 
       
    #nprint("subset",subset_iterated_feature_rank_values)
    unique_value=np.unique(subset_iterated_feature_rank_values)
    print("unique features",unique_value)
    '''
    Start of C_f code
    
    c_f for each feature present in the subset of features
    
    '''
    no_of_iteration=50
    feature_2_values=np.zeros((50,len(unique_value)))
    for i in range(len(unique_value)):
        temp_2=data_2[:,[unique_value[i]]]
        #nprint("temp 2",np.shape(temp_2))
        #feature_2_values=np.concatenate((feature_2_values,temp_2),axis=1)
        feature_2_values[:,[i]]=temp_2
        #nprint("temp 21",np.shape(feature_2_values[:,[i]]))
        #nprint(feature_2_values)
    #nprint("values",np.shape(feature_2_values))    
    
    
    '''new hide
    F_max=no_of_iteration
    F_min=1
    consistency_for_feature_ranking=[]
    
    for i in range(len(unique_value)):
        temp=unique_value[i]
        print("temp",temp)
        length=0
        for j in range(no_of_iteration):
            for k in range(len(unique_value)):
            #nfor k in range(subset_size):
                if feature_2_values[j][k]==temp:
                #nif subset_iterated_feature_rank_values[j][k]==temp:
                    length=length+1
                    print("length",length)
        
        c_f=((length-1)/(F_max-F_min))
        print("c_f",c_f)
        consistency_for_feature_ranking.append(c_f)        
    new hide '''
    #nprint("consistency for feature ranking",consistency_for_feature_ranking)
    '''
    #End of C_f code
    
    '''
    
    #narray=np.array(subset_iterated_feature_rank_values)
    array=np.array(feature_2_values)
    
    print("array",array)
    
    iteration, features=np.shape(array)
    
    #nprint("array",iteration,features)
    #unique 
    similarity_index=[]
    rank_stability=[]
    for f in range(features):
        temp_feature=array[:,f]
        #nprint("temp_features",temp_feature)
        unique=np.unique(temp_feature)
        #nprint("unique",unique)
        #nprint("maximum occurence of any number")
        count=[]
        for i in range(len(unique)):
            temp_unique=unique[i]
            temp_count=0
            for j in range(len(temp_feature)):
                if temp_unique==temp_feature[j]:
                    temp_count=temp_count+1
                    
            count.append(temp_count)
                    
        #nprint("count array",count)
        count=np.array(count)
        max_occu=max(count)
        #nprint("max_occu",max_occu)
        max_occu_indices=0
        for k in range(len(count)):
            if count[k]==max_occu:
                max_occu_indices=k
        #nprint("maximum occurence of rank for feature f",f+1,"is",unique[max_occu_indices])
        most_stable_rank=unique[max_occu_indices]  
        
        rank_difference=[]
        for i in range(len(unique)):
            rank_difference.append(abs(most_stable_rank-unique[i]))
        max_rank_difference=max(rank_difference)
        #creating array of most stable rank
        
        creating_stable_array=[]
        creating_difference_array=[]
        for c in range(len(temp_feature)):
            creating_stable_array.append(unique[max_occu_indices])
            creating_difference_array.append(max_rank_difference)
         
        #nprint("creas",creating_stable_array)
        #nprint("cread",creating_difference_array)
        S_dash=features
        #nprint("S_dash",S_dash)
        max_deviation=0
        for l in range(iteration):
            max_deviation=max_deviation+abs(creating_difference_array[l])
        #nprint("max_deviation",max_deviation)
        actual_deviation=0
        for l in range(iteration):
            actual_deviation=actual_deviation+abs(creating_stable_array[l]-temp_feature[l])
        #nprint("actual deviation",actual_deviation)
        
        if len(unique)==1:
            rank_stability.append(1)
        else:
            rank_stability.append(1-(actual_deviation/max_deviation))
    #nprint("rank_stability",rank_stability)
        
    temp_index=0    
    for j in range(len(rank_stability)): 
        temp_index=temp_index+rank_stability[j]
    
    system_index=temp_index/len(rank_stability)
        
    
    '''
        sqaure_root1=0
        sqaure_root2=0
        product_sum=0
        for s in range(len(temp_feature)):
            sqaure_root1=sqaure_root1+(np.square(temp_feature[s]))
            sqaure_root2=sqaure_root2+(np.square(creating_array[s]))
            product_sum=product_sum+((temp_feature[s])*(creating_array[s]))
        square_root=(np.sqrt(sqaure_root1))*(np.sqrt(sqaure_root2))
        cosine_similarity=product_sum/square_root
        
        #nprint("cosine similarity", cosine_similarity)
        similarity_index.append(cosine_similarity)
    
        
#    print("consistency feature ranking",consistency_for_feature_ranking)
    print("similarity index",similarity_index)    
    
    System_feature_rank_consistency=0
    
    for i in range(len(unique)):
        #ntemp=consistency_for_feature_ranking[i]*similarity_index[i]
        temp=similarity_index[i]
        System_feature_rank_consistency=System_feature_rank_consistency+temp
        
    System_index=(System_feature_rank_consistency/len(unique))
        
    print("system_index",System_feature_rank_consistency)
    
    #nprint(similarity_index)
    '''
    return system_index, rank_stability
         
        
    
    #return similarity_index

#feature_ra_stability(4)