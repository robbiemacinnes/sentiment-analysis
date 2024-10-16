import pyprind
import pandas as pd
import os
import sys
import numpy as np

file_path = "../data/external/aclImdb"

labels = {"pos": 1, "neg": 0}
pbar = pyprind.ProgBar(50000, stream=sys.stdout)

data = []  # Collect data in a list first
for s in ("test", "train"):
    for l in ("pos", "neg"):
        path = os.path.join(file_path, s, l)
        for file in sorted(os.listdir(path)):
            with open(os.path.join(path, file), "r", encoding="utf-8") as infile:
                txt = infile.read()
            data.append([txt, labels[l]])
            pbar.update()

# Convert the list into a DataFrame
df = pd.DataFrame(data, columns=["review", "sentiment"])

np.random.seed(0)
df = df.reindex(np.random.permutation(df.index))
df.to_csv("../data/processed/movie_data.csv", index=False, encoding="utf-8")
