# PROBLEM: Check if string has duplicate characters

s = 'Milwaakee'
#s ='abcdefghijklmnopqrstuvwxyz'

st = set(s)

# print(s,st)
# print(len(s),len(st))

if len(s) > len(st):
    print('String contains repetitive chars')
elif len(s) == len(st):
    print('String has unique chars')