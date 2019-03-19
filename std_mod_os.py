import os

# List Items using os.walk
path = '.'
for anchor, dirs, files in os.walk(path):
    for file in files:
        print(file)

    for name in dirs:
        print(name)



# List Items without using os.walk
def list_items(root):
    contents = os.listdir(root)
    for i in contents:
        p = os.path.join(root, i)               # windows path
        path = p.replace('\\', '/')             # windows path
        if os.path.isdir(path):
            list_items(path)
        else:
            print(path)


list_items('.')


s = 'MyDir'
a = 'C:/Users/Bharath/Desktop/PyProjects/PythonPractice/MyDir'

print(os.path.curdir)               # Get current dir

print(os.path.exists(s))            # path exists
print(os.path.isdir(s))             # is Directory
print(os.path.isfile(s))            # is file
print(os.path.isabs(s))             # is absolute path?

print(os.path.abspath(s))           # Get absolute path
print(os.path.basename(a))          # Get base path
print(os.path.dirname(a))           # Get dir path

print(os.path.join(os.path.dirname(a),os.path.basename(a)))
print(os.path.join(os.path.dirname(a),os.path.basename(a)) == a)