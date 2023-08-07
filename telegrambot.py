#!/usr/bin/env python3.8
from telegram.ext import Updater, CommandHandler
import logging
from glob import glob
import os
import subprocess
from time import sleep
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Telegram bot token from the environment variable
telegram_token = os.getenv('TELEGRAM_TOKEN')
admin_chat_ids = os.getenv('ADMIN_CHAT_IDS')

# Check if the token is provided in the .env file
if telegram_token is None:
    raise ValueError("TELEGRAM_TOKEN not found in the .env file.")
if admin_chat_ids is None:
    raise ValueError("ADMIN_CHAT_IDS not found in the .env file.")

admin_chat_ids = [int(chat_id.strip()) for chat_id in admin_chat_ids.split(',')]


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(telegram_token, use_context=False)

def create_method(bot,update,args):
        sender_chat_id = update.message.chat.id
        if sender_chat_id in admin_chat_ids:
          client_ocserv = str(args[0])
          proc = subprocess.Popen(['./user_add.sh',client_ocserv],stdout=subprocess.PIPE)
          bot.sendMessage(update.message.chat.id,"wait for certificate file to be created...")
          sleep(1)
          newpath = glob('/var/www/html/'+client_ocserv+'*')
          for f in newpath:
            fbasenam=os.path.basename(f)
            bot.send_document(update.message.chat.id, document=open(f, 'rb'))
        else:
          bot.sendMessage(update.message.chat.id,"Unauthorized")

def get_method(bot,update,args):
        sender_chat_id = update.message.chat.id
        if sender_chat_id in admin_chat_ids:
          client_ocserv = str(args[0])
          newpath = glob('/var/www/html/'+client_ocserv+'*')
          for f in newpath:
            bot.send_document(update.message.chat.id, document=open(f, 'rb'))
        else:
          bot.sendMessage(update.message.chat.id,"Unauthorized")

def revoke_method(bot,update,args):
        sender_chat_id = update.message.chat.id
        if sender_chat_id in admin_chat_ids:
          client_ocserv = str(args[0])
          proc = subprocess.Popen(['./user_del.sh',client_ocserv],stdout=subprocess.PIPE)
          bot.sendMessage(update.message.chat.id,"The user certificate has been revoked.")
        else:
          bot.sendMessage(update.message.chat.id,"Unauthorized")

def online_method(bot,update,args):
        sender_chat_id = update.message.chat.id
        if sender_chat_id in admin_chat_ids:
          x = subprocess.check_output(['./show_online_users.sh'],shell=True)
          bot.sendMessage(update.message.chat.id,x.decode("utf-8"))
        else:
          bot.sendMessage(update.message.chat.id,"Unauthorized")

def disconnect_method(bot,update,args):
        sender_chat_id = update.message.chat.id
        if sender_chat_id in admin_chat_ids:
          user_name = str(args[0])
          proc = subprocess.Popen(['./disconnect_user.sh',user_name],stdout=subprocess.PIPE)
          bot.sendMessage(update.message.chat.id,"User successfully disconnected.")
        else:
          bot.sendMessage(update.message.chat.id,"Unauthorized")

def status_method(bot,update,args):
        sender_chat_id = update.message.chat.id
        if sender_chat_id in admin_chat_ids:
          x = subprocess.check_output(['./mon.sh'],shell=True)
          bot.sendMessage(update.message.chat.id,x.decode("utf-8"))
        else:
          bot.sendMessage(update.message.chat.id,"Unauthorized")

######################################################################################################

create_command = CommandHandler('create',create_method,pass_args=True)
updater.dispatcher.add_handler(create_command)

get_command = CommandHandler('get',get_method,pass_args=True)
updater.dispatcher.add_handler(get_command)

revoke_command = CommandHandler('revoke',revoke_method,pass_args=True)
updater.dispatcher.add_handler(revoke_command)

online_command = CommandHandler('online',online_method,pass_args=True)
updater.dispatcher.add_handler(online_command)

disconnect_command = CommandHandler('disconnect',disconnect_method,pass_args=True)
updater.dispatcher.add_handler(disconnect_command)

status_command = CommandHandler('status',status_method,pass_args=True)
updater.dispatcher.add_handler(status_command)

######################################################################################################

updater.start_polling()
updater.idle()


