from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CallbackQueryHandler, CommandHandler, MessageHandler, Filters
from translate import Translator
import psycopg2
import time

phone_number = None

conn = psycopg2.connect(
        host = 'localhost',
        dbname = 'postgres',
        user = 'postgres',
        password = 'Admin',
        port = 5432
    )

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255),
        phoneNumber VARCHAR(255),
        chatId BIGINT UNIQUE
    )
""")
conn.commit()

def contact_callback(update, context):
    global phone_number
    contact = update.effective_message.contact
    phone_number = contact.phone_number
    chat_id = update.message.chat_id
    username = update.message.chat.username
    update.message.reply_text(f"Thank you for sharing your phone number\n{phone_number}")
    cur.execute("INSERT INTO users (username, phoneNumber, chatId) VALUES (%s, %s, %s)",
                    (username, phone_number, chat_id))
    conn.commit()

    time.sleep(3)
    select_lang(update,context)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello, how are you doing?")
    time.sleep(1)
    chat_id = update.message.chat_id
        # check if user exists in database
    cur.execute("SELECT * FROM users WHERE chatId = %s", (chat_id,))
    user = cur.fetchone()

    if user is None:
        # Create a keyboard with a "Share Contact" button
        contact_button = KeyboardButton("Share Contact", request_contact=True)
        reply_markup = ReplyKeyboardMarkup([[contact_button]], resize_keyboard=True, one_time_keyboard=True)

        # Ask the user to share their contact information
        update.message.reply_text("Please share your contact information.", reply_markup=reply_markup)
    else:
        select_lang(update,context)

def updating():
    pass
    

def select_lang(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("German", callback_data="German"),
            InlineKeyboardButton("Spanish", callback_data="Spanish"),
            InlineKeyboardButton("French", callback_data="French")
    ],
    [
            InlineKeyboardButton("Italian", callback_data="Italian"),
            InlineKeyboardButton("Russian", callback_data="Russian"),
            InlineKeyboardButton("Kazakh", callback_data="Kazakh")
    ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(f'Choose the language you want to translate to', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    global lang
    lang = update.callback_query.data.lower()
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"{query.data} has been selected for translation! You can start translating your text")


def lang_translator(user_input):
    try:
        translator = Translator(from_lang='english', to_lang=lang)
        translation = translator.translate(user_input)
        return translation
    except Exception as e:
        return "An error occurred while translating your text.Please type the correct word"


def reply(update, context):
    user_input = update.message.text
        # translate user input to selected language and send reply
    translated_text = lang_translator(user_input)
    update.message.reply_text(translated_text)


def main():
    with open("api.txt", "r") as f:
        api = f.read().strip()
    updater = Updater(api, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.contact, contact_callback))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler("hello", start))
    dp.add_handler(CommandHandler('select_lang', select_lang))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text, reply))
    
    try:
        updater.start_polling()
        updater.idle()
    except Exception as e:
        print(e)
    
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()

