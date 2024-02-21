import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os


# Function used to average width
def Average(j):
    if j == a_float:
        return sum(a_float) / len(a_float)
    else:
        return sum(w_float) / len(w_float)


# Generating the score for each system and parameter (amp or width)
def Score(arr, a):
    return [x / a for x in arr]


# Plotting the System Averages
def average_plot(arr1, arr2, arr3):

    x_values = range(len(arr1))
    x_labels = ["DPM02", "DPM03", "DPM12", "DPM13"]

    plt.scatter(
        range(len(arr1)), arr1, color="red", label="SLAC", marker="s", alpha=0.4
    )
    plt.scatter(
        range(len(arr2)), arr2, color="green", label="CERN", marker="d", alpha=0.3
    )
    plt.scatter(
        range(len(arr3)), arr3, color="blue", label="Edinburgh", marker="v", alpha=1
    )

    plt.xticks(x_values, x_labels)
    plt.xlabel("DPM Combination")
    plt.ylabel("Amplitude %")
    plt.title("1m MiniDP Average Eye Amplitude %")
    plt.legend()
    plt.show()


a_float_arrays = []  # List to store arrays for a_float
w_float_arrays = []  # List to store arrays for w_float

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
    # "DPM_Comp_Data/SLAC_DPM02_miniDPxy_calib_JnJn_20240201/",
    # "DPM_Comp_Data/SLAC_DPM03_miniDPxy_calib_JnJn_20240201/",
    # "DPM_Comp_Data/SLAC_DPM12_miniDPxy_calib_JnJn_20240201/",
    "DPM_Comp_Data/SLAC_DPM13_miniDPxy_calib_JnJn_20240201/",
    # CERN
    # "DPM_Comp_Data/CERN_DPM02_miniDPxy_1m/",
    # "DPM_Comp_Data/CERN_DPM03_miniDPxy_1m/",
    # "DPM_Comp_Data/CERN_DPM12_miniDPxy_1m/",
    "DPM_Comp_Data/CERN_DPM13_miniDPxy_1m/",
    # Edinburgh
    # "DPM_Comp_Data/ED_DPM02_miniDPxy_1m/",
    # "DPM_Comp_Data/ED_DPM03_miniDPxy_1m/",
    # "DPM_Comp_Data/ED_DPM12_miniDPxy_1m/",
    "DPM_Comp_Data/ED_DPM13_miniDPxy_1m/",
]


for i, parent in enumerate(parent_dir_list):
    dir_list = os.listdir(parent)

    idx = []
    w_float = []
    a_float = []

    DPM13 = []

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

            # Creation of a list of arrays for DPM setups ie DPM12_amp = [[SLAC_amp],[CERN_amp],[ED_amp]].
            w_float_arrays.append(np.array(w_float))
            a_float_arrays.append(np.array(a_float))

    avg_a = Average(a_float)
    avg_w = Average(w_float)

# Infrastructure_AVG = [DPM02, DPM03, DPM12, DPM13]
SLAC_AVG_W = [60.305, 57.880, 59.901, 59.195]
CERN_AVG_W = [63.740, 62.124, 62.326, 63.841]
ED_AVG_W = [55.456, 57.174, 62.325, 62.427]

SLAC_AVG_A = [44.085, 40.538, 48.172, 45.161]
CERN_AVG_A = [46.558, 43.656, 47.527, 46.989]
ED_AVG_A = [38.816, 38.279, 41.291, 39.678]

# average_plot(SLAC_AVG_A, CERN_AVG_A, ED_AVG_A)

# These arrays compare the SLAC system to the CERN and ED systems
CERN = a_float_arrays[1] / a_float_arrays[0]
ED = a_float_arrays[2] / a_float_arrays[0]

print(a_float_arrays[2])


# Plotting the System Averages
def average_plot1(arr1, arr2):

    plt.scatter(
        range(len(arr1)),
        arr1,
        color="green",
        label="DPM13 CERN",
        marker="d",
        alpha=0.4,
    )
    plt.scatter(
        range(len(arr2)),
        arr2,
        color="blue",
        label="DPM13 Edinburgh",
        marker="v",
        alpha=0.6,
    )

    plt.xticks(range(0, 31, 4))
    plt.xlabel("Link Index (J1-J6)")
    plt.ylabel("Score")
    plt.title("1m MiniDP Eye Amplitude Score")
    plt.vlines(x=[4.5, 9.5, 14.5, 19.5, 24.5], color="b", ymin=0, ymax=20, ls=":")
    plt.hlines(y=[0.8, 1.2], color="red", xmin=0, xmax=30, ls=":")
    plt.legend()
    plt.show()


average_plot1(CERN, ED)
