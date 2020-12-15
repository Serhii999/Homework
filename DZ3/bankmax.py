lst=[1000, 500, 200, 100, 50, 20, 10]
x=int(input("Vvedite 4islo "))

for i in lst:
  if x>= i:
      count= int(x/i)
      x=x-(count*i)
      print(count, "*", i, end='  ')

input()