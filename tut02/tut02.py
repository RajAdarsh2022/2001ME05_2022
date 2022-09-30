import numpy as np
import pandas as pd
import math
import openpyxl

def octant_transition_count(mod):
    df = pd.read_excel('input_octant_transition_identify.xlsx')  
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


    # adding a coummn for user input ans overall count    
    df.at[2,' '] ='User input'      
    df.at[0,'Octant ID']='Overall Count'   

            
    #   inserting the feequency data
    df.at[0,'1']=octant_list.count(1)
    df.at[0,'-1']=octant_list.count(-1)
    df.at[0,'2']=octant_list.count(2)
    df.at[0,'-2']=octant_list.count(-2)
    df.at[0,'3']=octant_list.count(3)
    df.at[0,'-3']=octant_list.count(-3)
    df.at[0,'4']=octant_list.count(4)
    df.at[0,'-4']=octant_list.count(-4)





    # function for split the list into equal parts
    def list_split(listA, n):
        for x in range(0, len(listA), n):
            every_chunk = listA[x: n+x]

            if len(every_chunk) < n:
                every_chunk = every_chunk + \
                    [None for y in range(n-len(every_chunk))]
            yield every_chunk
            
    mod=5000   
    start=0;
    i=3
    df.at[2,'Octant ID']="Mod "+str(mod)
    try:
        lis=list(list_split(octant_list, mod))
    except:
        print("The function List_split not found")


    lis_size=len(lis)
            
    for x in lis:     
        ## print("x")   
        if(i-2==lis_size):       
            df.at[i,'Octant ID']=str(start)+"-"+str(30000)
        else:
            df.at[i,'Octant ID']=str(start)+"-"+str(start+mod-1)
        df.at[i,'1']=x.count(1)
        df.at[i,'-1']=x.count(-1)
        df.at[i,'2']=x.count(2)
        df.at[i,'-2']=x.count(-2)
        df.at[i,'3']=x.count(3)
        df.at[i,'-3']=x.count(-3)
        df.at[i,'4']=x.count(4)
        df.at[i,'-4']=x.count(-4)
        i+=1
        start=start+mod


    df.at[i,'Octant ID']='Verified' 
    df.at[i,'1']=octant_list.count(1)
    df.at[i,'-1']=octant_list.count(-1)
    df.at[i,'2']=octant_list.count(2)
    df.at[i,'-2']=octant_list.count(-2)
    df.at[i,'3']=octant_list.count(3)
    df.at[i,'-3']=octant_list.count(-3)
    df.at[i,'4']=octant_list.count(4)
    df.at[i,'-4']=octant_list.count(-4)


    df2=pd.DataFrame(columns=['1','-1','2','-2','3','-3','4','-4'],index=['1','-1','2','-2','3','-3','4','-4'])
    df2=df2.fillna(0)
    # print(df2)

    # print(df2['1']['1'])
    for j in range(0,n-1):
        ro=str(int(octant_list[j]))
        co=str(int(octant_list[j+1]))
        df2.loc[ro,co]+=1
    i=i+3  
    df.at[i,'Octant ID']="Overall Transition Count"
    df.at[i+2,'Octant ID']="Count"
    i=i+1;
    df.at[i,'1']="To"
    df.at[i+2,' '] ='From'
    i=i+1
    df.at[i,'1']='1'
    df.at[i,'-1']='-1'
    df.at[i,'2']='2'
    df.at[i,'-2']='-2'
    df.at[i,'3']='3'
    df.at[i,'-3']='-3'
    df.at[i,'4']='4'
    df.at[i,'-4']='-4'
    df.at[i+1,'Octant ID']='1'
    df.at[i+2,'Octant ID']='-1'
    df.at[i+3,'Octant ID']='2'
    df.at[i+4,'Octant ID']='-2'
    df.at[i+5,'Octant ID']='3'
    df.at[i+6,'Octant ID']='-3'
    df.at[i+7,'Octant ID']='4'
    df.at[i+8,'Octant ID']='-4'
    i=i+1
    col_index=13
    for k in range(0,8):
        for l in range(0,8):
            df.iloc[i+k,col_index+l]=df2.iloc[k,l]


    i=i+7
    st=0
    # lis2=np.array_split(octant_list, mod)     
    lis2 = [octant_list[i * mod:(i + 1) * mod] for i in range((len(octant_list) + mod - 1) // mod )] 
    for x in lis2:
        df2=pd.DataFrame(columns=['1','-1','2','-2','3','-3','4','-4'],index=['1','-1','2','-2','3','-3','4','-4'])
        df2=df2.fillna(0)
        # print(df2)

        # print(df2['1']['1'])
        print(len(x),end='  ')
        for j in range(0,len(x)-1):
            ro=str(int(x[j]))
            co=str(int(x[j+1]))
            df2.loc[ro,co]+=1
        
        i=i+3  
        df.at[i,'Octant ID']="Mod Transition Count"
        df.at[i+2,'Octant ID']="Count"
        if st+mod-1 >= len(octant_list):
            df.at[i+1,'Octant ID']=str(st)+"-"+str(len(octant_list)-1)
        else:
            df.at[i+1,'Octant ID']=str(st)+"-"+str(st+mod-1)
            first = int(df.at[st+mod-1, 'Octant'])
            second = int(df.at[st+mod, 'Octant'])
            df2.loc[str(first), str(second)]+=1
            ## print(first, second)

        st=st+mod
        
        i=i+1;
        df.at[i,'1']="To"
        df.at[i+2,' '] ='From'
        i=i+1
        df.at[i,'1']='1'
        df.at[i,'-1']='-1'
        df.at[i,'2']='2'
        df.at[i,'-2']='-2'
        df.at[i,'3']='3'
        df.at[i,'-3']='-3'
        df.at[i,'4']='4'
        df.at[i,'-4']='-4'
        df.at[i+1,'Octant ID']='1'
        df.at[i+2,'Octant ID']='-1'
        df.at[i+3,'Octant ID']='2'
        df.at[i+4,'Octant ID']='-2'
        df.at[i+5,'Octant ID']='3'
        df.at[i+6,'Octant ID']='-3'
        df.at[i+7,'Octant ID']='4'
        df.at[i+8,'Octant ID']='-4'
        i=i+1
        col_index=13
        for k in range(0,8):
            for l in range(0,8):
                df.iloc[i+k,col_index+l]=df2.iloc[k,l]
        # print(df2)
        # print(df2.iloc[1][0])

        i=i+7
            
    df.to_excel('output_octant_transition_identify.xlsx',index=False)

mod=5000
octant_transition_count(mod)