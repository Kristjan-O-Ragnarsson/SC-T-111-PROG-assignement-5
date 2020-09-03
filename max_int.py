"""
while input not negativer
    if input > higest in 
        higest = input
"""

max_int = 0
kill = False

while not kill:
    num_int = int(input("Input a number: "))
    if num_int < 0:
        kill = True
    elif num_int > max_int:
        max_int = num_int
else:
    print("The maximum is", max_int)