# slumpar fram resultat på avancerad träfftabell

from random import randint
from os.path import join


def parse_table(table):
    path = r'avancerad_trafftabell_uppdelad'
    table_file = table + '.csv'
    table_file = join(path, table_file)
    array = []
    with open(table_file, 'r', encoding='utf8') as file:
        print(file.readline())
        for line in file.readlines():
            if line[0] != r'–':
                interval = line.split(',')[0].split('–')
                interval[0] = int(interval[0])
                # för specialfall med ensam siffra
                if len(interval) == 1:
                    interval.append(interval[0])
                interval[1] = int(interval[1])
                target = line.split(',')[1]
                subtarget = line.split(',')[2]
                code = int(line.split(',')[3])
                array.append((interval, target, subtarget, code))
    return(array)


def get_table_result(table, roll):
    table = parse_table(table)
    for entry in table:
        if roll <= entry[0][1]:
            print(entry)
            return entry


def get_subtarget(table, target):
    # Fulfix för armar och ben
    if target.lower() == 'arm':
        target = 'Vänster arm'
    elif target.lower() == 'ben':
        target = 'Vänster ben'
    else:
        target = target.lower().capitalize()

    table = parse_table(table)
    for i in range(60):
        roll = randint(0, 100)
        for entry in table:
            if roll <= entry[0][1]:
                if entry[1] == target:
                    return entry[2]
                else:
                    break
    print('Fel: kunde inte slumpa delområde')



#print(get_table_result('hugg_normalt', 45))
#print(get_subtarget('hugg_normalt', 'huvud'))