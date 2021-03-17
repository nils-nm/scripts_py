import os
import subprocess as sub


branch = ''
f = ''
t = ''


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
        f += i
    f = f.split()
    for j in range(len(f)):
        if f[j] == '*':
            branch = f[j + 1]
    a = input('если вас все устраивает нажмите enter или введите exit для выхода '
              'иначе введите имя ветвления в которое вы хотите попасть \n--> ')

    if a != 'main' and a != '':
        print(f, branch)

        if 'main' == branch:
            print('мы щас в main перехожу в ' + a)
            os.system('git checkout ' + a)
        elif a == branch:
            print('мы щас в ' + a + ' остаюсь в ' + a)
        elif a in f:
            print('мы щас в ' + branch + ' перехожу в ' + a)
            os.system('git checkout ' + a)
        else:
            print('ветвления ' + a + ' нет, создаю ' + a + ' и перехожу в него')
            os.system('git checkout -b ' + a)
    elif a == 'main':

        if a == branch:
            print('мы щас в ' + a + ' остаюсь в ' + a)

        elif a != branch:
            print('мы щас в ' + branch + ' перехожу в ' + a)
            os.system('git checkout ' + a)
    elif a == 'exit':
        break
    status()
    print('одобряю все для коммита')
    os.system('git add -A')
    print('делаю коммит')
    os.system('git commit -m' + input('оставьте коментарий --> '))
    status()
    for i in sub.getoutput('git branch'):
        t += i
    f = t.split()
    for j in range(len(f)):
        if f[j] == '*':
            print(f)
            print(f[j])
            branch = f[j + 1]
    if branch == 'main':
        print('вношу изменения в интернет')
        os.system('git push origin')
    else:
        print('ассоциирую ветку ' + branch + ' с веткой main')
        os.system('git push -u origin ' + branch)
        print('перехожу на main')
        os.system('git checkout main')
        print('закачиваю последниии изменения из main')
        os.system('git pull origin main')
        print('сливаюсь локально')
        os.system('git merge ' + branch)
        print('сливаюсь удаленно')
        os.system('git push origin main')
    if input('удалить ветвление? (y/n)\n--> ') == 'y':
        print('удаляю ' + branch)
        os.system('git branch -D ' + branch)
        print('работа завершена отключаюсь')
    else:
        print('работа завершена отключаюсь')

    break
