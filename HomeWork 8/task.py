# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
#     Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода. 
#     Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
#     Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
#     Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
#     Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
#     Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv


# Используйте функции для реализации значимых действий в программе

# Усложнение.

# - Сделать тесты для функций
# - Разделить на model-view-controller

import os.path as path1


def get_user() -> list:
    user =[]
    user.append(input("Введите фамилию: "))
    user.append(input("Введите имя: "))
    user.append(input("Введите номер телефона: "))
    user.append(input("Введите комментарий: "))
    return user

def create(phone_book_local: dict,user:list) -> dict:
    if len(phone_book_local) == 0:              
        idc =  1
    else:
        idc = max(phone_book_local.keys())+1
    phone_book_local[idc] = user
    return phone_book_local
    
def search_user(phone_book_local: dict):
    surname = input("Введите начальные буквы фамилии: ")
    for idc, user in phone_book_local.items():
        if ((user[0]).lower()).startswith(surname.lower()) == True:
            print(*phone_book_local[idc])
            return idc

def change_user(phone_book_local, idc)-> dict:
    while True:
        print("Введите 1, если хотите изменить фамилию.")
        print("Введите 2, если хотите изменить имя.")
        print("Введите 3, если хотите изменить телефон.")
        print("Введите 4, если хотите изменить комментарий.")
        print("Введите 0, если хотите выйти.")
        submenu_item = int(input("Введите ваш выбор: "))
        if submenu_item == 0:
            break
        else: 
            new_value = input("Введите новое значение: ")
            phone_book_local[idc][submenu_item-1] = new_value
            print(f"Новая запись: {phone_book_local[idc]}")
    return phone_book_local        

def delete_user(phone_book_local, idc)-> dict:
    del phone_book_local[idc]
    return phone_book_local

def export_in_file(phone_book_local: dict):
    file_name = input("Введите имя файла для экспорта: ") + '.csv'
    MAIN_DIR = path1.abspath(path1.dirname(__file__))
    file_path = path1.join(MAIN_DIR, file_name)
    with open(file_path, mode="w", encoding="utf-8") as file:
        for idc, user in phone_book_local.items():
            file.write(f"{user[0]},{user[1]},{user[2]}, {user[3]}\n")

def import_from_file() -> dict:
    file_name = input("Введите имя файла для импорта: ") + '.csv'
    MAIN_DIR = path1.abspath(path1.dirname(__file__))
    file_path = path1.join(MAIN_DIR, file_name)
    phone_book_local = dict()
    with open(file_path, mode="r", encoding="utf-8") as file:
        key_count = 1
        for line in file:
            phone_book_local[key_count] = line.strip().split(',')
            key_count+=1
    print(phone_book_local)
    return phone_book_local
                                           
def menu():
    phone_book= dict()
    
    while True:
        print("Введите 1, если хотите добавить нового пользователя.")
        print("Введите 2, если хотите отобразить весь телефонный справочник.")
        print("Введите 3, если хотите найти пользователя.")
        print("Введите 4, если хотите отредактировать пользователя.")
        print("Введите 5, если хотите удалить пользователя.")
        print("Введите 6, если хотите экспортировать справочник в файл.")
        print("Введите 7, если хотите импортировать справочник из файла.")
        print("Введите 0, если хотите выйти.")
        menu_item = int(input("Ваш выбор: "))
        if menu_item == 0:
            break
        if menu_item == 1:
            user = get_user()
            phone_book = create(phone_book,user)
        if menu_item == 2:
            print(phone_book)
        if menu_item == 3:
            search_user(phone_book)
        if menu_item == 4:
            inx = search_user(phone_book)
            phone_book = change_user(phone_book, inx)
        if menu_item == 5:
            inx = search_user(phone_book)
            phone_book = delete_user(phone_book, inx)
        if menu_item == 6:
            export_in_file(phone_book)    
        if menu_item == 7:
            phone_book = import_from_file()
                
menu()