from zipfile import ZipFile
import glob
import os

for f in glob.glob("Expiry*"):
    with ZipFile(f,"r") as zipobj:
        zipobj.extractall()


for dirpath, dirs, files in os.walk("."):
    for filename in files:
        for f in glob.glob("{}/CSV*".format(dirpath)):
            with ZipFile(f,"r") as zipobj:
                zipobj.extractall(path=os.path.join(dirpath))


