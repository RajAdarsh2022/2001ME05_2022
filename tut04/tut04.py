
from ast import Str
from cmath import inf, nan
from lib2to3.pytree import type_repr
import os
from csv import writer
from csv import reader
from traceback import print_tb
import numpy as np
import pandas as pd
os.system('cls')
# os.system('clear')

def octant_longest_subsequence_count():
    df = pd.read_excel('input_octant_longest_subsequence_with_range.xlsx')  
    # adding the values for avarage
    u1_avg=df['U'].mean()
    v1_avg=df['V'].mean()
    w1_avg=df['W'].mean()

    df.at[0,'u_avg']=u1_avg
    df.at[0,'v_avg']=v1_avg
    df.at[0,'w_avg']=w1_avg
    n=len(df.axes[0])
    print(n,type(n))
    # print(df['U']-u1_avg)
    #  finding the values of "V'=V - V avg" and insert in outfile using" db.at" function
    for i in range(0,n):
        df.at[i,'U_avg=U - U avg']=df['U'][i]-u1_avg
    for i in range(0,n):
        df.at[i,'V_avg=V - V avg']=df['V'][i]-v1_avg
    for i in range(0,n):
        df.at[i,'W_avg=W - W avg']=df['W'][i]-w1_avg


    octant_list=[]



    # finding the value of octant ans insert in output file
    try:
        for i in range(0,n):
            if(df.at[i,'U_avg=U - U avg']>0 and df.at[i,'V_avg=V - V avg']>0 and df.at[i,'W_avg=W - W avg']>0):
                df.at[i,"Octant"]=1
                octant_list.append(df.at[i,'Octant'])
                
            if(df.at[i,'U_avg=U - U avg']>0 and df.at[i,'V_avg=V - V avg']>0 and df.at[i,'W_avg=W - W avg']<0):
                df.at[i,'Octant']=-1
                octant_list.append(df.at[i,'Octant'])
                
            if(df.at[i,'U_avg=U - U avg']<0 and df.at[i,'V_avg=V - V avg']>0 and df.at[i,'W_avg=W - W avg']>0):
                df.at[i,'Octant']=2
                octant_list.append(df.at[i,'Octant'])
                
            if(df.at[i,'U_avg=U - U avg']<0 and df.at[i,'V_avg=V - V avg']>0 and df.at[i,'W_avg=W - W avg']<0):
                df.at[i,'Octant']=-2
                octant_list.append(df.at[i,'Octant'])
                
            if(df.at[i,'U_avg=U - U avg']<0 and df.at[i,'V_avg=V - V avg']<0 and df.at[i,'W_avg=W - W avg']>0):
                df.at[i,'Octant']=3
                octant_list.append(df.at[i,'Octant'])
                
            if(df.at[i,'U_avg=U - U avg']<0 and df.at[i,'V_avg=V - V avg']<0 and df.at[i,'W_avg=W - W avg']<0):
                    df.at[i,'Octant']=-3
                    octant_list.append(df.at[i,'Octant'])
                
            if(df.at[i,'U_avg=U - U avg']>0 and df.at[i,'V_avg=V - V avg']<0 and df.at[i,'W_avg=W - W avg']>0):
                df.at[i,'Octant']=4
                octant_list.append(df.at[i,'Octant'])
                
            if(df.at[i,'U_avg=U - U avg']>0 and df.at[i,'V_avg=V - V avg']<0 and df.at[i,'W_avg=W - W avg']<0):
                    df.at[i,'Octant']=-4
                    octant_list.append(df.at[i,'Octant'])
    except:
        print("Octant_list not found")    
    # df.at[0,'']=''
    # df.at[0,'Count']=''
    # df.at[0,'Longest Subsquence Length']=''
    # df.at[0,' Frequency']=''
    # df.at[1,'Count']='1'
    # df.at[2,'Count']='-1'
    # df.at[3,'Count']='2'
    # df.at[4,'Count']='-2'
    # df.at[5,'Count']='3'
    # df.at[6,'Count']='-3'
    # df.at[7,'Count']='4'
    # df.at[8,'Count']='-4'
    list_oct=[1,-1,2,-2,3,-3,4,-4]


    idx=1
    for i in list_oct:
        a=i
        l=0;
        r=0;
        ans=0
        while((l<=r&r<n)&(l<n)):    
            if((octant_list[l]==octant_list[r])&((octant_list[l]==a)&(octant_list[r]==a))):
                r=r+1
            else :
                # if(ans<r-l+1)
                ans=max(ans,r-l)
                l=r
                r=r+1
            if(r==n):
                ans=max(ans,r-l)
        
        
        # l=0;
        # r=0;
        # ans1=0;
        # cnt=0
        # while((l<=r&r<n)&(l<n)):    
        #     if((octant_list[l]==octant_list[r])&((octant_list[l]==a)&(octant_list[r]==a))):
        #         r=r+1
        #     else :
        #         # if(ans<r-l+1)
        #         ans1=max(ans1,r-l)
        #         if(ans1==ans):
        #             cnt=cnt+1
        #             ans1=0
        #         l=r
        #         r=r+1
        #     if(r==n):
        #         ans1=max(ans1,r-l) 
        #         if(ans1==ans):
        #             cnt=cnt+1         
        # df.at[idx,'Longest Subsquence Length']=ans
        # df.at[idx,' Frequency']=cnt
        idx+=1    


    df.to_excel("output_octant_longest_subsequence.xlsx",index=False)
octant_longest_subsequence_count()