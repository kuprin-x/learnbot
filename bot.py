from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import helpdesk
import logging

TOKEN = helpdesk.TOKEN

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                     filename = 'bot.log')


def c_start (bot, update): #Функция обработчик start
    text = 'Вызван /start'
    # data_user = update.message #Можно осюда брать много данных о пользователе
    logging.info(text)
    update.message.reply_text("Тебя нету в базе ссори!")



def talk_to_me (bot, update):
    text_bot_message = update.message.text
    data_user_m = update.message #Получаем данные о пользователе
    logging.info("User: %s, Chat id: %s, Message: %s", data_user_m.chat.username, data_user_m.chat.id,  data_user_m.text) #Логируем данные о пользователе
    update.message.reply_text (f'@{data_user_m.chat.username} Ты мне прислал: \b{text_bot_message}') #Отправляем эхо




def main():
    mybot = Updater(TOKEN) #Подключение 

    logging.info("Start work bot")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', c_start)) # Определяет функцию для команды /старт
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling() #Проверка обновлений в боте
    mybot.idle()



main()