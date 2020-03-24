import os
import glob

for dirpath, dirs, files in os.walk("."):
    for f in glob.glob("{}/BANKNIFTY*".format(dirpath)):
        print(f)
