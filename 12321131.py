a = ""
for i in range(int(input()), int(input()) + 1):
    if i % 2 == 0:
        a += " " + str(i)
print(a[1:])