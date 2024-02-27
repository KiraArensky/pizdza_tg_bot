def admn(message, bot, cur, con):
    if cur.execute(f"""SELECT admin FROM id WHERE id = {message.chat.id}""").fetchone()[0]:
        if message.text == "кон!":
            bot.send_message(message.chat.id, "стоп")
            cur.execute(f'''UPDATE id SET key = "default" WHERE id = {message.chat.id} ''')
            con.commit()
        elif message.text == "команды":
            bot.send_message(message.chat.id, "стоп - отключение режима админа\n"
                                              "команды - список команд админа\n"
                                              "стоп! - отключение режима пикчи\n")

