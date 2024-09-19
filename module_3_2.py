def chek_email(mail):
    lenth=len(mail)
    flag=True
    flag_1 = mail.find('@')
    flag_2 = mail.find('.com')
    flag_3 = mail.find('.ru')
    flag_4 = mail.find('.net')
    if flag_1 >= 1 and (lenth - flag_2 == 4 or lenth - flag_3 == 3 or lenth - flag_4 == 4):
        flag=True
    else:
        flag=False
    return flag


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    else:
        if chek_email(recipient) and chek_email(sender):
            if sender == "university.help@gmail.com":
                print("Письмо успешно отправлено с адреса: ", sender, " на адрес: ", recipient)
            else:
                print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, " на адрес: ", recipient)
        else:
            print("Невозможно отправить письмо с адреса: ", sender, " на адрес: ", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
