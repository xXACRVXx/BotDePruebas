from telegram.ext import Updater, CommandHandler, MessageHandler , Filters

def start(update, context):
      update.message.reply_text('Hola, humano\nSoy Xx_A_xX ver:0.08.32(beta)')

def anime(update, context):
      update.message.reply_text('Yo no puedo hacer eso :(')
      
def help(update, context):
         update.message.reply_text('hola por ahora no hago mucho solo  tengo /start /anime y /help pero también puedo enviar un mensaje con -say a mi grupo de soporte o a el que se halla configurado (esto solo lo puede cambiar mi administrador)')

#def process_chat(update, context): 
   
  # chat= update.message.chat
    
  # print(chat)
       
def process_message(update, context): 
   
   text= update.message.text
    
   print('Usuario: ' + text + ' \n')
   
   if str(text).__contains__('-say'):
      context.bot.send_message(chat_id='@Xx_A_xX_soporte',text=str(text).replace('-say', ''))
    
if __name__ == '__main__':
    

     actualizador =   Updater(token= input('pon el token de tu bot: ') , use_context=True)
     
     despachador = actualizador.dispatcher
    
     despachador.add_handler(CommandHandler('start', start))
     
     despachador.add_handler(CommandHandler('anime', anime))
     
     despachador.add_handler(CommandHandler('help', help))
     
     
     #despachador.add_handler(MessageHandler(filters = Filters.chat , callback = process_chat))
     
     despachador.add_handler(MessageHandler(filters = Filters.text , callback = process_message))
     
     actualizador.start_polling()
      
     print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ntoken aseptado exitosamente: \n\ncargando...\n\nbot iniciado\n\nfuncionando\n\nEn linea  \n\n")
     
     actualizador.idle()