#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil
def create_folder():
    global path
    path_cr = path + "\\" + input("Введите название папки: ")
    try:
        os.mkdir(path_cr)
    except OSError:
        print ("Создать директорию %s не удалось" % path_cr)
    #else:
        #print ("Успешно создана директория %s " % path_cr)
def delete_folder():
    global path
    path_dl = path + "\\" + input("Введите название папки: ")
    try:
        shutil.rmtree(path_dl)
    except OSError:
        print ("Удалить директорию %s не удалось" % path_dl)
    #else:
        #print ("Успешно удалена директория %s " % path_dl)
def move():
    global path
    try:
        path += "\\" + input("Введите название папки: ")
        os.chdir(path)
    except OSError:
        print ("Переместиться в данную директорию не удалось. Текущая директория %s" % os.getcwd())
    #else:
        #print ("Перемещение выполнено успешно. Текущая директория %s" % os.getcwd())
def move_up():
    global path
    try:
        path = path[:path.rfind("\\")]
        os.chdir(path)
    except OSError:
        print ("Переместиться в данную директорию не удалось. Текущая директория %s" % os.getcwd())
    #else:
        #print ("Перемещение выполнено успешно. Текущая директория %s" % os.getcwd())
def create_file():
    global path
    path_fl = path + "\\" + input("Введите название файла: ")
    try:
        file = open(path_fl, 'w')
    except IOError:
        print ("Создать файл %s не удалось" % path_fl)
    else:
        #print ("Успешно создан файл %s " % path_fl)
        file.close()
def write_file():
    global path
    path_fl = path + "\\" + input("Введите название файла: ")
    try:
        file = open(path_fl, 'w')
        msg = input('Введите текст: ')
        file.write(msg)
    except IOError:
        print ("Перезаписать файл %s не удалось" % path_fl)
    else:
        #print ("Успешно перезаписан файл %s " % path_fl)
        file.close()
def read_file():
    global path
    path_fl = path + "\\" + input("Введите название файла: ")
    try:
        file = open(path_fl, 'r')
        text = file.read()
        print(text)
    except IOError:
        print ("Прочитать файл %s не удалось" % path_fl)
    else:
        #print ("Успешно прочитан файл %s " % path_fl)
        file.close()
def delete_file():
    global path
    path_fl = path + "\\" + input("Введите название файла: ")
    try:
        os.remove(path_fl)
    except OSError:
        print ("Удалить файл %s не удалось" % path_fl)
    #else:
        #print ("Успешно удалён файл %s " % path_fl)
def rplc_file():
    global path
    file = input("Введите путь к файлу: ")
    path_fl = path + file
    folder = input("Введите путь к папке: ")
    if folder == '\\':
        path_fl_new = path + folder + file[file.rfind('\\')+1:]
    else:
        path_fl_new = path + folder + '\\' + file[file.rfind('\\')+1:]
    try:
        os.replace(path_fl, path_fl_new)
    except OSError:
        print ("Переместить файл %s не удалось" % path_fl)
    #else:
        #print ("Успешно перемещён файл %s " % path_fl)
def rnm_file():
    global path
    file = path + "\\" + input("Введите название файла: ")
    file_new = path + "\\" + input("Введите новое название файла: ")
    try:
        os.rename(file, file_new)
    except OSError:
        print ("Переименовать файл %s не удалось" % file)
    #else:
        #print ("Успешно переименован файл %s " % file)
def cp_file():
    global path
    file = path + input("Введите путь к файлу: ")
    file_new = path + input("Введите новый путь к файлу: ")
    try:
        shutil.copy2(file, file_new)
    except OSError:
        print ("Скопировать файл %s не удалось" % file)
    #else:
        #print ("Успешно скопирован файл %s " % file)
        
try:
    settings = open('settings.txt', 'r', encoding='utf-8')
    root = settings.read()
except IOError:
    print ("ERROR")
except OSError:
    print ("ERROR")
else:
    settings.close()
    os.chdir(root)
    path = os.getcwd() 
    #print ("Текущая рабочая директория %s" % path)
    print("cfd - создать папку\ndfd - удалить папку\nmove - переместиться в другую папку\nmoveup - перейти на уровень вверх\ncfl - создать файл\nwfl - перезаписать файл\nrfl - прочитать файл\ndfl - удалить файл\nrnm - переименовать файл\nrplc - переместить файл\ncpfl - копировать файл")
    while True:
        inp = input('Введите команду: ')
        if inp == 'cfd':
            create_folder()
        elif inp == 'dfd':
            delete_folder()
        elif inp == 'move':
            move()
        elif inp == 'moveup':
            move_up()
        elif inp == 'cfl':
            create_file()
        elif inp == 'wfl':
            write_file()
        elif inp == 'rfl':
            read_file()
        elif inp == 'dfl':
            delete_file()
        elif inp == 'rnm':
            rnm_file()
        elif inp == 'rplc':
            rplc_file()
        elif inp == 'cpfl':
            cp_file()
        elif inp == 'br':
            break
        else:
            print('Неизвестная команда')

