import view.menu as m

def menu_console():
    m.printMenuTitle("Главное меню\n            ЖУРНАЛ ЗАМЕТОК")
    print("1 - вывод журнала\n2 - вывод заметки по id\n3 - выбор заметки по дате\n4 - редактировать заметку"
          "\n5 - добавление заметки\n6 - удалить заметку\n7 - выход ")
    m.printMenuLine()
    print("\n введите пункт меню")