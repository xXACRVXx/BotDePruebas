from telegram.ext import Updater, CommandHandler

def start(update, context):
      update.message.reply_text('Hola, humano')
      
def help(update, context):
         update.message.reply_text('por ahora solo dice Hola humano cuando escribes /start')

if __name__ == '__main__':
    
     updater =        Updater(token='you token', use_context=True)
     
     dp = updater.dispatcher
    
     dp.add_handler(CommandHandler('start', start))
     
     dp.add_handler(CommandHandler('help', help))
     
     updater.start_polling()
      
     print("bot iniciado")
     
     updater.idle()

