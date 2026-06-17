n = int(input())

for i in range(1, n + 1):
    # Convert number to string, turn digits to integers, and check if sum is 9
    if sum(int(digit) for digit in str(i)) == 9:
        print(i, end=" ")
