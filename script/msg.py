import time
import os
import random
import json


def msg_func(s, message, bot, cur, con):
    f = open('database/json/insults.json')
    data = json.load(f)
    assss = data['list_insults']
    f.close()

    f = open('database/json/user_loh.json')
    data = json.load(f)
    lohhh = data['id_lohov']
    f.close()

    if message.from_user.id in lohhh:
        bot.reply_to(message, f'{random.choice(assss)}')

    elif "/lohh" in message.text or "/lohh@pizdza_bot" in message.text:
        f = open('database/json/user_loh.json')
        data = json.load(f)
        lohhh = data['id_lohov']
        f.close()

        try:
            if message.from_user.id not in lohhh.keys():
                if message.reply_to_message.from_user.id == 466348470:
                    lohhh[message.from_user.id] = message.reply_to_message.from_user.id
                    new_data = {f'{message.from_user.id}': message.reply_to_message.from_user.id}
                    with open('database/json/user_loh.json', encoding='utf8') as f:
                        data = json.load(f)
                    data['id_lohov'].append(new_data)
                    with open('database/json/user_loh.json', 'w', encoding='utf8') as outfile:
                        json.dump(data, outfile, ensure_ascii=False,
                                  indent=2)

                    bot.send_message(message.chat.id,
                                     f'[Котик](tg://user?id={message.from_user.id}) теперь лох',
                                     disable_web_page_preview=True,
                                     parse_mode="Markdown")
                else:
                    new_data = {f'{message.reply_to_message.from_user.id}': message.from_user.id}
                    with open('database/json/user_loh.json', encoding='utf8') as f:
                        data = json.load(f)
                    data['id_lohov'].append(new_data)
                    with open('database/json/user_loh.json', 'w', encoding='utf8') as outfile:
                        json.dump(data, outfile, ensure_ascii=False,
                                  indent=2)

                    bot.send_message(message.chat.id,
                                     f'[Котик](tg://user?id={message.reply_to_message.from_user.id}) теперь лох',
                                     disable_web_page_preview=True,
                                     parse_mode="Markdown")
            else:
                bot.send_message(message.chat.id,
                                 f'[Котик](tg://user?id={message.from_user.id}) не может обзываться, он только мяукает',
                                 disable_web_page_preview=True,
                                 parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, "Для начала ответь на сообщение лоха, кочелыга")

    elif (("/nelohh" == message.text or "/nelohh@pizdza_bot" == message.text)
          and message.from_user.id in lohhh.values()):
        try:
            del lohhh[f'{message.reply_to_message.from_user.id}']
            bot.send_message(message.chat.id,
                             f'Окей, [ты](tg://user?id={message.reply_to_message.from_user.id}) больше не лох',
                             disable_web_page_preview=True,
                             parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, "Для начала ответь на сообщение провинившегося, зайчик")

    elif "похуй" in s:
        bot.send_message(message.chat.id, "нет")
        bot.send_message(message.chat.id, "это мне похуй")
        img = open('../database/photo/pohui.jpg', 'rb')
        bot.send_photo(message.chat.id, img)

    elif "Asd1236987" == message.text and message.chat.id == 466348470:
        bot.send_message(message.chat.id, "админка")
        cur.execute(f'''UPDATE id SET key = "admin_mode" WHERE id = {message.chat.id} ''')
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
                         \n\
    #Функционал_будет_пополнятся\n\
    \n\
        \n\
    Приятное дополнение: бот может мутить участников беседы (но не админов)!\n\
        \n\
    Для этого ответьте на сообщение обидчика так: "тише! {срок в минутах}"\n\
        \n\
    \n\
    Все ваши предложения можете писать мне: @pizdza_mnyam\n\
    \n\
    Также у меня есть канал: https://t.me/trudhochetsya\n\
    \n\
    Маме привет!')
        #     /lohh - обижает обидчика после каждого сообщения (ВАЖНО! команду нужно использовать ответив на сообщение обидчика)\n\
        #     /nelohh - прекратить обижать (отмена /lohh)\n\
    elif "да" in s or "д" in s:
        bot.send_message(message.chat.id, "Пизда")
    elif message.text == '/poh0' or "/poh0@pizdza_bot" == message.text:
        bot.send_message(message.chat.id, "poh_on")
        cur.execute(f'''UPDATE id SET key = "pohui_mode" WHERE id = {message.chat.id} ''')
        con.commit()
    elif "андрей" in s:
        bot.send_message(message.chat.id, "Уебан")
    elif "нет" in s:
        bot.send_message(message.chat.id, "Пидора ответ")
    elif "Шлюхи аргумент" == message.text or "шлюхи аргумент" == message.text or "аргумент" in s:
        bot.send_message(message.chat.id, "От шлюхи слышу")
    elif "нахуй" in s:
        bot.send_message(message.chat.id, f'Только {int(time.strftime("%H")) + 5}:{time.strftime("%M")}, '
                                          f'а [ты](tg://user?id={message.from_user.id}) уже идешь нахуй',
                         disable_web_page_preview=True, parse_mode="Markdown")
    elif "/pic" == message.text or "/pic@pizdza_bot" == message.text:
        dir = '../database/pic/photos'
        img = open(os.path.join(dir, random.choice(os.listdir(dir))), "rb")
        bot.send_photo(message.chat.id, img)
    elif "/pic_add" == message.text or "/pic_add@pizdza_bot" == message.text:
        cur.execute(f'''UPDATE id SET key = "pic" WHERE id = {message.chat.id} ''')
        con.commit()
        bot.send_message(message.chat.id, "Ну давай, отправь пикчу на рассмотрение")
    elif "Тест на пидора" == message.text or "/test" == message.text or "/test@pizdza_bot" == message.text:
        cur.execute(f'''UPDATE id SET key = "pidr_test" WHERE id = {message.chat.id} ''')
        con.commit()
        bot.send_message(message.chat.id, "Тест на пидора")
        bot.send_message(message.chat.id, "Как вас зовут?")
