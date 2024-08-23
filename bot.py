import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = os.getenv("TOKEN")

CHAT_DESTINAZIONE = "@TuttoModding"  

CANALI_MONITORATI = {
    '@garnet_updates': 'rn13pro5g / PocoX6',
    '@PocoF6GlobalUpdate': 'POCO F6',
    '@Redmi10CUpdates': 'Redmi 10c',    
    '@setupTommo23': 'test',    
}

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('my job is to forward the new roms of your device.')

async def inoltra_messaggio(update: Update, context: CallbackContext) -> None:
    if update.message and update.message.chat:
        canale = update.message.chat.username
        if canale in CANALI_MONITORATI:
            nome_canale = CANALI_MONITORATI[canale]
            testo_inoltrato = f"Nuova ROM per {nome_canale}\n\n{update.message.text}"
            await context.bot.send_message(chat_id=CHAT_DESTINAZIONE, text=testo_inoltrato)
    else:
        # Messaggio di debug per aggiornamenti non validi
        print("L'aggiornamento ricevuto non contiene un messaggio valido.")

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & filters.ChatType.CHANNEL, inoltra_messaggio))

    application.run_polling()

if __name__ == '__main__':
    main()
