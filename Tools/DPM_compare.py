import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

# Make sure plot titles correspond with cable length and DPM labels are correctly inputed before running

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))

parent_dir_list = [
    # ------------------------------------------
    # 10m cables
    # SLAC
    # "DPM_Comp_Data/SLAC_DPM13_miniDPxy_10m/"
    # "DPM_Comp_Data/SLAC_DPM03_miniDPxy_10m/",
    # "DPM_Comp_Data/SLAC_DPM12_miniDPxy_10m/",
    # "DPM_Comp_Data/SLAC_DPM13_miniDPxy_10m/",
    # ------------------------------------------
    # 1m cables
    # SLAC
    "DPM_Comp_Data/SLAC_DPM02_miniDPxy_calib_JnJn_20240201/",
    "DPM_Comp_Data/SLAC_DPM03_miniDPxy_calib_JnJn_20240201/",
    "DPM_Comp_Data/SLAC_DPM12_miniDPxy_calib_JnJn_20240201/",
    "DPM_Comp_Data/SLAC_DPM13_miniDPxy_calib_JnJn_20240201/",
    # CERN
    # "DPM_Comp_Data/CERN_DPM02_miniDPxy_1m/",
    # "DPM_Comp_Data/CERN_DPM03_miniDPxy_1m/",
    # "DPM_Comp_Data/CERN_DPM12_miniDPxy_1m/",
    # "DPM_Comp_Data/CERN_DPM13_miniDPxy_1m/",
    # Edinburgh
    # "DPM_Comp_Data/ED_DPM02_miniDPxy_1m/",
    # "DPM_Comp_Data/ED_DPM03_miniDPxy_1m/",
    # "DPM_Comp_Data/ED_DPM12_miniDPxy_1m/",
    # "DPM_Comp_Data/ED_DPM13_miniDPxy_1m/",
]


plotConfigs = {
    0: {
        "label": "DPM02 SLAC",
        "color": "red",
        "marker": "X",
        "s": 40,
        "alpha": 0.4,
    },
    1: {
        "label": "DPM03 SLAC",
        "color": "blue",
        "marker": "h",
        "s": 60,
        "alpha": 0.3,
    },
    2: {
        "label": "DPM12 SLAC",
        "color": "black",
        "marker": "p",
        "s": 30,
        "alpha": 0.3,
    },
    3: {
        "label": "DPM13 SLAC",
        "color": "green",
        "marker": "s",
        "s": 50,
        "alpha": 0.3,
    },
}
for i, parent in enumerate(parent_dir_list):
    dir_list = os.listdir(parent)

    idx = []
    w_float = []
    a_float = []

    for d1 in dir_list:
        if "." not in d1:
            file_list = glob.glob(parent + d1 + "/*.csv")
            # Splitting on [3] allows for us to properly order the channels in the scatter

            file_list.sort(key=lambda x: str(x.split("/")[-1].split("J")[1]))
            x = 1

            for f1 in file_list:
                df = pd.read_csv(f1, index_col=0, skipfooter=33, engine="python")
                col_name = df.columns[0]
                width = df[col_name].iloc[7]
                amp = df[col_name].iloc[9]
                idx.append(x)
                w_float.append(float(width))
                a_float.append(float(amp))
                x += 1

    ax1.scatter(idx, w_float, **plotConfigs[i])
    ax1.set_ylabel("Width %")
    ax1.set_xlabel("Link Index (J1-J6)")
    ax1.set_title("1m MiniDP Eye Width %")
    ax1.vlines(x=[5.5, 10.5, 15.5, 20.5, 25.5], color="b", ymin=0, ymax=100, ls=":")

    ax2.scatter(idx, a_float, **plotConfigs[i])
    ax2.set_ylabel("Amplitude %")
    ax2.set_xlabel("Link Index (J1-J6)")
    ax2.set_title("1m MiniDP Eye Amplitude %")
    ax2.vlines(x=[5.5, 10.5, 15.5, 20.5, 25.5], color="b", ymin=0, ymax=100, ls=":")

ax1.legend()
ax2.legend()
plt.show()
