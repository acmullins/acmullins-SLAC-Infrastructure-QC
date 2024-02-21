import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os


parent_dir_1 = "DPM_Comp_Data/SLAC_DPM02_miniDPxy_10m/"
parent_dir_3 = "DPM_Comp_Data/SLAC_DPM03_miniDPxy_10m/"
dir_list_1 = os.listdir(parent_dir_1)
dir_list_3 = os.listdir(parent_dir_3)

plotdir_1 = "RTM03_SLAC/"
plotdir_3 = "RTM01_ED/"

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax2 = fig.add_subplot(122)

parent_dir_list = [
    "DPM_Comp_Data/SLAC_DPM02_miniDPxy_10m/",
    "DPM_Comp_Data/SLAC_DPM03_miniDPxy_10m/",
]
for i, parent in enumerate(parent_dir_list):
    dir_list = os.listdir(parent)

    idx = []
    w_float = []
    a_float = []

    legend_name = "DPM02" if i == 0 else "DPM03"

    for d1 in dir_list:
        if "." not in d1:
            file_list = glob.glob(parent + d1 + "/*.csv")
            # Splitting on [3] allows for us to properly order the channels in the scatter
            for f in file_list:
                print(f)
            file_list.sort(key=lambda x: str(x.split("/")[-1].split("J")[1]))

            x = 1

            for f1 in file_list:
                df = pd.read_csv(f1, index_col=0, skipfooter=33, engine="python")
                width = df["2022.1"].iloc[7]
                amp = df["2022.1"].iloc[9]
                idx.append(x)
                w_float.append(float(width))
                a_float.append(float(amp))
                x += 1

            label_color = "red" if i == 0 else "blue"
            marker_type = "s" if i == 0 else "d"
            size_type = 40 if i == 0 else 30
            alpha_type = 0.4 if i == 0 else 1

    ax1.scatter(
        idx,
        w_float,
        marker=marker_type,
        alpha=alpha_type,
        s=size_type,
        color=label_color,
        label=legend_name,
    )
    ax1.set_ylabel("Width %")
    ax1.set_xlabel("Link Index (J1-J6)")
    ax1.set_title("1m MiniDP Eye Width %")
    ax1.vlines(x=[5.5, 10.5, 15.5, 20.5, 25.5], color="b", ymin=0, ymax=100, ls=":")

    ax2.scatter(
        idx,
        a_float,
        marker=marker_type,
        alpha=alpha_type,
        s=size_type,
        color=label_color,
        label=legend_name,
    )
    ax2.set_ylabel("Amplitude %")
    ax2.set_xlabel("Link Index (J1-J6)")
    ax2.set_title("1m MiniDP Eye Amplitude %")
    ax2.vlines(x=[5.5, 10.5, 15.5, 20.5, 25.5], color="b", ymin=0, ymax=100, ls=":")

ax1.legend()
ax2.legend()
plt.show()
