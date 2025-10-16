s = input("Enter a string: ")

print("First character:", s[0])
print("Last character:", s[-1])

length = len(s)
if length % 2 == 0:
    mid1 = length // 2 - 1
    mid2 = length // 2
    print("Middle characters:", s[mid1], s[mid2])
else:
    mid = length // 2
    print("Middle character:", s[mid])
