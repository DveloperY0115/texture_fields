"""
Script for generating adversarial data for Texture Fields
"""

import argparse
import os
import sys
import shutil
import random
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--num_samples', type=int, default=100, help='Number of adversarial samples to be generated')
args = parser.parse_args()

def main():

    path_to_data = "./data/shapenet/synthetic_cars_nospecular"

    # copy the subset of original dataset
    path_to_adversarial_data = "./data/shapenet_adversarial"
    if not os.path.exists(path_to_adversarial_data):
        print("[!] Start copying data...")
        os.mkdir(path_to_adversarial_data)

        # number of samples to be copied
        num_samples = args.num_samples

        samples = os.listdir(path_to_data)
        for sample in samples:
            if num_samples == 0:
                break
            shutil.copytree(
                os.path.join(path_to_data, sample), os.path.join(path_to_adversarial_data, sample)
            )
            num_samples -= 1
        print("[!] Done.")

    # randomly shuffle data between samples
    samples = os.listdir(path_to_adversarial_data)

    for sample in tqdm(samples):

        another_sample = random.sample(samples, 1)[0]

        while sample is another_sample:
            another_sample = random.sample(samples, 1)[0]

        imgs_1 = os.path.join(path_to_adversarial_data, sample, "input_image")
        imgs_1_copy = os.path.join(path_to_adversarial_data, sample, "tmp")
        copy_directory_and_overwrite(imgs_1, imgs_1_copy)
        imgs_2 = os.path.join(path_to_adversarial_data, another_sample, "input_image")

        # swap two directories and their
        copy_directory_and_overwrite(imgs_2, imgs_1)
        copy_directory_and_overwrite(imgs_1_copy, imgs_2)
        shutil.rmtree(imgs_1_copy)

    # clean up
    print("[!] Finished generating adversarial dataset.")

    return


def copy_directory_and_overwrite(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


if __name__ == "__main__":
    main()
