import sqlite3
import traceback
from os import system

from script.admin_mode import admn
from script.mute import user_mute
from script.msg import *
from database.config import token_bot
from script.pic import pic_add
from script.pidr_test import pidrr
from script.pohui_mode import poh

try:
    import pymorphy2
    import cowsay
    import telebot
except ImportError:
    system("pip install -r requirements.txt")
    import pymorphy2
    import cowsay
    import telebot

bot = telebot.TeleBot(token_bot)

print(cowsay.get_output_string('ghostbusters', "Работай сучка"))


@bot.message_handler(commands=['start'])  # Запуск бота
def start(message):
    con = sqlite3.connect("db/chats.db")  # Подключение к базе данных
    cur = con.cursor()  # Создание курсора

    result = cur.execute("""SELECT id FROM id""").fetchall()  # Получение всех айди из базы данных
    id_list = [elem[0] for elem in result]

    if message.chat.id not in id_list:  # Если айди нет в базе данных, то добавляем его
        cur.execute(
            f'''INSERT INTO id (id) VALUES({message.chat.id}) ''')
        con.commit()
    con.close()  # Закрытие базы данных

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
       Также у меня есть канал: https://t.me/trudhochetsya\n\
       \n\
       Маме привет!')


@bot.message_handler(content_types=['text'])
def message_text(message):
    con = sqlite3.connect("database/chat.db")
    cur = con.cursor()

    try:
        key = cur.execute(f"""SELECT key FROM id WHERE id = {message.chat.id}""").fetchone()[0]

    except Exception as e:
        cur.execute(
            f'''INSERT INTO id (id) VALUES({message.chat.id}) ''')
        con.commit()
        key = "default"

    bot.send_message(466348470, f'[Челик](tg://user?id={message.from_user.id}) печатает...'
                                f'\nЕго id: {message.from_user.id}'
                                f'\nЧат id: {message.chat.id}', disable_web_page_preview=True,
                     parse_mode="Markdown")

    if key == "default":
        if "тише!" in message.text or "Тише!" in message.text:
            user_mute(message, bot)

        msg_text = []
        for i in message.text.lower().split():
            msg_text.append("".join(c for c in i if c.isalpha()))
        msg_func(msg_text, message, bot, cur, con)

    elif key == "pohui_mode":
        poh(message, bot, cur, con)

    elif key == "pidr_test":
        pidrr(message, bot, cur, con)

    elif key == "admin_mode":
        admn(message, bot, cur, con)

    elif key == "pic":
        if message.chat.id == 466348470 and message.text == "cтоп!":
            cur.execute(f'''UPDATE id SET key = "default" WHERE id = {message.chat.id} ''')
            con.commit()
            bot.reply_to(message, "Ура, Добби свободен")
        else:
            bot.reply_to(message, "Это не пикча дурак")


@bot.message_handler(content_types=['photo'])
def message_photo(message):
    con = sqlite3.connect("database/chat.db")
    cur = con.cursor()

    try:
        k = cur.execute(f"""SELECT kluch FROM id WHERE id = {message.chat.id}""").fetchone()[0]
    except Exception as e:
        cur.execute(
            f'''INSERT INTO id (id, kluch) VALUES({message.chat.id}, 1111) ''')
        k = cur.execute(f"""SELECT kluch FROM id WHERE id = {message.chat.id}""").fetchone()[0]
        con.commit()
    bot.send_message(5184714205, "[{}](tg://user?id={}) отправил фото..."
                     .format(message.from_user.first_name, message.from_user.id), disable_web_page_preview=True,
                     parse_mode="Markdown")
    print(message.from_user.first_name, message.chat.id)
    if k == "pic":
        pic_add(message, bot, cur, con)


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    bot.send_message(message.chat.id, "Welcome to the club, [buddy](tg://user?id={})"
                     .format(message.new_chat_members[0].id), disable_web_page_preview=True,
                     parse_mode="Markdown")


def telegram_polling():
    try:
        bot.polling()  # Опрос сервера Telegram на предмет новых сообщений
    except Exception as e:
        traceback_error_string = traceback.format_exc()  # Здесь хранится информация об ошибке
        with open("Error.Log", "a") as myfile:  # Запись ошибки в файл Error.Log
            myfile.write("\r\n\r\n" + time.strftime(
                "%c") + "\r\n<<ERROR polling>>\r\n" + traceback_error_string + "\r\n<<ERROR polling>>")
        bot.stop_polling()  # Перезапуск бота
        time.sleep(10)
        telegram_polling()


if __name__ == '__main__':
    telegram_polling()  # Запуск бота
