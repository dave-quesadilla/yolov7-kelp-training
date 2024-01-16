from os import listdir, mkdir
from os.path import exists, join, split, basename
from shutil import copyfile, rmtree
from sklearn.model_selection import train_test_split
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("seed", default = None, nargs = "?", help = "seed for random split (optional)")

args = parser.parse_args()

seed = args.seed

source_dir = join("sporophytes", "all")
source_dir_img = join(source_dir, "images")
source_dir_labels = join(source_dir, "labels")
imgs = listdir(source_dir_img)


print(f" found {len(imgs)} images")

train_imgs, test_imgs = train_test_split(imgs, test_size=.2, train_size=.8, random_state=seed)

print(f"split into {len(train_imgs)} training images and {len(test_imgs)} validation images")

train_dir =join("sporophytes", "train")
train_dir_imgs = join(train_dir, "images")
train_dir_labels = join(train_dir, "labels")

test_dir = join("sporophytes", "test")
test_dir_imgs = join(test_dir, "images")
test_dir_labels = join(test_dir, "labels")

locations = [train_dir, test_dir]

for loc in locations:
    if exists(loc):
        print(f"found existing {split(loc)[1]} split, deleting...")
        rmtree(loc)
    mkdir(loc)
    mkdir(join(loc, "images"))
    mkdir(join(loc, "labels"))

for img in train_imgs:
    name = basename(img).split(".")[0]
    label = f"{name}.txt"
    copyfile(join(source_dir_img, img), join(train_dir_imgs, img))
    copyfile(join(source_dir_labels, label), join(train_dir_labels, label))

for img in test_imgs:
    name = basename(img).split(".")[0]
    label = f"{name}.txt"
    copyfile(join(source_dir_img, img), join(test_dir_imgs, img))
    copyfile(join(source_dir_labels, label), join(test_dir_labels, label))



