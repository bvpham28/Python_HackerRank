n1, s1 = int(input()), set(list(map(int, input().strip().split())))
n2, s2 = int(input()), set(list(map(int, input().strip().split())))

print(len(s1 - s2))