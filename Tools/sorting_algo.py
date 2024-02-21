import glob

file_list = glob.glob('Run_Data/DP13-run6-2-20230626/*.csv')

allfiles = glob.glob('Run_Data/DP13-run6-2-20230626/*.csv')   
allfiles.sort(key= lambda x: str(x.split('J')[2])) 
#allfiles.sort(key= lambda x: str(x.split('J')[2].split('.')[0]))

print(file_list)
print(allfiles)

even_file_list = glob.glob('Run_Data_Evens/DP13_J246_run1/*.csv')

even_allfiles = glob.glob('Run_Data_Evens/DP13_J246_run1/*.csv')   
even_allfiles.sort(key= lambda x: str(x.split('J')[2])) 

#print(even_file_list)
#print(even_allfiles)
