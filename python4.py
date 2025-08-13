list=[1,5,7,8,1,9,1]

duplicates=[]
for i in list:
    if list.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print("Duplicate elements:", duplicates)

