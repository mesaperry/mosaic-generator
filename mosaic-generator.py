import os
import shutil
import sys
import random
from google_images_download import google_images_download

sys.path.insert(1, 'mosaic-master/')

import mosaic


IMAGES = "images/"


def downloadImages():
    last_file = open("last.txt", "r")
    last = last_file.readline()
    last_file.close()

    if os.path.isdir(IMAGES):
        if os.listdir(IMAGES) and last == sys.argv[1]:
            return

    shutil.rmtree("images", ignore_errors=True)

    response = google_images_download.googleimagesdownload()
    arguments = {
        "keywords": sys.argv[1],
        "format": "jpg",
        "size": "medium",
        "output_directory": IMAGES,
        "no_directory": True,
    }
    response.download(arguments)

    last_file = open("last.txt", "w+")
    last_file.write(sys.argv[1])
    last_file.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python {} <keyword>".format(sys.argv[0]))
        quit()

    downloadImages()

    imgs = os.listdir(IMAGES)
    if len(imgs) < 2:
        print("Insufficient number of images")
        quit()

    background = os.path.join(IMAGES, random.choice(imgs))

    mosaic.mosaic(background, IMAGES)