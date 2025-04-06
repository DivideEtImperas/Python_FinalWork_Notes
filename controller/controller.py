import view.userMenu as ui
import controller.commands as comm


def start():
    while True:
        ui.menu_console()
        user_input = input()
        if user_input == '1':
            comm.show("all")
        elif user_input == '2':
            comm.show("ID")
        elif user_input == '3':
            comm.show("date")
        elif user_input == '4':
            comm.show("all")
            comm.change_note()
        elif user_input == '5':
            comm.add_note()
        elif user_input == '6':
            comm.show("all")
            comm.del_note()
        else:
            print("Программа Журнал заметок завершена")
            break