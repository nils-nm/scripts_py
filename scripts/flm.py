#!/usr/bin/env python3
"""
allow touch or rm file in current dir 
"""

import os

print('rm - удалить один файл',
      '\ntouch - создать один файл',
      '\nenter - пропустить или фыход')

lwname = []

while True:
    action = input("Выберите действие --> ")
    if action == "touch":
        while True:
            print("*создание одного файла* После ввода имени файла будет приписано --> .py")
            name = input("Введите имя файда --> ")
            if len(name) > 0:
                os.system("touch " + name + ".py")
                continue
            else:
                break
    elif action == "rm":
        while True:
            print("*удаление одного файла* После ввода имени файла будет приписано --> .py")
            name = input("Введите имя файла --> ")
            if len(name) > 0:
                os.system("rm " + name + ".py")
                continue
            else:
                break
    elif len(action) == 0:
        break
    else:
        print("Неправельный ввод!!!")
