import os
import subprocess as sub

while True:

    lis = []
    f = ''
    print('началось выполнение задачи мы в ', os.getcwd())
    print('проверка в каком мы ветвлении и статуса файлов')
    # os.system('git status')
    # os.system('git branch')
    # a = input('если вас все устраивает нажмите enter иначе введите имя ветвления в которое вы хотите попасть')
    for i in sub.getoutput('git branch'):
        f += i
    if '* main' in f:
        print(f)
    output_branch = sub.getoutput('ls ~/PycharmProjects/mahlab/task')

    # print(output_branch)
    break
