lst=[10, 20, 50, 100, 200, 500, 1000]
x=int(input("Vvedite 4islo "))
limit = 10
final_banknote = False
for index, nominal in enumerate(lst):

    current_limit = limit
    test_sum =limit*nominal
    next_index = index+1
    if (next_index>= len(lst)):
        final_banknote = True
    if(test_sum<=x) and not final_banknote:
        while ((x - test_sum)%lst[next_index]):

            test_sum=test_sum-nominal
            current_limit-=1
        x-=test_sum
        print("Take", current_limit, " of", nominal)
        if x == 0:
            break
    else:
        current_limit = x//nominal
        if(not (x%nominal)):
            print("Take", current_limit, " of", nominal)
            break



