
str1 = ['a', 'A', 'c', 'b', 'B', 'd', 'E', 'F']
dummy = ""
dct = {}

for j in (str1):
    if j.upper() in dct.keys() or j.lower() in dct.keys():

        if j.upper() in dct.keys():
            dct[j.upper()] += 1
        else:
            dct[j.lower()] += 1
    else:
        dct[j] = 1
print(dct)
for key, val in dct.items():
    if val <2:
        dummy=dummy+key
    else:
        continue
print(dummy)