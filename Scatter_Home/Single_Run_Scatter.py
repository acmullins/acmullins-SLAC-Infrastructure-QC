import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os


parent_dir = "Vector5_Data/"
dir_list = os.listdir(parent_dir)


plotdir = "Z_Scatter_1/"

if not os.path.isdir(plotdir):
    os.mkdir(plotdir)

for d in dir_list:

    if "." not in d:
        file_list = glob.glob(parent_dir + d + "/*.csv")
        file_list.sort(key=lambda x: str(x.split("A")[1]))
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 10))

        x = 1

        idx = []
        w_float = []
        a_float = []
        # print(d)
        # print(a_float)

        for f in file_list:
            df = pd.read_csv(f, index_col=0, skipfooter=33, engine="python")
            width = df["2022.1"].iloc[7]
            amp = df["2022.1"].iloc[9]
            idx.append(x)
            w_float.append(float(width))
            a_float.append(float(amp))
            x += 1

        print(d)
        print(a_float)

        # PLOT GENERATION

        ax1.set_ylabel("Width %")
        ax1.set_xlabel("Link Index (J1-J6)")
        ax1.set_title(d + " Eye Width %")
        ax1.plot(idx, w_float, ".")
        ax1.vlines(
            x=[5.5, 10.5, 15.5, 20.5, 25.5],
            color="b",
            ymin=0,
            ymax=max(w_float),
            ls=":",
        )

        ax2.set_ylabel("Amplitude %")
        ax2.set_xlabel("Link Index (J1-J6)")
        ax2.set_title(d + " Eye Amplitude %")
        ax2.plot(idx, a_float, ".")
        ax2.vlines(
            x=[5.5, 10.5, 15.5, 20.5, 25.5],
            color="b",
            ymin=0,
            ymax=max(a_float),
            ls=":",
        )

        plt.savefig(plotdir + "/" + d + ".png")


# name of pdf .split("/")[1]
