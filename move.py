#!/usr/bin/python3

import os
import shutil
import glob


def moveMostRecentDownload():
    # get list of files that matches pattern
    destination = "/home/anthony/Code/scripts/thumbnail-python/destination"
    pattern = "/home/anthony/Downloads/*"
    files = list(filter(os.path.isfile, glob.glob(pattern)))

    # sort by modified time
    files.sort(key=lambda x: os.path.getmtime(x))

    # get last item in list
    lastfile = files[-1]

    # print("Most recent file matching {}: {}".format(pattern, lastfile))
    # print("Most recent file is : " + lastfile)

    shutil.copy2(
        lastfile, destination)

    os.chdir(destination)
    for file in os.listdir():
        # print(file)
        new_name = "NEW_THUMBNAIL.png"
        os.rename(file, new_name)
        print("File moved from" + pattern + " to " + destination)


moveMostRecentDownload()
