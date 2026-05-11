from models.operator import Operator, get_all_operators, get_operator_by_id


def menu_operators():
    while True:
        print("\n=== Операторы ===")
        print("1. Показать всех операторов")
        print("2. Добавить оператора")
        print("3. Удалить оператора")
        print("0. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            operators = get_all_operators()

            print("\nСписок операторов:")
            for operator in operators:
                print(f"{operator.id}. {operator.full_name} | Должность: {operator.position} | Телефон: {operator.phone}")

        elif choice == "2":
            full_name = input("ФИО: ")
            position = input("Должность: ")
            phone = input("Телефон: ")

            operator = Operator(
                full_name=full_name,
                position=position,
                phone=phone
            )
            operator.save()

            print("Оператор добавлен.")

        elif choice == "3":
            operator_id = int(input("Введите ID оператора: "))
            operator = get_operator_by_id(operator_id)

            if operator:
                operator.delete()
                print("Оператор удалён.")
            else:
                print("Оператор не найден.")

        elif choice == "0":
            break

        else:
            print("Неверный ввод.")