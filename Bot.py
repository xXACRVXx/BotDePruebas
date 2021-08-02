# este bot forma parte de el repositorio de GitHub https://github.com/xXACRVXx/bot_deseo bajo licencia MIT

import os
import sys
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# TOKEN contiene el token de telegram necesario para que el bot funcione se extrae en este caso de la variable de entorno configurada en Heroku


TOKEN = os.getenv("TOKEN")



# el # para reenviar los archivos
#Hastag1 = '#hentai'
Hastag1 = '#prueba'

# el # para enviar sugerencias al canal de los administradores
Hastag2 = '#deseo'


# aqui se pone el grupo o canal al que desea reenviar los mensajes que contengan #hentai
#Canal_hastag1= '@solo_hentai_s3'

Canal_hastag1= '@canalparaprobarbots'



# aqui se pone el grupo o canal al que desea reenviar los mensajes que contengan #deseo
Canal_hastag2 ='-1001407312660'




# grupo donde se encuentran los administradores de el bot
#Admins_Grupo = '-1001255367733'
Admins_Grupo = '@grupo_para_probar_bots'


# aquí terminan los parámetros editables de el bot
##############################################################################


# modo = [] controla el reenvío de arcivos del bot se guarda str("1") si el bot es desactivado por los admiradores o se deja vacía para que funcione
modo = []

# lista de usuarios ignorados por el bot
ignore = []



print('By Python 3.8')

# def admins(Contextbot, Usuario_id ): controla los administradores devolviendo EsAdmin = True en caso de que el usuario sea administrador de el grupo definido en ChatId
def admins(Contextbot, Usuario_id ):
  
  ChatId = Admins_Grupo
  
  GrupoAdmins = Contextbot.get_chat_administrators(ChatId)
  
  EsAdmin = False
  for admin in GrupoAdmins:
        if admin.user.id == Usuario_id:
           EsAdmin = True
  return EsAdmin


# el comando /start cumple 2 funciones, si un usuario no es administrador responde un mensaje para indicar que está funcionando correctamente pero si el usuario es un administrador aciva el reenvío de archivos en caso de estar desactivado
def start(update, context):
          
   Usuario2 =update.effective_user['username']
  
   print(Usuario2)
  
   Usuario_id = update.effective_user['id']
   
   Contextbot = context.bot
   
   

   if admins(Contextbot, Usuario_id) == True :  
      
      update.message.reply_text(f"@{Usuario2}-Sama El reenvío de multimedia a sido activado ")
      
      if modo.__contains__('1'):
         modo.remove('1')
         return modo
         print(modo)
      
         
   else:   
     
      update.message.reply_text("""Bot hentai_s3 funcionando""")

# el comando /stop cumplela funcion contraria al /start desactivando el reenvio de archivos
def stop(update, context):
      
   Usuario2 =update.effective_user['username']
   
   print(Usuario2)

   Usuario_id = update.effective_user['id']
   
   Contextbot = context.bot
   

   if admins(Contextbot, Usuario_id) == True :  
      update.message.reply_text(f"@{Usuario2}-Sama El reenvío de multimedia a sido desactivado ")
      modo.append('1')
      print(modo)
      return modo

# el comando /updates muestra el Historial de cambios de las actualizaciones del bot
def updates(update, context):
      update.message.reply_text( """Historial de cambios ver: 1.5.7\n\ninformacion clasificada hasta que me entren ganas de escribir """ )

# en def mensajes_entrantes(update, context): es donde se maneja la mayoría de mensajes que entran y salen hacia Telegram convirtiendolo en una de las partes fundamentales del bot
def mensajes_entrantes(update, context):
     Texto= update.message.text
     Grupo= update.message.chat.title
     Usuario= update.effective_user['first_name']
     Usuario2= update.effective_user['username']
     
     Id_grupo = update.message.chat.id
     
     # Subtitulos se utiliza en los archivos que contienen texto
     Subtitulos = update.message.caption
     
     Usuario_id = update.effective_user['id']
   
     Contextbot = context.bot
   
   
     # esto es opcional solo esta aquí como alternativa a /start y /stop en caso de existir muchos bots en un grupo y asi no tengan que responder todos al conando /start
     if admins(Contextbot, Usuario_id) == True :  
       if str(Texto).startswith('-off'):
          update.message.reply_text(f"@{Usuario2}-Sama El reenvío de multimedia a sido desactivado ")
          modo.append('1')
          print(modo)
          return modo
          
          update.message.reply_text(f"@{Usuario2}-Sama El reenvío de multimedia a sido activado ")
      
       if str(Texto).startswith('-on'):
         if modo.__contains__('1'):
          modo.remove('1')
          return modo
          print(modo)
       
       if str(Texto).startswith('-modo'):
         
          update.message.reply_text(str(modo))
        
     
     # aqui es donde se permite o no el reenvío de archivos si la lista modo=[] no contiene '1'
     if not modo.__contains__('1') :
       
         # si el usuario que utiliza el #hentai no es Telegram se reenviar los archivos o el mensaje esto se utiliza para evitar que el bot caiga en bucle
         if not str(Usuario) == 'Telegram':
           
           if str(Subtitulos).__contains__(Hastag1):
            Id_mensage = update.message.message_id
            context.bot.forward_message(chat_id=Canal_hastag1 ,from_chat_id = Id_grupo , message_id= Id_mensage )
           
           if str(Texto).startswith(Hastag1):
            Id_mensage_re = update.message.reply_to_message.message_id
            
            context.bot.forward_message(chat_id=Canal_hastag1 ,from_chat_id = Id_grupo , message_id= Id_mensage_re )
            update.message.reply_text("Tu mensaje fue enviado")
     
     # en caso de estar desactivado el reenvío de el bot y se envie un mensaje que contenga #hentai se enviara un mensaje como feedback al usuario para que sepa la razon por la cual no funcionó
     else:
       
        if not str(Usuario) == 'Telegram':
           
           if str(Subtitulos).__contains__(Hastag1):
             
            update.message.reply_text("El reenvío fue desactivado")
     
           if str(Texto).startswith(Hastag1):
     
            update.message.reply_text("El reenvío fue desactivado")
     
      
     # si se envia el texto #deseo un grupo donde se encuentre el bot este reenviará el mensaje a el grupo establecido en chat_id='' y devolvera un mensaje de feedback  
     if str(Texto).startswith(Hastag2):
      context.bot.send_message(chat_id=Canal_hastag2,text=f"Grupo:{str(Grupo).replace('None', 'privado' )}\nUsuario: {str(Usuario).replace('None','Anónimo')} @{str(Usuario2)}\n\nt.me/{update.message.chat.username}/{update.message.message_id}\n\n{str(Texto)}")
      
      update.message.reply_text("Tu deseo fue enviado")
      

# aqui comienza la ejecución del bot   
if __name__ == "__main__":
  
    # el objeto Hentaibot contiene el token de telegram obtenido de la variable TOKEN y otros datos 
    Hentaibot = telegram.Bot(token=TOKEN)
 
 # actualizador contiene el objeto Hentaibot y extrae el token de telegram mas use_context=True necesario para el funcionamiento de el bot
actualizador = Updater(Hentaibot.token, use_context=True)
 
 # despachador normalmente nombrado dp extrae el dispatcher de el objeto actualizador      
despachador = actualizador.dispatcher

# aqui se definen los comandos a los que reacciona el bot
despachador.add_handler(CommandHandler('start', start))

despachador.add_handler(CommandHandler('stop', stop))

despachador.add_handler(CommandHandler('updates', updates))

despachador.add_handler(MessageHandler(filters=Filters.all, callback= mensajes_entrantes))


   
print('\nIniciando\n')
  
actualizador.start_polling()
  
actualizador.idle   
