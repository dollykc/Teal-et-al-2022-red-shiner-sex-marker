#%% Pick out the loci with the highest number of samples genotyped
#Note! The output is not printed in order. For example, M2n3 may print after M6n5.
import glob, os
import pandas as pd
import re
Total_lib = input('How many individuals went into Stacks?')
upper75_lib = (int(Total_lib))*.75
upper50_lib = (int(Total_lib))*.5
print("75% of that is", upper75_lib)
print("50% of that is", upper50_lib)
with open("./redshiner/outfileXY.txt", "w") as outfile: #creating a file to dump all the results
    for filename in glob.iglob('./redshiner/*_XY.txt', recursive=True):#look at all the files that end with "_XY.txt"
        if os.path.isfile(filename):
            df= pd.read_csv(filename, sep='\t', header=0) #index_col='Locus') #make a dataframe from the text file
            TG=df[["Total_geno"]] # this is a data frame with just the Total_geno column
            TGlist= TG.values.tolist() # changing it to a list so we can get the max
            max_TG= (max(TGlist)) # getting the max in the total genotyped, but still list
            max_TG = int("".join(str(i) for i in max_TG))#now changing from list to integer so it can be used below
            TG_line=df[df.Total_geno == max_TG]# gives all the info for the locus with the most genotyped  
            upper75_TG_line=df[df.Total_geno >= upper75_lib] # lines with total genotyped >= 75% quartile
            upper50_TG_line=df[df.Total_geno >= upper50_lib] # lines with total genotyped >= 50% quartile
            upper50_TG_line=upper50_TG_line.sort_values(by=['Total_geno','Locus'], ascending = [False, True]) #sorting the results by locus, then by most genotyped
            f=re.search(r'M\dn\d_XY\.txt$', filename)#making variable with part of file name M*n*.txt
            upper50_TG_line['File'] = f.group(0) #adding a column to df that has the file the results came from
            upper50_TG_line.to_csv('./redshiner/outfileXY.txt', mode='a') #appending the results from each iteration into one outfile
            print("From", filename, "Here are the ones with greater than or equal to", upper50_lib, ":\n", upper50_TG_line)  
#%%
df.head(5)
df1=df['Locus']
print(df1)
  
#%%
outfile.close()
