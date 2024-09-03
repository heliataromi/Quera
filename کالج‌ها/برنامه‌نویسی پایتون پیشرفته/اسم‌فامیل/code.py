import csv


data = {}
people = []
esms = []
famils = []
keshvars = []
rangs = []
ashias = []
ghazas = []


def ready_up():
    file = csv.DictReader(open('esm_famil_data.csv', 'r', encoding="utf8"))
    global data
    data = {'esm': [],
            'famil': [],
            'keshvar': [],
            'rang': [],
            'ashia': [],
            'ghaza': []}
    for col in file:
        data['esm'].append(col['esm'].replace(' ', ''))
        data['famil'].append(col['famil'].replace(' ', ''))
        data['keshvar'].append(col['keshvar'].replace(' ', ''))
        data['rang'].append(col['rang'].replace(' ', ''))
        data['ashia'].append(col['ashia'].replace(' ', ''))
        data['ghaza'].append(col['ghaza'].replace(' ', ''))

    data['esm'] = [x for x in data['esm'] if x != '']
    data['famil'] = [x for x in data['famil'] if x != '']
    data['keshvar'] = [x for x in data['keshvar'] if x != '']
    data['rang'] = [x for x in data['rang'] if x != '']
    data['ashia'] = [x for x in data['ashia'] if x != '']
    data['ghaza'] = [x for x in data['ghaza'] if x != '']


def add_participant(participant, answers):
    people.append(participant)
    esms.append(answers['esm'].replace(' ', ''))
    famils.append(answers['famil'].replace(' ', ''))
    keshvars.append(answers['keshvar'].replace(' ', ''))
    rangs.append(answers['rang'].replace(' ', ''))
    ashias.append(answers['ashia'].replace(' ', ''))
    ghazas.append(answers['ghaza'].replace(' ', ''))


def calculate_one(ls, name):
    points = []
    for i in range(len(ls)):
        if '' in ls:
            if ls[i] == '':
                points.append(0)
            elif ls[i] not in data[name]:
                points.append(0)
            elif ls.count(ls[i]) > 1:
                points.append(10)
            else:
                points.append(15)
        else:
            if ls[i] not in data[name]:
                points.append(0)
            elif ls.count(ls[i]) > 1:
                points.append(5)
            else:
                points.append(10)
    return points


def calculate_all():
    total_points = []
    esm_points = calculate_one(esms, 'esm')
    print('esm', esm_points)
    for point in esm_points:
        total_points.append(point)

    famil_points = calculate_one(famils, 'famil')
    print('famil', famil_points)
    for i in range(len(famil_points)):
        total_points[i] += famil_points[i]

    keshvar_points = calculate_one(keshvars, 'keshvar')
    print('keshvar', keshvar_points)
    for i in range(len(keshvar_points)):
        total_points[i] += keshvar_points[i]

    rang_points = calculate_one(rangs, 'rang')
    print('rang', rang_points)
    for i in range(len(rang_points)):
        total_points[i] += rang_points[i]

    ashia_points = calculate_one(ashias, 'ashia')
    print('ashia', ashia_points)
    for i in range(len(ashia_points)):
        total_points[i] += ashia_points[i]

    ghaza_points = calculate_one(ghazas, 'ghaza')
    print('ghaza', ghaza_points)
    for i in range(len(ghaza_points)):
        total_points[i] += ghaza_points[i]

    ans = {}
    for i in range(len(people)):
        ans[people[i]] = total_points[i]

    return ans
