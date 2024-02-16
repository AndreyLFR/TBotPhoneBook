from telegram.ext import ConversationHandler, CallbackContext
from telegram import Update
from Commands.base_commands import download_data, save_data
from Handlers.handler_main import *

def search_name_for_edit(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    data_array = download_data('phone_book.json')
    amount_coincidences = 0
    for data in data_array:
        if text in data['name']:
            update.message.reply_text(f'{data}')
            amount_coincidences += 1
    update.message.reply_text('Поиск завершен. Укажите id для редактирования: ')
    if amount_coincidences != 0: return OP_INPUT_ID_FOR_EDIT
    else:
        update.message.reply_text('Поиск не дал результата. Попробуй ввести другое имя: ')
        return OP_SEARCH_NAME_FOR_EDIT

def input_id_for_edit(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    data_array = download_data('phone_book.json')
    if text.isdigit():
        id = int(text)
        for data in data_array:
            if data['id'] == id:
                data['id'] == -id
        data_array.append(data)
        save_data('phone_book.json', data_array)
        update.message.reply_text('Введите новое имя: ')
        return OP_INPUT_NAME_FOR_EDIT
    else:
        update.message.reply_text('Введен некорректный id. Укажи повторно:')
        return OP_INPUT_ID_FOR_EDIT

def input_name_for_edit(update: Update, context: CallbackContext) -> int:
    name = update.message.text
    data_array = download_data('phone_book.json')
    out_data_array = []
    for data in data_array:
        if data['id'] < 0:
            data['name'] = name
        out_data_array.append(data)
    update.message.reply_text('Введите новый номер:')
    return OP_INPUT_NUMBER_FOR_EDIT

def input_number_for_edit(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    if not text.isdigit():
        update.message.reply_text('Введен некорректный номер. Введите числами повторно:')
        return OP_INPUT_NUMBER_FOR_EDIT
    else:
        number = int(text)
        data_array = download_data('phone_book.json')
        out_data_array = []
        for data in data_array:
            id = data['id']
            if id < 0:
                data['number'] = number
                data['id'] = -id
            out_data_array.append(data)
        update.message.reply_text('Изменения сохранены.')
        return ConversationHandler.END