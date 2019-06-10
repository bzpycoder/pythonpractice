# PROBLEM: Find the highest element in given list

# a = input().split()
# a = ['6','7','9','9','1','2']
# a = ['9','9','9','9','9','9']
# a = ['6','7','9','9','1','2']
# a = ['1','9','9','9','9','9']
# a = ['1','1','1','9','0','0']
# a = ['1','2','3','2','1']
# a = []
a = ['0']

maxn = None
for i in range(0, len(a)):
    element_current = int(a[i])
    if maxn is None or element_current > maxn:
        maxn = element_current

print(maxn)

# shorthand
print(max(a))