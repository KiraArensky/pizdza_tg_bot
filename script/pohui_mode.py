def poh(message, bot, cur, con):
    if message.text == '/poh1' or "/poh1@pizdza_bot" == message.text:
        bot.send_message(message.chat.id, "poh_off")
        cur.execute(f'''UPDATE id SET key = "default" WHERE id = {message.chat.id} ''')
        con.commit()
    else:
        bot.send_message(message.chat.id, "Да мне похуй.")
