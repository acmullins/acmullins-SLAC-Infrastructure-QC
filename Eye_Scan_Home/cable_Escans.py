import pandas as pd
import numpy as np
import glob
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from pylab import colorbar
import os


def genplot():
    fig, axs = plt.subplots(3, 2, figsize=(9, 9))
    fig.subplots_adjust(hspace=0.8)
    # fig.delaxes(axs[2,1])
    return fig, axs


parent_dir = "Vector5_Data/"
dir_list = os.listdir(parent_dir)

for d in dir_list:
    with PdfPages("Vector5_PDF/" + d + "_Summary.pdf") as pdf:

        # Creates a title page
        plt.figure()
        plt.axis("off")
        plt.text(0.5, 0.5, "Vector5 " + d + " Run Summary", ha="center", va="center")
        pdf.savefig()
        plt.close()

        x = 0

        # Read in the csv files
        file_list = glob.glob(parent_dir + d + "/*.csv")
        # file_list.sort(key= lambda x: str(x.split('CA')[3]))

        fig, axs = genplot()

        for f in file_list:

            df = pd.read_csv(f, skiprows=20, index_col=0)
            df = df.head(len(df) - 1)

            foo = axs[x // 2, x % 2]
            foo.set(xlabel="Unit Interval")
            foo.set(ylabel="Voltage")
            foo.set_title(f.split("/")[2], fontsize=6)
            foo.text(0.50, 0.50, "")
            foo.set_xticks(list(np.arange(-0.5, 0.7, 0.2)))
            foo.set_yticks(list(np.arange(-120, 160, 40)))

            im = foo.imshow(
                np.log10(df.values),
                cmap="jet",
                extent=[-0.5, 0.5, -120, 120],
                aspect="auto",
            )
            clb = fig.colorbar(im)
            clb.ax.set_title("Log\u2081\u2080BER", size=8)

            d_var = pd.read_csv(f, index_col=0, skipfooter=33, engine="python")
            h_area = d_var["2022.1"].iloc[7]
            v_area = d_var["2022.1"].iloc[9]
            dwell = d_var["2022.1"].iloc[11]
            # print(v_area)

            # textstr = '\n'.join(('A','Dwell BER: 1E-05'))

            stats_txt = "\n".join(["Amplitude % ", "Width %", "Dwell BER"])
            stats = "\n".join(
                ["{}".format(v_area), "{}".format(h_area), "{}".format(dwell)]
            )

            # creating the summary textbox
            props = dict(
                boxstyle="square", facecolor="white", edgecolor="none", alpha=1
            )
            fig.text(
                0.7,
                0.9,
                stats_txt,
                transform=foo.transAxes,
                fontsize=5,
                verticalalignment="top",
                bbox=props,
                ha="left",
            )
            fig.text(
                0.97,
                0.9,
                stats,
                transform=foo.transAxes,
                fontsize=5,
                verticalalignment="top",
                bbox=props,
                ha="right",
            )

            x += 1

            if x == 6:
                pdf.savefig(fig)
                plt.close(fig)
                x = 0
                fig, axs = genplot()

        if x != 0:
            pdf.savefig(fig)
            pdf.close(fig)
