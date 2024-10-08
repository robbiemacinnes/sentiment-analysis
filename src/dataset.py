import pyprind
import pandas as pd
import os
import sys

file_path = "../data/external/aclImdb"

labels = {"pos": 1, "neg": 0}
pbar = pyprind.ProgBar(50000, stream=sys.stdout)

df = pd.DataFrame()
for s in ("test", "train"):
    for l in ("pos", "neg"):
        path = os.path.join(file_path, s, l)
        for file in sorted(os.listdir(path)):
            with open(os.path.join(path, file), "r", encoding="utf-8") as infile:
                txt = infile.read()
            df = df.append([[txt, labels[1]]], ignore_index=True)
            pbar.update()

df.columns = ["review", "sentiment"]
