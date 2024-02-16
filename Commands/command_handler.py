from telegram.ext import CallbackContext, Updater
from telegram import Update
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from Handlers.handler_main import OP_INPUT_NAME_CONTACT, OP_SEARCH_NAME_FOR_DELETE, OP_SEARCH_CONTACT, OP_SEARCH_NAME_FOR_EDIT
import csv
from Commands.base_commands import download_data

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f"Привет {user.first_name}!\nСписок команд:\n1) найти контакт - /search_contact\n"
                              f"2) добавить контакт - /add_contact \n3) удалить контакт - /delete_contact\n4) "
                              f"изменить контакт - /edit_contact")

def choice_search_contact(update: Update, context: CallbackContext) -> int:
    kb = [
        [InlineKeyboardButton("по имени", callback_data="name"),
         InlineKeyboardButton("по номеру телефона", callback_data="number")],
    ]
    reply_kb_markup = InlineKeyboardMarkup(kb)
    update.message.reply_text(f"Выберите параметр поиска: ", reply_markup=reply_kb_markup)
    return OP_SEARCH_CONTACT

def add_contact(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    update.message.reply_text(f"{user.first_name}!\nВведите имя контакта: ")
    return OP_INPUT_NAME_CONTACT

def delete_contact(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    update.message.reply_text(f"{user.first_name}!\nВведите имя контакта: ")
    return OP_SEARCH_NAME_FOR_DELETE

def edit_contact(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    update.message.reply_text(f"{user.first_name}!\nВведите имя контакта: ")
    return OP_SEARCH_NAME_FOR_EDIT


