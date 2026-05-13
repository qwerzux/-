from models.user import User, get_all_users, get_user_by_id


def menu_users():
    while True:
        print("\n=== Пользователи ===")
        print("1. Показать всех пользователей")
        print("2. Добавить пользователя")
        print("3. Удалить пользователя")
        print("4. Изменить пользователя")
        print("0. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            users = get_all_users()

            print("\nСписок пользователей:")
            for user in users:
                print(f"{user.id}. {user.full_name} | Email: {user.email} | Телефон: {user.phone}")

        elif choice == "2":
            full_name = input("ФИО: ")
            email = input("Email: ")
            phone = input("Телефон: ")

            user = User(full_name=full_name, email=email, phone=phone)
            user.save()

            print("Пользователь добавлен.")

        elif choice == "3":
            user_id = int(input("Введите ID пользователя: "))
            user = get_user_by_id(user_id)

            if user:
                user.delete()
                print("Пользователь удалён.")
            else:
                print("Пользователь не найден.")

        elif choice == "4":
            user_id = int(input("Введите ID пользователя: "))
            user = get_user_by_id(user_id)

            if user:
                print("Оставьте поле пустым, если не хотите менять значение.")

                full_name = input(f"ФИО [{user.full_name}]: ")
                email = input(f"Email [{user.email}]: ")
                phone = input(f"Телефон [{user.phone}]: ")

                user.full_name = full_name if full_name else user.full_name
                user.email = email if email else user.email
                user.phone = phone if phone else user.phone

                user.save()
                print("Данные пользователя изменены.")
            else:
                print("Пользователь не найден.")

        elif choice == "0":
            break

        else:
            print("Неверный ввод.")