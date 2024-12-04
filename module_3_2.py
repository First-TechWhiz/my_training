def send_email(message, recipiend, sender = "university.help@gmail.com"):
    if "@" not in recipiend or "@" not in sender\
            or not recipiend.endswith((".com", ".net", ".ru")) or not sender.endswith((".com", ".net", ".ru")):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipiend}')
    elif recipiend == sender:
        print('Нельзя отправить письмо самому себе')
    elif sender != "university.help@gmail.com":
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipiend}')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipiend}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')