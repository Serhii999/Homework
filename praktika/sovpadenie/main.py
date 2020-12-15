f = open("4isla.txt")
for l in f.readlines():
    before = [int(i) for i in l.split(';')[0] if i.isdigit()]
    after = [int(i) for i in l.split(';')[1] if i.isdigit()]
    whole = sum(before) // len(before)
    percent = sum(before) % len(before)
    if whole == after[0] and percent == after[1]:
        print(l.strip(), True, sep=' ---> ')
    else:
        print(l.strip(), False, sep=' ---> ')
