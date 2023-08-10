import feature_selection_stability2 as fss
import feature_ranking_stability2 as frs
import xlsxwriter
import numpy as np
import pandas as pd

folder_file=["Adult_feature_ranking/"]
        
#folder_file=["feature_ranking_ionosphere/","feature_ranking_onlineshoppers/","feature_ranking_SCADI/","feature_ranking_australia/","Adult_feature_ranking/"]

#folder_file=["Adult_feature_ranking/"]

filter_file=["ranova.xlsx","rfisher.xlsx","rinfogain.xlsx","rrelief.xlsx","rsvm.xlsx","rfsp.xlsx"]

for i in range(1):
    path="/content/drive/My Drive/CBFS/high_dimensional/"
    temp_folder=path+folder_file[i]
    temp_folder_2=temp_folder+"feature_ranking_2/"
    temp_write_folder=temp_folder+"stability/"
    initial=1
    for j in range(6):
        temp_read=temp_folder_2+filter_file[j]
        temp_write=temp_write_folder+"fs"+filter_file[j]
        workbook1=xlsxwriter.Workbook(temp_write)
        worksheet1=workbook1.add_worksheet()    
        
        
        f_not=0.7
        temp=1
        k=0
        while initial>0:
            cw_rel, CW_s, C_s=fss.feature_sel_stability(temp_read,temp)
            worksheet1.write(k,0,initial)
            worksheet1.write(k,1,CW_s)
            worksheet1.write(k,2,C_s)
            temp=initial-f_not
            k=k+1
            print("consistency for feature ranking",cw_rel, CW_s, C_s)
            print("")
            
        workbook1.close()    
        
        
        
    
    
    '''
    temp_write=temp_folder+"rs.xlsx"
    workbook1=xlsxwriter.Workbook(temp_write)
    worksheet1=workbook1.add_worksheet()
    k=0
    for j in range(6):
        temp_read=temp_folder+filter_file[j]
        print(filter_file[j])
        print(temp_read)
        print(temp_write)
        print("kj",np.shape(pd.read_excel(temp_read)))
        temp_read_2=temp_folder_2+filter_file[j]
        print(temp_read_2)
        print("kjg",np.shape(pd.read_excel(temp_read_2)))
        
        
        consistency_for_feature_ranking, cw_rel, unique_value=fss.feature_sel_stability(temp_read_2)
        
        system_index, rank_stability=frs.feature_ra_stability(temp_read_2,temp_read_2)
        
        #nprint("feature rank",system_index)
        #nprint("features",unique_value)
        #nprint("cumulative stability",cw_rel)
        #nprint("each feature consistency",consistency_for_feature_ranking)
        print("cumulative system_index",system_index)
        print("each feature system index",rank_stability)
        print("feature stability",cw_rel)   
        #print("rank_stabilit",rank_stability)
        
        k=k+0
        worksheet1.write(k,4,filter_file[j])
        k=k+1
        #print("k value",k,j)
        worksheet1.write(k,4,"feature stability")
        k=k+1
        
        for l in range(len(unique_value)):
            worksheet1.write(k,l,unique_value[l])
        k=k+1
        worksheet1.write(k,4,cw_rel)
        worksheet1.write(k,5,np.mean(consistency_for_feature_ranking))
        k=k+1
        for l in range(len(unique_value)):
            worksheet1.write(k,l,consistency_for_feature_ranking[l])
        k=k+1
        worksheet1.write(k,4,"rank stability")
        k=k+1
        
        
        worksheet1.write(k,4,system_index)
        k=k+1    
        for l in range(len(unique_value)):
            worksheet1.write(k,l,rank_stability[l])
        k=k+1
        worksheet1.write(k,4,"")
        k=k+1
        #print("k value",k)
        #k=k+6
        #for k in range(len(rank_stability)):
        #    worksheet1.write(i+2,k,rank_stability[k])
        
        #for k in range(len(rank_stability)):
        #    worksheet1.write(i+1,j,system_index)
        #    worksheet1.write(i+1,j+k,rank_stability[k])
            
            
    workbook1.close()
    '''    
            
