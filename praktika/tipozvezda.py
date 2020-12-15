num = int(input("Enter your number: "))
while not (num % 2 and num > 0):
    print("Try again ")
    num = int(input("Enter your number: "))
if num % 2 and num > 0:
    for i in range(1, num + 1, 2):
        print(i * "*")
    for i in range(num - 2, 0, -2):
        print(i * "*")