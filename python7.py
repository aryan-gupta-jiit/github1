first=1
second=1
third=2

print(first)
print(second)

for i in range(3):
    fib_num=first+second
    print(fib_num)
    first=second
    second=fib_num
