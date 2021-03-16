import os
import subprocess as sub

while True:

    lis = []
    f = ''
    print('началось выполнение задачи мы в ', os.getcwd())
    print('проверка в каком мы ветвлении и статуса файлов')
    os.system('git status')
    os.system('git branch')
    a = input('если вас все устраивает нажмите enter иначе введите имя ветвления в которое вы хотите попасть \n~ ')
    if not a == 'master':
        for i in sub.getoutput('git branch'):
            f += i
        if a in f:
            os.system('git checkout ' + a)
        elif a == '* ' + a:
            print('already ')
        else:
            os.system('git checkout -b ' + a)
        os.system('git checkout ' + a)

    output_branch = sub.getoutput('ls ~/PycharmProjects/mahlab/task')

    # print(output_branch)
    break
# it is test
