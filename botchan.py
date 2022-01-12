# este bot forma parte de el repositorio de GitHub https://github.com/xXACRVXx/bot_deseo bajo licencia MIT
from os import system
import os
import Logopython
import sys
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from subprocess import call, check_output

system('clear')


print('######################################################################')

print(f"Botchan Shiromi corriendo en: ")

system('python --version')

print('\n')
try:
 system('neofetch')
except:
  print('Instale neofetch en su equipo con apt install neofetch')



# TOKEN contiene el token de telegram necesario para que el bot funcione se extrae en este caso de la variable de entorno configurada en Heroku
TOKEN = os.getenv("TOKEN")


# el # para reenviar los archivos
#Hastag1 = '#shiromi'
Hastag1 = '#prueba'

# el # para enviar sugerencias al canal de los administradores
Hastag2 = '#deseo2'


# aqui se pone el grupo o canal al que desea reenviar los mensajes que contengan #shiromi
#Canal_hastag1= '@solo_shiromi_s3'

Canal_hastag1= '@canalparaprobarbots'



# aqui se pone el grupo o canal al que desea reenviar los mensajes que contengan #deseo
Canal_hastag2 ='@deseos_solo_shiromi_desu'

#Canal_hastag2 = '@canalparaprobarbots'


# el grupo de donde estan los usuarios que interactúan con el bot
#GrupoPrincipal = '@shiromi_s3'
GrupoPrincipal = '@grupo_para_probar_bots'

# grupo donde se encuentran los administradores de el bot
#Admins_Grupo = '-1001255367733'
Admins_Grupo = '@grupo_para_probar_bots'


# aquí terminan los parámetros editables de el bot
##############################################################################




# modo = [] controla el reenvío de arcivos del bot se guarda str("1") si el bot es desactivado por los admiradores o se deja vacía para que funcione
modo = []

# lista de usuarios ignorados por el bot
ignore = []

dev_modo = []





# def admins(Contextbot, Usuario_id ): controla los administradores devolviendo EsAdmin = True en caso de que el usuario sea administrador de el grupo definido en ChatId
def admins(Contextbot, Usuario_id ):
  
  ChatId = Admins_Grupo
  
  GrupoAdmins = Contextbot.get_chat_administrators(ChatId)
  
  EsAdmin = False
  for admin in GrupoAdmins:
        if admin.user.id == Usuario_id:
           EsAdmin = True
  return EsAdmin


# a diferencia de admins(), alladmins() incluye a todos los administradores y no solo a los del grupo de administradores 
def alladmins(Contextbot, Usuario_id):
  
  ChatId = GrupoPrincipal
  
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
      
      update.message.reply_text(f"@{Usuario2} El reenvío de multimedia a sido activado ")
      
      if modo.__contains__('desactivado'):
         modo.remove('desactivado')
         return modo
         print(modo)
      
         
   else:   
     
      update.message.reply_text("""Bot shiromi_s3 funcionando""")

# el comando /stop cumplela funcion contraria al /start desactivando el reenvio de archivos
def stop(update, context):
      
   Usuario2 =update.effective_user['username']
   
   print(Usuario2)

   Usuario_id = update.effective_user['id']
   
   Contextbot = context.bot
   

   if admins(Contextbot, Usuario_id) == True :  
      update.message.reply_text(f"@{Usuario2} El reenvío de multimedia a sido desactivado ")
      modo.append('desactivado')
      print(modo)
      return modo

# el comando /updates muestra el Historial de cambios de las actualizaciones del bot
def comandos(update, context):
      update.message.reply_text( f"""ESTOS SON LOS COMANDOS DEL BOT:\n\n\nCOMANDOS SOLO PARA ADMINS VETERANOS:\n\n/start (activa el reenvío de mensajes y archivos al canal)\n\n/stop (desactiva el reenvío de mensajes y archivos al canal)\n\n\nCOMANDOS PARA TODOS LOS ADMINS DEL GRUPO:\n\n/ignorar (este comando añade al usuario a la lista de ignorados para que no pueda reenviar archivos al canal)\n\nPara utilizarlo se puede responder a un usuario con\n/ignorar o puede pegar el id de usuario despues del comando (/ignorar 1715705674)\n\n/noignorar (quita al usuario de la lista de usuarios ignorados)\nse utiliza igual que el de arriba\n\n\nHASHTAGS DEL BOT \n\n{Hastag1} (sirve para reenviar archivos al canal) Se utiliza principalmente para enviar fotos o memes shiromi al canal\n\n{Hastag2} (sirve para enviar una sugerencia de contenido a los admins [intenta incluir el link de lo que deseas] )  """ )

def ignorar(update, context):
   print('yes')
  
   Usuario2 =update.effective_user['username']
   
   print(Usuario2)

   Usuario_id = update.effective_user['id']
   
   Contextbot = context.bot
   
   Args = context.args
   
   Reemplazar = str(Args).replace("['", "")
        
   El_baneado = Reemplazar.replace("']", "")

   if alladmins(Contextbot, Usuario_id) == True :  
      
      if Args:
        pass
      else:
        try:
          El_baneado = update.message.reply_to_message.from_user.id
        except:
          update.message.reply_text(f"@{Usuario2} escriba:\n/ign seguido del id del usuario o responda con /ing a un mensaje de la víctima ")
      if not ignore.__contains__(El_baneado):
          
       if not El_baneado == "[]":
         ignore.append(El_baneado)
         
         update.message.reply_text(f"@{Usuario2} El usuario {El_baneado} será ignorado ")
      else:
        update.message.reply_text(f"@{Usuario2} El usuario {El_baneado} ya estaba en la lista de usuarios ingorados")
   else:
     update.message.reply_text("Lo siento pero no eres admin de este grupo")
     
   print(ignore)
   return ignore
  
def console(update, context):
  
   Usuario2 =update.effective_user['username']
  
   print(f'\nUsado por: {Usuario2}')
  
   Usuario_id = update.effective_user['id']
   
   Contextbot = context.bot
   
   Args = context.args
   
   Reemplazar = str(Args).replace("['", "")
        
   El_comando = Reemplazar.replace("']", "")
   El_comando = El_comando.replace("', '", " ")
   print(El_comando, '\n')
   if admins(Contextbot, Usuario_id) == True :  
       try:
         comando = check_output(El_comando)
        
         comando = comando.decode()
        
         comando = str(comando)
         #comando = comando.replace("','", " ")
         #comando = comando.replace("'" , " ")
         print (comando)
         update.message.reply_text(str(comando))
       except:
          try:
            system(El_comando)
            respuesta = 'Ejecutado'
            update.message.reply_text(str(respuesta))
          except Exception as e:
	          print("ERROR : "+str(e))
         
         
     # except:
    #   update.message.reply_text(f"no pos F :( ")
      
      
def noignorar(update, context):
   print('no')
  
   Usuario2 =update.effective_user['username']
  
   print(Usuario2)
  
   Usuario_id = update.effective_user['id']
   
   Contextbot = context.bot
   
   Args = context.args
   
   Reemplazar = str(Args).replace("['", "")
        
   El_baneado = Reemplazar.replace("']", "")
   

   if admins(Contextbot, Usuario_id) == True :  
      
      
      if Args:
        pass
      else:
        try:
          El_baneado = update.message.reply_to_message.from_user.id
        except:
          update.message.reply_text(f"Lista de ignorados {ignore} ")
           
      if ignore.__contains__(El_baneado):
         ignore.remove(El_baneado)
         
         update.message.reply_text(f"@{Usuario2} El usuario {El_baneado} dejará de ser ignorado ")    
      else:
         if not El_baneado == "[]":
           update.message.reply_text(f"@{Usuario2} El usuario {El_baneado} no está en la lista de usuarios ingorados")
         
   
   else:
     update.message.reply_text("Lo siento pero no eres admin de este grupo")
     
     
   return ignore
   print(ignore)
  


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
     if Usuario2 == 'xXACRVXx' or Usuario2 == 'RathHunt' :  
       if str(Texto).startswith('-off'):
          update.message.reply_text(f"@{Usuario2} El reenvío de multimedia a sido desactivado ")
          dev_modo.append('off')
          print(modo)
          return modo
          
          update.message.reply_text(f"@{Usuario2} El reenvío de multimedia a sido activado ")
      
       if str(Texto).startswith('-on'):
         if modo.__contains__('off'):
          dev_modo.remove('off')
          return modo
          print(modo)
       
       if str(Texto).startswith('-modo'):
         
          update.message.reply_text(str(modo) + '\n' + str(dev_modo) )
       
       if str(Texto).startswith('-say'):
         
          Id_mensage_re = update.message.reply_to_message.message_id
          print(Id_mensage_re)
          update.message.reply_text(str(Texto.replace('-say','')), reply_to_message_id=Id_mensage_re )
     
       if str(Texto).startswith('-comand'):
         El_Comando = Texto.replace('-comand ','')
         print(El_Comando)
         
     # aqui es donde se permite o no el reenvío de archivos si la lista modo=[] no contiene '1'
     if not dev_modo.__contains__('off') :
         if not modo.__contains__('desactivado') :
           
           if not ignore.__contains__(Usuario_id):
             
             
             # si el usuario que utiliza el #shiromi no es Telegram se reenviar los archivos o el mensaje esto se utiliza para evitar que el bot caiga en bucle
             if not str(Usuario) == 'Telegram':
               
               if str(Subtitulos).__contains__(Hastag1):
                 
                 if not ignore.__contains__(Usuario_id):
                    Id_mensage = update.message.message_id
                    context.bot.forward_message(chat_id=Canal_hastag1 ,from_chat_id = Id_grupo , message_id= Id_mensage )
                 
                 else:
                    update.message.reply_text("No puedes usar el bot porque te encuentras en la lista de usuarios ignorados")
               
               if str(Texto).startswith(Hastag1):
                  
                 if not ignore.__contains__(Usuario_id):
                    Id_mensage_re = update.message.reply_to_message.message_id
                    
                    context.bot.forward_message(chat_id=Canal_hastag1 ,from_chat_id = Id_grupo , message_id= Id_mensage_re )
                    update.message.reply_text("Tu mensaje fue enviado")
                 
                 else:
                   update.message.reply_text("No puedes usar el bot porque te encuentras en la lista de usuarios ignorados")
                  
           else:
               update.message.reply_text("No puedes usar el bot porque te encuentras en la lista de usuarios ignorados")
         
         
         # en caso de estar desactivado el reenvío de el bot y se envie un mensaje que contenga #shiromi se enviara un mensaje como feedback al usuario para que sepa la razon por la cual no funcionó
         else:
           
            if not str(Usuario) == 'Telegram':
               
               if str(Subtitulos).__contains__(Hastag1):
                 
                update.message.reply_text("El reenvío fue desactivado")
         
               if str(Texto).startswith(Hastag1):
         
                update.message.reply_text("El reenvío fue desactivado")
     else:
           
            if not str(Usuario) == 'Telegram':
               
               if str(Subtitulos).__contains__(Hastag1):
                 
                update.message.reply_text(f'El {Hastag1} fue desactivado por los administradores, pero aún puedes usar el {Hastag2} :)')
         
               if str(Texto).startswith(Hastag1):
         
                update.message.reply_text(f'El {Hastag1} fue desactivado por los administradores, pero aún puedes usar el {Hastag2} :)')
     
     # si se envia el texto #deseo un grupo donde se encuentre el bot este reenviará el mensaje a el grupo establecido en chat_id='' y devolvera un mensaje de feedback  
     
     #if not dev_modo.__contains__('off') :
     if str(Texto).startswith(Hastag2):
          boton1 = InlineKeyboardButton(text= 'Boton (Mas Beta que el toDus)', callback_data= 'www')
          if update.message.reply_to_message.message_id:
            Texto = update.message.reply_to_message.text
          
          Eldeseo = f"Grupo:{str(Grupo).replace('None', 'privado' )}\nUsuario: {str(Usuario).replace('None','Anónimo')} @{str(Usuario2)}\nID: {Usuario_id}\n\nt.me/{update.message.chat.username}/{update.message.message_id}\n\n{str(Texto)}\n\n <code>Prueba de grupo: </code>{update.message.chat.title}"
                     
          
            
          
          context.bot.send_message(chat_id=Canal_hastag2,parse_mode="HTML", text=Eldeseo, reply_markup=InlineKeyboardMarkup([[boton1]]))
          
          update.message.reply_text("Tu deseo fue enviado")
      
def pruebabotones(update, context):
   Contextbot = context.bot
   Usuario_id = update.effective_user['id']
   if admins(Contextbot, Usuario_id) == True :  
      boton2 = InlineKeyboardButton(text= 'Prueba (Mas Beta que el toDus)', callback_data= 'xxx')
      
      elmensaje = update.callback_query
      
      el_deseo = elmensaje.message.text
      eluser = update.effective_user['username']
      elmensaje.answer()
      elmensaje.edit_message_text(text= str(el_deseo) + f'\n\n{eluser} Complacerá este deseo', reply_markup=InlineKeyboardMarkup([[boton2]]))
      
def pruebabotones2(update, context):
   Contextbot = context.bot
   Usuario_id = update.effective_user['id']
   if admins(Contextbot, Usuario_id) == True :  
      boton2 = InlineKeyboardButton(text= 'Prueba2 (Mas Beta que el toDus)', callback_data= 'xxx')
      
      elmensaje = update.callback_query
      
      el_deseo = elmensaje.message.text
      eluser = update.effective_user['username']
      elmensaje.answer()
      elmensaje.edit_message_text(text= str(el_deseo) + f'\n\n{eluser} Complacerá este deseo', reply_markup=InlineKeyboardMarkup([[boton2]]))
   

# aqui comienza la ejecución del bot   
if __name__ == "__main__":
  
    # el objeto shiromibot contiene el token de telegram obtenido de la variable TOKEN y otros datos 
    shiromibot = telegram.Bot(token=TOKEN)
 
    modo.append('desactivado')
 # actualizador contiene el objeto shiromibot y extrae el token de telegram mas use_context=True necesario para el funcionamiento de el bot
actualizador = Updater(shiromibot.token, use_context=True)
 
 # despachador normalmente nombrado dp extrae el dispatcher de el objeto actualizador      
despachador = actualizador.dispatcher

# aqui se definen los comandos a los que reacciona el bot
despachador.add_handler(CommandHandler('start', start))

despachador.add_handler(CommandHandler('stop', stop))

despachador.add_handler(CommandHandler('ignorar',ignorar))

despachador.add_handler(CommandHandler('console',console))

despachador.add_handler(CommandHandler('noignorar',noignorar))

despachador.add_handler(CommandHandler('comandos', comandos))

despachador.add_handler(MessageHandler(filters=Filters.all, callback= mensajes_entrantes))

despachador.add_handler(CallbackQueryHandler(pattern='www', callback=pruebabotones))

despachador.add_handler(CallbackQueryHandler(pattern='xxx', callback=pruebabotones2))

   
print('######################################################################\n\n')

try:
  Logopython.logopy()
except:
  print('Este bot forma parte de el repositorio de GitHub https://github.com/xXACRVXx/BotDePruebas bajo licencia MIT')

print('\n\n                      ############################')
print('                                INICIADO      ')
print('                      ############################\n')
#print('LOG:     ')
actualizador.start_polling()
  
actualizador.idle   
