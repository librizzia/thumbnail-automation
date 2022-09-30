import os
import glob

# get list of files that matches pattern
pattern = "/home/anthony/Downloads/*"
files = list(filter(os.path.isfile, glob.glob(pattern)))

# sort by modified time
files.sort(key=lambda x: os.path.getmtime(x))

# get last item in list
lastfile = files[-1]

# print("Most recent file matching {}: {}".format(pattern, lastfile))
print("Most recent file is : " + lastfile)
