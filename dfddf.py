from mnam import *
import sqlite3
import time

try:
    import pymorphy2
except:
    system("pip install pymorphy2")
    import pymorphy2

try:
    import cowsay
except:
    system("pip install cowsay")
    import cowsay

try:
    import telebot
except:
    system("pip install pyTelegramBotAPI")
    import telebot

bot = telebot.TeleBot('#####')

print(cowsay.get_output_string('ghostbusters', "Работай сучка"))
[print("", end='\n') for _ in range(5)]
print("The ghost-free zone", "#####" * 50, sep="\n")

morph = pymorphy2.MorphAnalyzer()


@bot.message_handler(content_types=['text'])
def func(message):
    con = sqlite3.connect("database/chat.db")
    cur = con.cursor()
    try:
        k = cur.execute(f"""SELECT kluch FROM id WHERE id = {message.chat.id}""").fetchone()[0]
    except:
        cur.execute(
            f'''INSERT INTO id (id, kluch) VALUES({message.chat.id}, 1111) ''')
        k = cur.execute(f"""SELECT kluch FROM id WHERE id = {message.chat.id}""").fetchone()[0]
        con.commit()
    xxx = 'Лох'
    bot.send_message(5184714205, f'[Челик](tg://user?id={message.from_user.id}) печатает...\n\
    Его id: {message.from_user.id}\n\
    Чат id: {message.chat.id}', disable_web_page_preview=True,
                     parse_mode="Markdown")
    if k == 1111:
        if "тише!" in message.text or "Тише!" in message.text:
            try:
                loh = int(message.text[6:]) * 60
            except:
                loh = 60
            comment = morph.parse('минуту')[0]
            keks = comment.make_agree_with_number(int(loh / 60)).word
            bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAIC-mLa6-18z-1E9KJEj45-jh-yDa24AAIeGgACPDxxSo3gZaQZq5ewKQQ")
            try:
                bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=time.time()+loh)
                bot.send_message(message.chat.id,
                                 f'[Чурка](tg://user?id={message.reply_to_message.from_user.id}) ты в муте на {int(loh / 60)} {keks}',
                                 disable_web_page_preview=True, parse_mode="Markdown")
            except:
                bot.send_message(message.chat.id, "Чел, ты не ответил на сообщение чурки, которую ты хочешь замутить...")
                bot.send_message(message.chat.id, "Ну или где-то в другом месте обосрался, сам думай")
        s = []
        for i in message.text.lower().split():
            s.append("".join(c for c in i if c.isalpha()))
        slovs(s, message, bot, cur, con)
    elif k == 2222:
        poh(message, bot, cur, con)
    elif k == 3333:
        pidrr(message, bot, cur, con)
    elif k == 4444:
        s = []
        for i in message.text.lower().split():
            s.append("".join(c for c in i if c.isalpha()))
        jopaa(s, message, bot, cur, con)
    elif k == 123:
        admn(message, bot, cur, con)
    elif k == 5555:
        if message.chat.id == 466348470 and message.text == "Стоп!":
            cur.execute(f'''UPDATE id SET kluch = 1111 WHERE id = {message.chat.id} ''')
            con.commit()
            bot.reply_to(message, "Ура, Добби свободен")
        else:
            bot.reply_to(message, "Это не пикча дурак")


@bot.message_handler(content_types=['photo'])
def func(message):
    con = sqlite3.connect("database/chat.db")
    cur = con.cursor()
    try:
        k = cur.execute(f"""SELECT kluch FROM id WHERE id = {message.chat.id}""").fetchone()[0]
    except:
        cur.execute(
            f'''INSERT INTO id (id, kluch) VALUES({message.chat.id}, 1111) ''')
        k = cur.execute(f"""SELECT kluch FROM id WHERE id = {message.chat.id}""").fetchone()[0]
        con.commit()
    bot.send_message(5184714205, "[{}](tg://user?id={}) отправил фото..."
                     .format(message.from_user.first_name, message.from_user.id), disable_web_page_preview=True,
                     parse_mode="Markdown")
    print(message.from_user.first_name, message.chat.id)
    if k == 5555:
        handle_docs_photo(message, bot, cur, con)


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    bot.send_message(message.chat.id, "Welcome to the club, [buddy](tg://user?id={})"
                     .format(message.new_chat_members[0].id), disable_web_page_preview=True,
                     parse_mode="Markdown")


bot.polling(none_stop=True, interval=0)
