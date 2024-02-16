import logging
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from Commands.command_handler import start, choice_search_contact, add_contact, delete_contact, edit_contact
from Handlers.handler_search import search_contact_handler, search_name_contact, search_number_contact
from Handlers.handler_add import input_name_contact, input_number_contact
from Handlers.handler_delete import search_name_for_delete, input_id_for_delete
from Handlers.handler_edit import search_name_for_edit, input_id_for_edit, input_name_for_edit, input_number_for_edit
from Handlers.handler_main import *

# Создайте Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создайте обработчик для записи данных в файл
logger_handler = logging.FileHandler('botlog.log')
logger_handler.setLevel(logging.INFO)

# Создайте Formatter для форматирования сообщений в логе
logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

# Добавьте Formatter в обработчик
logger_handler.setFormatter(logger_formatter)

# Добавьте обработчик в Logger
logger.addHandler(logger_handler)
logger.info('Настройка логгирования окончена!')

TOKEN = ""


def main() -> None:
    """Start the bot."""
    logger.info('Проверка токена')
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    logger.info('Запуск команды start')

    dispatcher.add_handler(CommandHandler('start', start))

    search_contact_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('search_contact', choice_search_contact)],
        states={
            OP_SEARCH_CONTACT: [CallbackQueryHandler(search_contact_handler)],
            OP_SEARCH_NAME_CONTACT: [MessageHandler(Filters.text, search_name_contact)],
            OP_SEARCH_NUMBER_CONTACT: [MessageHandler(Filters.text, search_number_contact)]
        },
        fallbacks=[]
    )

    add_contact_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add_contact', add_contact)],
        states={
            OP_INPUT_NAME_CONTACT: [MessageHandler(Filters.text, input_name_contact)],
            OP_INPUT_NUMBER_CONTACT: [MessageHandler(Filters.text, input_number_contact)],
        },
        fallbacks=[]
    )

    delete_contact_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('delete_contact', delete_contact)],
        states={
            OP_SEARCH_NAME_FOR_DELETE: [MessageHandler(Filters.text, search_name_for_delete)],
            OP_INPUT_ID_CONTACT_FOR_DELETE: [MessageHandler(Filters.text, input_id_for_delete)],
        },
        fallbacks=[]
    )

    edit_contact_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('edit_contact', edit_contact)],
        states={
            OP_SEARCH_NAME_FOR_EDIT: [MessageHandler(Filters.text, search_name_for_edit)],
            OP_INPUT_ID_FOR_EDIT: [MessageHandler(Filters.text, input_id_for_edit)],
            OP_INPUT_NAME_FOR_EDIT: [MessageHandler(Filters.text, input_name_for_edit)],
            OP_INPUT_NUMBER_FOR_EDIT: [MessageHandler(Filters.text, input_number_for_edit)]
        },
        fallbacks=[]
    )

    dispatcher.add_handler(search_contact_conv_handler)
    dispatcher.add_handler(add_contact_conv_handler)
    dispatcher.add_handler(delete_contact_conv_handler)
    dispatcher.add_handler(edit_contact_conv_handler)
    updater.start_polling()
    updater.idle()
    logger.info('Работа программы завершена')

if __name__ == '__main__':
    main()
