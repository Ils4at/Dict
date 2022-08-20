"""Программа кто твой папа"""

daddy = {'Sasha': 'Tomy', 'Tolya': 'Anton', 'Artem': 'Artur'}
choice = None
while choice != "0":
    print("""
    Игра кто твой папа? Выберите один из  пунктов:
    0 - Выйти;
    1 - Показать существующие связи сын-отец;
    2 - Добавить новую связь;
    3 - Изменить существующую связь;
    4 - Удалить связь.
    """)
    choice = input("Введите пункт: ")
    if choice == '0':
        print("Досвидание")
    elif choice == '1':
        names = input("Введите имя сына, у которого хотите узнать отца: ")
        if names in daddy:
            print(f"Связь {names} - {daddy[names]}")
        else:
            print("Я незнаю такого человека, вы можете его добавить через главное меню.")
    elif choice == '2':
        key = input("Для добавления новоого значения введите имя сна: ")
        if key not in daddy:
            value = input("Имя отца: ")
            daddy[key] = value
            print("Новая связь сына и отца добавлена")
        else:
            print("такой имя уже используеться")
    elif choice == '3':
        key = input("для изминеня введите: ")
        if key in daddy:
            value = input("Введите имя отца: ")
            daddy[key] = value
            print("Изминения внесены")
        else:
            print("Такого значения пока нет но вы можете его добавить!")
    elif choice == '4':
        key = input("Введите имя сына которого хотите удалить: ")
        if key in daddy:
            del daddy[key]
            print("Изминения внесены")
        else:
            print("Такого значения пока нет но вы можете его добавить!")
    else:
        print("Я не знаю такого параметра!")

input("нажмите enter чтобы закрыть.")