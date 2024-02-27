import random
import time


def pidrr(message, bot, cur, con):
    msg_txt = message.text

    cur.execute(f'''UPDATE id SET key = NULL WHERE id = {message.chat.id}''')
    con.commit()

    bot.send_message(message.chat.id, f'Проверка на сколько % [{msg_txt}](tg://user?id={message.from_user.id}) '
                                      f'пидор...',
                     disable_web_page_preview=True, parse_mode="Markdown")

    msg = bot.send_message(message.chat.id, "Загрузка.")
    for _ in range(2):
        bot.edit_message_text("Загрузка..", message.chat.id, msg.id)
        bot.edit_message_text("Загрузка...", message.chat.id, msg.id)
        bot.edit_message_text("Загрузка....", message.chat.id, msg.id)
        bot.edit_message_text("Загрузка.....", message.chat.id, msg.id)
        bot.edit_message_text("Загрузка.", message.chat.id, msg.id)
    bot.edit_message_text("Подсчет результатов...", message.chat.id, msg.id)
    time.sleep(4)
    bot.edit_message_text("Соединение с сервером...", message.chat.id, msg.id)
    time.sleep(4)
    bot.edit_message_text("Выявление окончательного ответа...", message.chat.id, msg.id)
    time.sleep(4)
    bot.edit_message_text("Поздравляем!", message.chat.id, msg.id)

    bot.send_message(message.chat.id, f'[{msg_txt}](tg://user?id={message.from_user.id}) пиздец пидорас на все '
                                      f'{random.randrange(0, 100, 5)}%',
                     disable_web_page_preview=True, parse_mode="Markdown")

    cur.execute(f'''UPDATE id SET kluch = 1111 WHERE id = {message.chat.id} ''')
    con.commit()
