"""
n = n + n1 + n2
n1 = old n 
n2 = old n1

2 1 0
3 2 1
6 3 2
11 
"""

n1 = 2
n2 = 1
n3 = 0

counter = 2

n = int(input("Enter the length of the sequence: "))

print(n2)
print(n1)

while counter < n:
    tmp = n1
    n1 = n1 + n2 + n3
    n3 = n2
    n2 = tmp
    print(n1)
    counter += 1

