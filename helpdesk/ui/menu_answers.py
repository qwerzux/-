from models.answer import Answer, get_answers_by_ticket_id, get_answer_by_id
from models.ticket import get_ticket_by_id


def menu_answers():
    while True:
        print("\n=== Ответы ===")
        print("1. Показать ответы по обращению")
        print("2. Добавить ответ")
        print("3. Изменить ответ")
        print("4. Удалить ответ")
        print("0. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            ticket_id = int(input("Введите ID обращения: "))
            answers = get_answers_by_ticket_id(ticket_id)

            if not answers:
                print("Ответов по этому обращению нет.")
            else:
                print("\nОтветы:")
                for answer in answers:
                    print(f"{answer.id}. {answer.answer_text}")

        elif choice == "2":
            ticket_id = int(input("Введите ID обращения: "))
            ticket = get_ticket_by_id(ticket_id)

            if ticket:
                answer_text = input("Введите текст ответа: ")

                answer = Answer(
                    ticket_id=ticket_id,
                    answer_text=answer_text
                )
                answer.save()

                ticket.status = "Решено"
                ticket.save()

                print("Ответ добавлен. Статус обращения изменён на 'Решено'.")
            else:
                print("Обращение не найдено.")

        elif choice == "3":
            answer_id = int(input("Введите ID ответа: "))
            answer = get_answer_by_id(answer_id)

            if answer:
                print(f"Текущий ответ: {answer.answer_text}")
                new_text = input("Новый текст ответа: ")

                if new_text:
                    answer.answer_text = new_text
                    answer.save()
                    print("Ответ изменён.")
                else:
                    print("Текст не изменён.")
            else:
                print("Ответ не найден.")

        elif choice == "4":
            answer_id = int(input("Введите ID ответа для удаления: "))
            answer = get_answer_by_id(answer_id)

            if answer:
                answer.delete()
                print("Ответ удалён.")
            else:
                print("Ответ не найден.")

        elif choice == "0":
            break

        else:
            print("Неверный ввод.")