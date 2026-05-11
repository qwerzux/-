from models.ticket import Ticket, get_all_tickets, get_ticket_by_id
from models.user import get_all_users
from models.operator import get_all_operators


def menu_tickets():
    while True:
        print("\n=== Обращения ===")
        print("1. Показать все обращения")
        print("2. Создать обращение")
        print("3. Назначить оператора")
        print("4. Изменить статус")
        print("5. Удалить обращение")
        print("0. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            tickets = get_all_tickets()

            print("\nСписок обращений:")
            for ticket in tickets:
                print(
                    f"{ticket.id}. Пользователь ID: {ticket.user_id} | "
                    f"Оператор ID: {ticket.operator_id} | "
                    f"Описание: {ticket.description} | "
                    f"Статус: {ticket.status}"
                )

        elif choice == "2":
            print("\nДоступные пользователи:")
            users = get_all_users()

            for user in users:
                print(f"{user.id}. {user.full_name}")

            user_id = int(input("Введите ID пользователя: "))
            description = input("Описание проблемы: ")

            ticket = Ticket(
                user_id=user_id,
                description=description,
                status="Новое"
            )

            ticket.save()
            print("Обращение создано.")

        elif choice == "3":
            ticket_id = int(input("Введите ID обращения: "))
            ticket = get_ticket_by_id(ticket_id)

            if ticket:
                print("\nДоступные операторы:")
                operators = get_all_operators()

                for operator in operators:
                    print(f"{operator.id}. {operator.full_name}")

                operator_id = int(input("Введите ID оператора: "))
                ticket.operator_id = operator_id
                ticket.status = "Назначено"
                ticket.save()

                print("Оператор назначен.")
            else:
                print("Обращение не найдено.")

        elif choice == "4":
            ticket_id = int(input("Введите ID обращения: "))
            ticket = get_ticket_by_id(ticket_id)

            if ticket:
                print("Доступные статусы:")
                print("1. Новое")
                print("2. Назначено")
                print("3. В обработке")
                print("4. Решено")
                print("5. Закрыто")

                status_choice = input("Выберите статус: ")

                statuses = {
                    "1": "Новое",
                    "2": "Назначено",
                    "3": "В обработке",
                    "4": "Решено",
                    "5": "Закрыто"
                }

                if status_choice in statuses:
                    ticket.status = statuses[status_choice]
                    ticket.save()
                    print("Статус изменён.")
                else:
                    print("Неверный статус.")
            else:
                print("Обращение не найдено.")

        elif choice == "5":
            ticket_id = int(input("Введите ID обращения: "))
            ticket = get_ticket_by_id(ticket_id)

            if ticket:
                ticket.delete()
                print("Обращение удалено.")
            else:
                print("Обращение не найдено.")

        elif choice == "0":
            break

        else:
            print("Неверный ввод.")