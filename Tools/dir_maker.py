import os 

parent_dir = "Loss_Test_Data/"
dir_list = os.listdir(parent_dir)

plotdir = "Cable_Loss_pdf/"

if not os.path.isdir(plotdir):
    os.mkdir(plotdir)