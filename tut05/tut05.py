import pandas as pd
import numpy as np
import math

from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/N6PBd4XdnEw
def octant_range_names(mod=5000):
    octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}
    # Reading Excel File
    try:
        df = pd.read_excel('octant_input.xlsx')
        rows = len(df)
    except:
        print("There was some error in reading the file")
        exit()

    try:
        # Calculating Average Values
        # Calculating Average Value of U, V, W
        df.at[0, "U Avg"] = df['U'].mean()
        df.at[0, "V Avg"] = df['V'].mean()
        df.at[0, "W Avg"] = df['W'].mean()

        # Calculating U', V', W' 
        #for i in range(0,rows):
        df["U'=U - U avg"] = df['U'] - df.at[0, "U Avg"]
        df["V'=V - V avg"] = df['V'] - df.at[0, "V Avg"]
        df["W'=W - W avg"] = df['W'] - df.at[0, "W Avg"]
    except:
        print("There was some error in calculating the average")
        exit()

    try:
        l=[]
    except:
        print("Error in inserting columns.")
        exit()

    try:
        # Calculating the octant values
        for i in range(0, rows):
            if df.at[i,"U'=U - U avg"] >= 0 and  df.at[i,"V'=V - V avg"] >= 0:
                if df.at[i,"W'=W - W avg"] >= 0:
                  df.at[i, 'Octant'] = 1
                else:
                  df.at[i, 'Octant'] = -1
            elif df.at[i,"U'=U - U avg"] < 0 and  df.at[i,"V'=V - V avg"] >= 0:
                if df.at[i,"W'=W - W avg"] >= 0:
                  df.at[i, 'Octant'] = 2
                else:
                  df.at[i, 'Octant'] = -2
            elif df.at[i,"U'=U - U avg"] < 0 and  df.at[i,"V'=V - V avg"] < 0:
                if df.at[i,"W'=W - W avg"] >= 0:
                  df.at[i, 'Octant'] = 3
                else:
                  df.at[i, 'Octant'] = -3
            elif df.at[i,"U'=U - U avg"] >= 0 and  df.at[i,"V'=V - V avg"] < 0:
                if df.at[i,"W'=W - W avg"] >= 0:
                  df.at[i, 'Octant'] = 4
                else:
                  df.at[i, 'Octant'] = -4
            l.append(df.at[i, 'Octant'])

        df.at[1, ''] = "User Input"
        df.at[0, 'Octant ID'] = "Overall Count"
        df.at[1, 'Octant ID'] = "Mod "+ str(mod) 

        df.at[0, "1"] = l.count(1)
        df.at[0, "-1"] = l.count(-1)
        df.at[0 ,"2"] = l.count(2)
        df.at[0 ,"-2"] = l.count(-2)
        df.at[0 ,"3"] = l.count(3)
        df.at[0 ,"-3"] = l.count(-3)
        df.at[0 ,"4"] = l.count(4)
        df.at[0 ,"-4"] = l.count(-4)
    except:
        print("Error in counting octant values.")
        exit()
    
   
        
    
            
    try:
        df.to_excel('octant_output_ranking_excel.xlsx', index=False)
    except:
        print("Error in writing to excel file")
        exit()
###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


mod=5000 
octant_range_names(mod)



#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
