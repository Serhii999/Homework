x = int(input('Ввведите первое число '))
y = int(input('Введите второе число '))
z = int(input('Введите третье число '))

for i in range(1, z+1):
    if i % x == 0 and i % y == 0:
        print("FB", end=' ')
    elif i % x == 0:
        print("F", end=' ')
    elif i % y == 0:
        print("B", end=' ')
    else:
        print(i, end=' ')

input()
