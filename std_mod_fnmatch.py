import fnmatch
import os

for file in os.listdir('MyDir'):
    if fnmatch.fnmatch(file, '*.txt'):
        print(file)


for file in os.listdir('MyDir'):
    if fnmatch.fnmatch(file, '??-??-2026.log'):
        print(file)
