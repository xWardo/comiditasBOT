from telegram.ext import Updater #Importas las librerias
updater = Updater(token='489218394:AAHc1__5vd2hiKBLNFGExNuhRuvD4Voi0mU') #Creas el updater para mantener el bot siempre activo
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode #librerias para cambiar el teclado
dispatcher = updater.dispatcher #Para que el updater acceda mas rapido al dispatcher
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters


#Esto crea un registro en la consola para saber si falla algo pues que diga que es lo que falla
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

#Para el comando start
def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Hola! estas usando a ComiditasBOT. el bot que te informa de que comiditas son las que tenemos que hacer. \npara recibir ayuda escribre /help",
        reply_markup=keyboard_cmds()) #Llama a la funcion que construye el teclado

#Contruye el teclado con los comandos que yo le diga
def keyboard_cmds():
    command_buttons = [
        KeyboardButton("/help"),
        KeyboardButton("/comiditas"),
        KeyboardButton("/comiditas_hechas"),
        KeyboardButton("/comiditas_por_hacer"),
        KeyboardButton("pole"),
        KeyboardButton("/Comiditas favoritas"),
        KeyboardButton("/donaciones"),
        KeyboardButton("/start"),
    ]
#Devuelve el telcado con 3 columnas y llamando a la funcion build que organiza el telcado
    return ReplyKeyboardMarkup(build_menu(command_buttons, n_cols=3))

def build_menu(buttons, n_cols=1, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]

    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)

    return menu

start_handler = CommandHandler('start', start) #Haces que con el comando /start se inicie la funcion start
dispatcher.add_handler(start_handler) #Lo añades al dispatcher

#Para que repita los mensajes
def pole(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Menuda poleada te has marcado maquina")

pole_handler = MessageHandler('pole', pole)
dispatcher.add_handler(pole_handler)

def ayuda(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Comandos del bot:\n\n/ \n\n \n\n \n  \n  \n ")
    
help_handler = CommandHandler('help', ayuda)
ayuda_handler = CommandHandler('ayuda', ayuda)
dispatcher.add_handler(ayuda_handler)
dispatcher.add_handler(help_handler)

def comiditas(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="COMIDITAS EN TOTAL\n\nKebab del centro\n\nCasa del cereal\n\nKebab de benimaclet\n\nTGB\n\nTaco BELL\n\nSubway\n\nLemon Grass\n\nPor favor, para contribuir con nuestra lista de comiditas, mandanos tu petición al Drive compatido, la lista será actualizada a su debido tiempo! Gracias por su colaboración :)")

comiditas_handler = CommandHandler('comiditas', comiditas)
dispatcher.add_handler(comiditas_handler)

def donaciones(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Dona a este bot para seguir manteniendo los servidores y ayudar al creador!\npaypal.me/memestroika")

def nuria(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="")



def capitulito(bot, update):
     contador = 0
     while (contador < 120):
         bot.send_message(chat_id=update.message.chat_id, text="http://www.animeyt.tv/ver/shokugeki-no-souma-san-no-sara-10-sub-espanol")
         contador = contador+1




#updater = Updater("458849790:AAG9dLDx5f_jNlA8NjnJl_-gTvmW2nN8nh4")
#dp = updater.dispatcher

def stop_and_restart():
    """Gracefully stop the Updater and replace the current process with a new one"""
    updater.stop()
    os.execl(sys.executable, sys.executable, *sys.argv)

def restart(bot, update):
    update.message.reply_text('Bot is restarting...')
    Thread(target=stop_and_restart).start()


dispatcher.add_handler(CommandHandler('restart', restart, filters=Filters.user(username='@xWardo')))

#Si ponen un comando que no está registrado
def unknown(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Lo siento, no entiendo ese comando! asegurate de escribirlo bien. /help para ver los comandos disponibles.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)





updater.start_polling() #Para empexar el bot
