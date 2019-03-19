
# a = input().split()
# a = ['6','7','9','9','1','2']
# a = ['9','9','9','9','9','9']
# a = ['6','7','9','9','1','2']
# a = ['1','9','9','9','9','9']
# a = ['1','1','1','9','0','0']
a = ['1','2','3','2','1']
# a = []
# a = ['0']

first = None
for i in range(0, len(a)):
    element_current = int(a[i])
    if first is None or element_current > first:
        first = element_current

print(first)

