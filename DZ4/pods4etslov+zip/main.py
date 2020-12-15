
f= open('some.txt', 'r')

d= f.read().split()
print(dict(zip(d,list(map(lambda word: d.count(word),d)))))
f.close()

input()

