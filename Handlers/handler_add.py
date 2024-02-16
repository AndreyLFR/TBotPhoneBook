from telegram.ext import ConversationHandler, CallbackContext
from telegram import Update
from Commands.base_commands import download_data, save_data, save_dict_data
from Handlers.handler_main import OP_INPUT_NAME_CONTACT, OP_INPUT_NUMBER_CONTACT

def input_name_contact(update: Update, context: CallbackContext) -> int:
    data_array = download_data('phone_book.json')
    name = update.message.text
    #проверяем пустой справочник или нет
    if len(data_array) == 0:
        id = 1
        save_dict_data(name, id, data_array)
    else:
        # проверяем завершился ли процесс предыдущего сохранения контакта
        if data_array[-1]['number'] != None:
            id = data_array[-1]['id'] + 1
            save_dict_data(name, id, data_array)
    update.message.reply_text('Введите номер контакта: ')
    return OP_INPUT_NUMBER_CONTACT

def input_number_contact(update: Update, context: CallbackContext) -> int:
    input_text = update.message.text
    if not input_text.isdigit():
        update.message.reply_text('Введено некорректное значение.')
        return OP_INPUT_NAME_CONTACT
    else:
        number = int(input_text)
        data_array = download_data('phone_book.json')
        data = data_array[-1]
        data['number'] = number
        save_data('phone_book.json', data_array)
        update.message.reply_text('Контакт сохранен')
    return ConversationHandler.END