import sys
numbers = []
f= open('chisla.txt', 'r')

for line in f:
    numbers.append([int(x) for x in line.split(' ')])

for nums in numbers:
        for num in range(1, nums[2]+1):
            if num % nums[0] == 0 and num % nums[1] == 0:
                print('FB', end=' ')
            elif num % nums[0] == 0:
                print('F', end=' ')
            elif num % nums[1] == 0:
                print('B', end=' ')
            else:
                print(num, end=' ')
        print()
input()