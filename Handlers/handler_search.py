from telegram.ext import CallbackContext, ConversationHandler
from telegram import Update
from Commands.base_commands import download_data
from Handlers.handler_main import OP_SEARCH_NAME_CONTACT, OP_SEARCH_NUMBER_CONTACT

def search_contact_handler (update: Update, context: CallbackContext) -> int:
    if update.callback_query.data == 'name':
        update.callback_query.message.edit_text("Введите имя контакта: ")
        return OP_SEARCH_NAME_CONTACT
    elif update.callback_query.data == 'number':
        update.callback_query.message.edit_text("Введите номер: ")
        return OP_SEARCH_NUMBER_CONTACT

def search_name_contact(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    data_array = download_data('phone_book.json')
    for data in data_array:
        if text in data['name']:
            update.message.reply_text(f'{data}')
    update.message.reply_text('Поиск завершен')
    return ConversationHandler.END

def search_number_contact(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    if text.isdigit():
        data_array = download_data('phone_book.json')
        for data in data_array:
            number_in_book = str(data['number'])
            number_search = text
            print(number_in_book)
            print(number_search)
            if number_search in number_in_book:
                update.message.reply_text(f'{data}')
        update.message.reply_text('Поиск завершен')
        return ConversationHandler.END
    else:
        update.message.reply_text('Некорректное значение')
        return OP_SEARCH_NUMBER_CONTACT