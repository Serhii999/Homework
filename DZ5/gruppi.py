students = {
    'Kalaychev_G' : {'FrontEnd', 'Python', 'Fullstack'},
    'Karenov_S' : {'FrontEnd', 'Java'},
    'Drulev_D' : {'Python', 'Fullstack'},
    'Khamza_I' : {'Java'},
    'Gerasimenko_M' : {'FrontEnd', 'Python'},
    'Pedan_R' : {'Python', 'FullStack'}
}
def bolshe_dvuh (dict):
    bd = []
    for name, group in dict.items():
        if len(group) > 1:
            bd.append(name)
    return bd

def Ne_front(dict):
    notf = []
    for name, group in dict.items():
        if 'FrontEnd' not in group:
           notf.append(name)
    return notf

def P_or_J (dict):
    pj = []
    for name, group in dict.items():
        if 'Python' or 'Java' in group:
            pj.append(name)
    return pj

print('Rabotyagi - ', bolshe_dvuh(students))
print('Ih net na Frontned - ', Ne_front(students))
print('Na pythone ili jave - ', P_or_J(students))

input()
