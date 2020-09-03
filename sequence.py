"""
n = n + n1 + n2
n1 = old n 

2 1 0
3 2 1
6 3 2
11 
"""

n = 2
n1 = 1
n2 = 0

counter = 2

limit = int(input())

print(n1)
print(n)

while counter < limit:
    tmp = n
    n = n + n1 + n2
    n2 = n1
    n1 = tmp
    print(n)
    counter += 1

