def send_mail(message, recipient, *, sender='university.help@gmail.com'):
    if not all(['@' in recipient,
                '@' in sender,
                recipient.endswith('.ru') or
                recipient.endswith('.com') or
                recipient.endswith('.net'),
                sender.endswith('.ru') or
                sender.endswith('.com') or
                sender.endswith('.net')]):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender != 'university.help@gmail.com':
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")


send_mail('Это сообщение для проверки связи', 'emilo@gmail.com')
send_mail('Вы видите это сообщение как лучший студент курса!',
          "university.help@gmail.com", sender='urban.info@gmail.com')
send_mail('Пожалуйста, исправьте задание', 'YamilononeYandex@mail.kz')
send_mail('Напоминаю самому себе о вебинаре', 'university.help@gmail.com')
