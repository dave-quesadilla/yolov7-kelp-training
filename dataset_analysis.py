import pandas as pd 
from os import listdir
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
label_files = listdir("sporophytes/all/labels/")


all_labels = pd.concat([pd.read_csv( "sporophytes/all/labels/" + label, names=["class_num", "x", "y", "w", "h"], sep = "\s+") for label in label_files])

all_labels["area (pixels)"] = (all_labels["w"] * all_labels["h"]) * 896 * 684
all_labels["class"] = all_labels["class_num"].map(dict(zip(range(6), [ "Attached Alive", "Attached Dead", "Detached Alive", "Detached Dead", "Embryo", "Sporophyte"])))

sns.catplot(all_labels, x = "area (pixels)", y = "class", hue = "class", kind = "violin",  log_scale = True)
ax = plt.gca()
plt.savefig("sizes")

plt.close("all")
counts = pd.DataFrame(all_labels["class"].value_counts())
print(counts)
sns.barplot(counts, y = counts.index, x = "count")
plt.tight_layout()
plt.savefig("counts")

