def pic_add(message, bot, cur, con):
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

        cur.execute(f'''UPDATE id SET key = "default" WHERE id = {message.chat.id} ''')
        con.commit()