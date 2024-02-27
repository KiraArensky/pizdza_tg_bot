import pymorphy2
import time


def user_mute(message, bot):
    morph = pymorphy2.MorphAnalyzer()

    try:
        mute_time = int(message.text[6:]) * 60
    except ValueError:
        mute_time = 60

    comment = morph.parse('минуту')[0]
    msg_text = comment.make_agree_with_number(int(mute_time / 60)).word

    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAIC-mLa6-18z-1E9KJEj45-jh-yDa24AAIeGgACPDxxSo3gZaQZq5ewKQQ")
    try:
        bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                 until_date=time.time() + mute_time)
        bot.send_message(message.chat.id,
                         f'[Чурка](tg://user?id={message.reply_to_message.from_user.id}) ты в муте на'
                         f' {int(mute_time / 60)} {msg_text}',
                         disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as e:
        bot.send_message(message.chat.id,
                         "Чел, ты ошибся, дурак...")
