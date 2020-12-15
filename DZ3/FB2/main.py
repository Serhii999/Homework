import sys
numbers = []
f= open('chisla.txt', 'r')
k= open ('vivod.txt', 'w')
for line in f:
    numbers.append([int(x) for x in line.split(' ')])

for nums in numbers:
        for num in range(1, nums[2]+1):
            if num % nums[0] == 0 and num % nums[1] == 0:
                k.write('FB')
            elif num % nums[0] == 0:
                k.write('F')
            elif num % nums[1] == 0:
                k.write('B')
            else:
                k.write(str(num))
        k.write('\n')
k.close()
input()