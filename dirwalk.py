import os
import random

dirs = "/home/pi/Documents/my_projects/lavictrola/music"
files = os.listdir(dirs)
print random.choice(files)
