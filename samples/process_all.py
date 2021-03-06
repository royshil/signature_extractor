import glob
import os
import sys
from multiprocessing import Pool

import cv2

from extractor.extract import extract_signature

DEBUG = os.environ.get("DEBUG") == "1"


def process_file(name: str):
    print(name)
    img = cv2.imread(name, cv2.IMREAD_COLOR + cv2.IMREAD_IGNORE_ORIENTATION)

    basename, ext = os.path.splitext(name)
    outname = basename + ".out" + ext

    cv2.imwrite(outname, extract_signature(img, enable_debug=DEBUG))


def main():
    files = sys.argv[1:]

    if DEBUG:
        for file in files:
            process_file(file)
    else:
        Pool(8).map(process_file, files, chunksize=1)


main()
