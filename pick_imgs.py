"""
Simple Python script for picking generated outputs.
"""

import os
import argparse
import random
import shutil
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("--num_imgs", type=int, default=1000, help="Number of images to be picked")
parser.add_argument(
    "--paths",
    type=tuple,
    default=(
        "out/singleview/car/eval_fix/condition",
        "out/singleview/car/eval_fix/fake",
        "out/singleview/car/eval_fix/real",
    ),
    help="Path to image database",
)
args = parser.parse_args()


def main():

    # unpack tuple containing path
    path_condition, path_fake, path_real = args.paths
    num_imgs = args.num_imgs

    # randomly pick 'num_imgs' number of images
    picked_imgs = random.sample(os.listdir(path_fake), num_imgs)

    if not os.path.exists("./picked_imgs"):
        os.mkdir("./picked_imgs")
        os.mkdir("./picked_imgs/condition")
        os.mkdir("./picked_imgs/fake")
        os.mkdir("./picked_imgs/real")

    # copy selected images to destination
    for picked_img in tqdm(picked_imgs):

        img_condition = os.path.join(path_condition, picked_img)
        img_fake = os.path.join(path_fake, picked_img)
        img_real = os.path.join(path_real, picked_img)

        # shutil.copy(
        #    img_condition, os.path.join("./picked_imgs/condition", picked_img),
        # )

        if os.path.exists(img_fake):
            shutil.copy(img_fake, os.path.join("./picked_imgs/fake", picked_img))
        if os.path.exists(img_real):
            shutil.copy(img_real, os.path.join("./picked_imgs/real", picked_img))


if __name__ == "__main__":
    main()
