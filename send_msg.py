import os
import configparser
import telebot

# Creating an instance of the bot
try:
    file_dir = os.path.dirname(os.path.abspath(__file__))

    # Reading bot token and chat id from configuration file
    config = configparser.ConfigParser()
    config_file_path = os.path.join(file_dir, 'config.ini')
    config.read(config_file_path)

    bot_token = config.get('telegram', 'bot_token')
    chat_id = config.get('telegram', 'chat_id')

    bot = telebot.TeleBot(bot_token)
except configparser.Error as e:
    print('Configuration file error:', e)


# Defining functions for sending text messages and public URLs
def send_text_msg(text):
    try:
        bot.send_message(chat_id, text)
    except telebot.apihelper.ApiException as e:
        print('Failed to send message:', e)


def send_public_url(url):
    if not url:
        send_text_msg('Start Local Stable Diffusion')
    else:
        send_text_msg(url)


# Starting the bot and printing a message to the console
if __name__ == '__main__':
    send_text_msg('Start Bot')
    print('Bot loaded')
