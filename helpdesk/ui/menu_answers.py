from models.answer import Answer, get_answers_by_ticket_id
from models.ticket import get_ticket_by_id


def menu_answers():
    while True:
        print("\n=== Ответы ===")
        print("1. Показать ответы по обращению")
        print("2. Добавить ответ")
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

        elif choice == "0":
            break

        else:
            print("Неверный ввод.")