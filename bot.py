# programmed by toommo23

import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = os.getenv("TOKEN")

CHAT_DESTINAZIONE = "@TuttoModding"  

CANALI_MONITORATI = {
    '@garnet_updates': 'rn13pro5g / PocoX6',
    '@PocoF6GlobalUpdate': 'POCO F6',
    '@Redmi10CUpdates': 'Redmi 10c',    
    '@setupTommo23': 'test',    
}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('my job is to forward the new roms of your device.')

def inoltra_messaggio(update: Update, context: CallbackContext) -> None:
    canale = update.message.chat.username
    if canale in CANALI_MONITORATI:
        nome_canale = CANALI_MONITORATI[canale]
        testo_inoltrato = f"Nuova ROM per {nome_canale}\n\n{update.message.text}"
        context.bot.send_message(chat_id=CHAT_DESTINAZIONE, text=testo_inoltrato)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.chat_type.channel, inoltra_messaggio))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
