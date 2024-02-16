from telegram.ext import ConversationHandler, CallbackContext
from telegram import Update
from Handlers.handler_main import OP_INPUT_ID_CONTACT_FOR_DELETE, OP_SEARCH_NAME_FOR_DELETE
from Commands.base_commands import download_data, save_data

def search_name_for_delete(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    data_array = download_data('phone_book.json')
    amount_coincidences = 0
    for data in data_array:
        if text in data['name']:
            update.message.reply_text(f'{data}')
            amount_coincidences += 1
    update.message.reply_text('Поиск завершен. Укажите id для удаления: ')
    if amount_coincidences != 0: return OP_INPUT_ID_CONTACT_FOR_DELETE
    else:
        update.message.reply_text('Поиск не дал результата. Попробуй ввести другое имя: ')
        return OP_SEARCH_NAME_FOR_DELETE

def input_id_for_delete(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    data_array = download_data('phone_book.json')
    out_data_array = []
    if text.isdigit():
        id = int(text)
        for data in data_array:
            if not data['id'] == id:
                out_data_array.append(data)
        save_data('phone_book.json', out_data_array)
        update.message.reply_text('Контакт удален')
        return ConversationHandler.END
    else:
        update.message.reply_text('Введен некорректный id. Укажи повторно:')
        return OP_INPUT_ID_CONTACT_FOR_DELETE