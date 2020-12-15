students = {"Karenov_S":[80,70,75, 60, 75],
            "Kalaychev_G":[80, 90, 80, 75, 85],
            "Drulev_D":[60, 50, 45, 70, 65],
            "Khamza_I":[75, 90, 75, 70, 85],
            "Gerasimenko_M":[70, 65, 80, 75, 60]}
avg =[]
for name, marks in students.items():
    avg.append(sum(marks)/len(marks))
    s =(sum(marks)/len(marks))


    print(name,', ' "Average mark =", s)

print()




if len(avg)==5:
    print("Max average =", max(avg))
if len(avg)==5:
    print("Min average =", min(avg))

input()