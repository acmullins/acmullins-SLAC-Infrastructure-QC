import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os


parent_dir = "Infrastructure_Test_Data/RTM03_runs/"
dir_list = os.listdir(parent_dir)

fig, (ax1, ax2) = plt.subplots(1,2,figsize = (16,10))

plotdir = "RTM03_Scatter/"

if not os.path.isdir(plotdir):
    os.mkdir(plotdir)

for d in dir_list:

    if "." not in d:
        legend_name = d.split("_")[0]
        file_list = glob.glob(parent_dir+d+'/*.csv')
        #Splitting on [3] allows for us to properly order the channels in the scatter
        file_list.sort(key= lambda x: str(x.split('J')[3])) 

        x = 1

        idx = []
        w_float = []
        a_float = []

        for f in file_list:
            df = pd.read_csv(f,index_col=0,skipfooter=33, engine = 'python')
            width = df["2022.1"].iloc[7]
            amp = df["2022.1"].iloc[9]
            idx.append(x)
            w_float.append(float(width))
            a_float.append(float(amp))
            x += 1

        #PLOT GENERATION

        ax1.set_ylabel("Width %")
        ax1.set_xlabel("Link Index (J1-J6)")
        ax1.set_title("Run Data Eye Width %")
        ax1.plot(idx, w_float, '.', label=legend_name)
        ax1.legend()
        ax1.vlines(x = [5.5, 10.5, 15.5, 20.5, 25.5], color = 'b', ymin = 0, ymax = 100, ls = ':')

        ax2.set_ylabel("Amplitude %")
        ax2.set_xlabel("Link Index (J1-J6)")
        ax2.set_title("Run Data Eye Amplitude %")
        ax2.plot(idx, a_float, '.', label=legend_name)
        ax2.legend()
        ax2.vlines(x = [5.5, 10.5, 15.5, 20.5, 25.5], color = 'b', ymin = 0, ymax = 100, ls = ':')


    #elif "mini" in d:
    #    file_list = glob.glob(parent_dir+d+'/*.csv')
    #    file_list.sort(key= lambda x: str(x.split('J')[1].split('.')[0])) 
    #
    #    x = 1
    #
    #    idx = []
    #    w_float = []
    #    a_float = []
    #
    #    for f in file_list:
    #        df = pd.read_csv(f,index_col=0,skipfooter=33, engine = 'python')
    #        width = df["2022.1"].iloc[7]
    #        amp = df["2022.1"].iloc[9]
    #        idx.append(x)
    #        w_float.append(float(width))
    #        a_float.append(float(amp))
    #        x += 1
    #
    #    ax1.set_xlabel("Link Index (J1-J6)")
    #    ax1.set_title("Run Data Eye Width %")
    #    ax1.bar(idx, w_float, color = 'tan')
    #    ax1.vlines(x = [5.5, 10.5, 15.5, 20.5, 25.5], color = 'b', ymin = 0, ymax = 100, ls = ':')
    #
    #    ax2.set_ylabel("Amplitude %")
    #    ax2.set_xlabel("Link Index (J1-J6)")
    #    ax2.set_title("Run Data Eye Amplitude %")
    #    ax2.bar(idx, a_float, color = 'tan')
    #    ax2.vlines(x = [5.5, 10.5, 15.5, 20.5, 25.5], color = 'b', ymin = 0, ymax = 100, ls = ':')
    
plt.savefig(plotdir+"/"+"Multi_Run_Scatter.png")