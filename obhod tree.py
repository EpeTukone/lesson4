import os
for root_dir, dirs, files in os.walk("c:/pyt"):
    print("root_dir is {}, dirs are {}, files are {}".format(root_dir, dirs, files))
