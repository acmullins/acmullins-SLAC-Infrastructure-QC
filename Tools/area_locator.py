import pandas as pd

file = "Run_Data/DP13-Run2-20230622/Scan_3J1D0-1J1D3.csv"

df = pd.read_csv(file,skipfooter=33, engine = 'python')
v_area = df["2022.1"].iloc[9]
h_area = df["2022.1"].iloc[7]

print(h_area)
print(v_area)
