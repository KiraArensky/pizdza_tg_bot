from os import system
import time
import os
import random

try:
    import shelve
except:
    system("pip install shelve")
    import shelve

try:
    import telebot
except:
    system("pip install pyTelegramBotAPI")
    import telebot

d = shelve.open('id.txt')

lohhh = {}
kluch = 123
assss = ["Лох", "Еблан", "Пидор", "Чмо", "Долбоеб", "Попуск", "Ботик", "Абортыш", "Никто", "Уебан", "Хуйло",
         "Ничтожество", "Дурак", "Мразь"]


def slovs(s, message, bot, cur, con):
    global lohhh, kluch, assss
    if "/lohh" in message.text or "/lohh@pizdza_bot" in message.text:
        kluch = 321
        try:
            if message.from_user.id not in lohhh.keys():
                if message.reply_to_message.from_user.id == 466348470:
                    lohhh[message.from_user.id] = message.reply_to_message.from_user.id
                    bot.send_message(message.chat.id,
                                     f'[Котик](tg://user?id={message.from_user.id}) теперь лох',
                                     disable_web_page_preview=True,
                                     parse_mode="Markdown")
                else:
                    lohhh[message.reply_to_message.from_user.id] = message.from_user.id
                    bot.send_message(message.chat.id,
                                     f'[Котик](tg://user?id={message.reply_to_message.from_user.id}) теперь лох',
                                     disable_web_page_preview=True,
                                     parse_mode="Markdown")
            else:
                bot.send_message(message.chat.id,
                                 f'[Котик](tg://user?id={message.from_user.id}) не может обзываться, он только мяукает',
                                 disable_web_page_preview=True,
                                 parse_mode="Markdown")
        except:
            bot.send_message(message.chat.id, "Для начала ответь на сообщение лоха, кочелыга")
    elif (
            "/nelohh" == message.text or "/nelohh@pizdza_bot" == message.text) and kluch == 321 and message.from_user.id in lohhh.values():
        try:
            del lohhh[message.reply_to_message.from_user.id]
            bot.send_message(message.chat.id,
                             f'Окей, [ты](tg://user?id={message.reply_to_message.from_user.id}) больше не лох',
                             disable_web_page_preview=True,
                             parse_mode="Markdown")
            kluch = 123
        except:
            bot.send_message(message.chat.id, "Для начала ответь на сообщение провинившегося, зайчик")
    elif (
            "/nelohh" == message.text or "/nelohh@pizdza_bot" == message.text) and kluch == 321 and message.from_user.id in lohhh.keys():
        bot.send_message(message.chat.id, f'Хаха, пошел нахуй {random.choice(assss).lower()}')
    elif "похуй" in s:
        bot.send_message(message.chat.id, "нет")
        bot.send_message(message.chat.id, "это мне похуй")
        img = open('gbwwf.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif "👍" in message.text:
        img = open('partiya.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif "👎" in message.text:
        img = open('nepartiya.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif "/Asd1236987" == message.text and message.chat.id == 466348470:
        bot.send_message(message.chat.id, "админка")
        cur.execute(f'''UPDATE id SET kluch = 123 WHERE id = {message.chat.id} ''')
        con.commit()
    elif "/cum" == message.text or "/cum@pizdza_bot" == message.text:
        bot.send_message(message.chat.id, 'Добрый день, это чат-бот Пицц(зд)а!\n\
    \n\
    Он создан ради вашего удовольствия, ну и обосрать вас, как в чате, так и раз на раз\n\
    \n\
    Основной его функционал: хамить вам и раздражать вас и ваших друзей\n\
    \n\
    Но помимо этого, у него есть команды:\n\
    /cum - инфа о боте\n\
    /poh0 - специальный режим похуй\n\
    /poh1 - отключение режима похуй\n\
    /pic - рандомная пикча\n\
    /pic_add - предложить пикчу в добавление рандомной пикчи\n\
    /test - тест на пидора\n\
    /jops - спам взлом жопы\n\
    /lohh - обижает обидчика после каждого сообщения (ВАЖНО! команду нужно использовать ответив на сообщение обидчика)\n\
    /nelohh - прекратить обижать (отмена /lohh)\n\
                         \n\
    #Функционал_будет_пополнятся\n\
    \n\
        \n\
    Приятное дополнение: бот может мутить участников беседы (но не админов)!\n\
        \n\
    Для этого ответьте на сообщение обидчика так: "тише! {срок в минутах}"\n\
        \n\
    \n\
    Все ваши предложения можете писать мне: @kshi_rar\n\
    \n\
    Также у меня есть канал: https://t.me/tultayeji\n\
    \n\
    Маме привет!')
    elif "да" in s or "д" in s:
        bot.send_message(message.chat.id, "Пизда")
    elif message.text == '/poh0' or "/poh0@pizdza_bot" == message.text:
        bot.send_message(message.chat.id, "poh_on")
        cur.execute(f'''UPDATE id SET kluch = 2222 WHERE id = {message.chat.id} ''')
        con.commit()
    elif "андрей" in s:
        bot.send_message(message.chat.id, "Уебан")
    elif "нет" in s:
        bot.send_message(message.chat.id, "Пидора ответ")
    elif "Шлюхи аргумент" == message.text or "шлюхи аргумент" == message.text or "аргумент" in s:
        bot.send_message(message.chat.id, "От шлюхи слышу")
    elif "нахуй" in s:
        bot.send_message(message.chat.id, f'Только {int(time.strftime("%H")) + 5}:{time.strftime("%M")}, \
 а [ты](tg://user?id={message.from_user.id}) уже идешь нахуй', disable_web_page_preview=True,
                         parse_mode="Markdown")
    elif "/jops" == message.text or "/jops@pizdza_bot" == message.text:
        cur.execute(f'''UPDATE id SET kluch = 4444 WHERE id = {message.chat.id} ''')
        con.commit()
        bot.send_message(message.chat.id, text="Вы уверены?")
    elif "/pic" == message.text or "/pic@pizdza_bot" == message.text:
        DIR = 'pic/photos'
        img = open(os.path.join(DIR, random.choice(os.listdir(DIR))), "rb")
        bot.send_photo(message.chat.id, img)
    elif "/pic_add" == message.text or "/pic_add@pizdza_bot" == message.text:
        cur.execute(f'''UPDATE id SET kluch = 5555 WHERE id = {message.chat.id} ''')
        con.commit()
        bot.send_message(message.chat.id, "Ну давай, отправь пикчу на рассмотрение")
    elif "Тест на пидора" == message.text or "/test" == message.text or "/test@pizdza_bot" == message.text:
        cur.execute(f'''UPDATE id SET kluch = 3333 WHERE id = {message.chat.id} ''')
        con.commit()
        bot.send_message(message.chat.id, "Тест на пидора")
        bot.send_message(message.chat.id, "Как вас зовут?")
    if kluch == 321 and message.from_user.id in lohhh:
        bot.reply_to(message, f'{random.choice(assss)}')


def poh(message, bot, cur, con):
    if message.text == '/poh1' or "/poh1@pizdza_bot" == message.text:
        bot.send_message(message.chat.id, "poh_off")
        cur.execute(f'''UPDATE id SET kluch = 1111 WHERE id = {message.chat.id} ''')
        con.commit()
    else:
        bot.send_message(message.chat.id, "Да мне похуй.")


def pidrr(message, bot, cur, con):
    xxx = message.text
    cur.execute(f'''UPDATE id SET kluch = 0000 WHERE id = {message.chat.id} ''')
    con.commit()
    bot.send_message(message.chat.id, f'Проверка на сколько % [{xxx}](tg://user?id={message.from_user.id}) \
     пидор...', disable_web_page_preview=True,
                     parse_mode="Markdown")
    dd = bot.send_message(message.chat.id, "Загрузка.")
    for _ in range(1):
        bot.edit_message_text("Загрузка..", message.chat.id, dd.id)
        bot.edit_message_text("Загрузка...", message.chat.id, dd.id)
        bot.edit_message_text("Загрузка....", message.chat.id, dd.id)
        bot.edit_message_text("Загрузка.....", message.chat.id, dd.id)
        bot.edit_message_text("Загрузка.", message.chat.id, dd.id)
    bot.edit_message_text("Подсчет результатов...", message.chat.id, dd.id)
    time.sleep(4)
    bot.edit_message_text("Соединение с сервером...", message.chat.id, dd.id)
    time.sleep(4)
    bot.edit_message_text("Выявление окончательного ответа...", message.chat.id, dd.id)
    time.sleep(4)
    bot.edit_message_text("Поздравляем!", message.chat.id, dd.id)
    bot.send_message(message.chat.id, f'[{xxx}](tg://user?id={message.from_user.id}) пиздец пидорас на все \
{random.randrange(0, 100, 5)}%', disable_web_page_preview=True, parse_mode="Markdown")
    cur.execute(f'''UPDATE id SET kluch = 1111 WHERE id = {message.chat.id} ''')
    con.commit()


def jopaa(s, message, bot, cur, con):
    if "да" in s or "д" in s:
        cur.execute(f'''UPDATE id SET kluch = 0000000 WHERE id = {message.chat.id} ''')
        con.commit()
        bot.send_message(message.chat.id, "Пизда")
        dd = bot.send_message(message.chat.id, "Загрузка.")
        time.sleep(5)
        for _ in range(1):
            bot.edit_message_text("Загрузка..", message.chat.id, dd.id)
            time.sleep(5)
            bot.edit_message_text("Загрузка...", message.chat.id, dd.id)
            time.sleep(5)
            bot.edit_message_text("Загрузка....", message.chat.id, dd.id)
            time.sleep(5)
            bot.edit_message_text("Загрузка.....", message.chat.id, dd.id)
            time.sleep(5)
            bot.edit_message_text("Загрузка.", message.chat.id, dd.id)
            time.sleep(5)
        for _ in range(10):
            bot.send_message(message.chat.id, "взлом жопы " * 200)
        bot.send_message(message.chat.id, "Это сделал [{}](tg://user?id={})"
                         .format(message.from_user.first_name, message.from_user.id),
                         disable_web_page_preview=True,
                         parse_mode="Markdown")
        cur.execute(f'''UPDATE id SET kluch = 1111 WHERE id = {message.chat.id} ''')
        con.commit()
    elif "нет" == message.text:
        bot.send_message(message.chat.id, "ок.")
        cur.execute(f'''UPDATE id SET kluch = 1111 WHERE id = {message.chat.id} ''')
        con.commit()
    else:
        bot.send_message(message.chat.id, text="Вы уверены?")


def admn(message, bot, cur, con):
    try:
        zxc = d["admmm"]
    except:
        d["admmm"] = 99
        zxc = d["admmm"]
    if zxc == 99:
        if message.text == "айди":
            bot.send_message(message.chat.id, "айди")
            try:
                bot.send_message(message.chat.id, d["admdd"])
                d["admmm"] = 99
            except:
                bot.send_message(message.chat.id, "none")
                d["admmm"] = 99
        elif message.text == "какой":
            bot.send_message(message.chat.id, "какой")
            d["admmm"] = 97
            bot.send_message(message.chat.id, "какой")
        elif message.text == "письмо":
            bot.send_message(message.chat.id, "письмо")
            d["admmm"] = 95
            bot.send_message(message.chat.id, "письмо")
        elif message.text == "стоп!!":
            bot.send_message(message.chat.id, "стоп")
            d[f'{message.chat.id}'] = 1111
    elif zxc == 97:
        d["admdd"] = message.text
        d["admmm"] = 99
    elif zxc == 95:
        if message.text == "кон!":
            bot.send_message(message.chat.id, "кон!")
            d["admmm"] = 99
        else:
            bot.send_message(message.chat.id, "ща")
            bot.send_message(int(d["admdd"]), message.text)


def handle_docs_photo(message, bot, cur, con):
    if message.chat.id == 466348470:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'pic/' + file_info.file_path
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "Добавил фото, господин")
    else:
        bot.reply_to(message, "Ок, я отправил твою ничтожную пикчу на рассмотрение")
        bot.send_message(466348470, "[{}](tg://user?id={}) предложил пикчу:"
                         .format(message.from_user.first_name, message.from_user.id), disable_web_page_preview=True,
                         parse_mode="Markdown")
        bot.forward_message(466348470, message.chat.id, message.id)
        cur.execute(f'''UPDATE id SET kluch = 1111 WHERE id = {message.chat.id} ''')
        con.commit()
