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
        df.at[i,'AK']="Mod Transition Count"
        df.at[i+2,'AK']="Count"
        if st+mod-1 >= len(octant_list):
            df.at[i+1,'AK']=str(st)+"-"+str(len(octant_list)-1)
        else:
            df.at[i+1,'AK']=str(st)+"-"+str(st+mod-1)
            first = int(df.at[st+mod-1, 'Octant'])
            second = int(df.at[st+mod, 'Octant'])
            df2.loc[str(first), str(second)]+=1
            ## print(first, second)

        st=st+mod
        
        i=i+1;
        df.at[i,'AL']="To"
        df.at[i+2,'AJ'] ='From'
        i=i+1
        df.at[i,'AL']='1'
        df.at[i,'AM']='-1'
        df.at[i,'AN']='2'
        df.at[i,'AO']='-2'
        df.at[i,'AP']='3'
        df.at[i,'AQ']='-3'
        df.at[i,'AR']='4'
        df.at[i,'AS']='-4'
        df.at[i+1,'AK']='1'
        df.at[i+2,'AK']='-1'
        df.at[i+3,'AK']='2'
        df.at[i+4,'AK']='-2'
        df.at[i+5,'AK']='3'
        df.at[i+6,'AK']='-3'
        df.at[i+7,'AK']='4'
        df.at[i+8,'AK']='-4'
        i=i+1
        col_index=37
        for k in range(0,8):
            for l in range(0,8):
                df.iloc[i+k,col_index+l]=df2.iloc[k,l]
        # print(df2)
        # print(df2.iloc[1][0])

        i=i+7