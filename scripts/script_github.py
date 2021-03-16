import os
import subprocess as sub

branch = ''
def status():
    print('--------------------------------------')
    os.system('git status')
    print('--------------------------------------')
    os.system('git branch')
    print('--------------------------------------')


while True:

    print('началось выполнение задачи мы в ', os.getcwd())
    print('проверка в каком мы ветвлении и статуса файлов')
    status()
    for i in sub.getoutput('git branch'):
        if '*' in i:
            branch = i
    a = input('если вас все устраивает нажмите enter или введите exit для выхода '
              'иначе введите имя ветвления в которое вы хотите попасть \n--> ')

    if a != 'main' and a != '':

        for i in sub.getoutput('git branch'):
            if '*' in i:
                if 'main' in i:
                    print('мы щас в main перехожу в ' + a)
                    os.system('git checkout ' + a)
                elif a in i:
                    print('мы щас в ' + a + ' остаюсь в ' + a)
                else:
                    print('ветвления ' + a + ' нет, создаю ' + a + ' и перехожу в него')
                    os.system('git checkout -b ' + a)
    elif a == 'main':
        for i in sub.getoutput('git branch'):
            if '*' in i:
                if a in i:
                    print('мы щас в ' + a + ' остаюсь в ' + a)

                elif a not in i:
                    print('мы щас в ' + i + ' перехожу в ' + a)
                    os.system('git checkout ' + a)
    elif a == 'exit':
        break
    status()
    print('одобряю все для коммита')
    os.system('git add -A')
    print('делаю коммит')
    os.system('git commit')
    if branch == 'main':
        pass
    else:
        print('ассоциируем ветку ' + branch + ' с веткой main')




    break
    # print(output_branch)
    # output_branch = sub.getoutput('ls ~/PycharmProjects/mahlab/task')