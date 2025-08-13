names=["Alice", "Bob", "Charlie", "David", "Eve","John", "Jane", "Jack", "Jill", "Joe"]

print(names[0])
print(names[-1])

print(names[2:6])

for i in range(1,len(names)+1):
    print(names[-i])

print(names[7:1:-1])