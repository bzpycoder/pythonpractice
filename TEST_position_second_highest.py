# PROBLEM: Find the second highest element in given list

# a = input().split()
# a = ['6','7','9','9','1','2']
# a = ['9','9','9','9','9','9']
# a = ['6','7','9','9','1','2']
a = ['1','9','9','9','9','9']
# a = ['1','1','1','9','0','0']
# a = ['1','2','3','2','1']
# a = []
# a = ['0']

first = None
second = None
for i in range(0, len(a)):
    element_current = int(a[i])
    if first is None or element_current > first:                            # (first, second) < element    *Change first
        second = first
        first = element_current
    elif second is None and element_current == first:                       # second < first == element    *Do Nothing
        second = None
    elif element_current <= second and element_current != first:            # element < second < first    *Change
        second = element_current
    #else                                                                   # second < element < first    *Do nothing

print(first, second)

