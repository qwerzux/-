from database.db_manager import initialize_db
from ui.menu import show_main_menu
from ui.menu_users import menu_users
from ui.menu_operators import menu_operators
from ui.menu_tickets import menu_tickets
from ui.menu_answers import menu_answers


def main():
    initialize_db()

    while True:
        choice = show_main_menu()

        if choice == "1":
            menu_users()

        elif choice == "2":
            menu_operators()

        elif choice == "3":
            menu_tickets()

        elif choice == "4":
            menu_answers()

        elif choice == "0":
            print("Программа завершена.")
            exit()

        else:
            print("Неверный ввод.")


if __name__ == "__main__":
    main()
    