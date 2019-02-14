from pickings import *
from aeon import *
from ald import *
import lxml
import os
import random
from telegram.ext import Updater, Dispatcher, CommandHandler
import requests
import telepot
from bs4 import BeautifulSoup
import urllib.request

YOUR_TOKEN = '686403591:AAGsQLfGe2ffNFdsD37rPCwtdKq5iMdfq4c'
WELCOME = 'Welcome! I am PhilDailyBot, here to give you your dose of philosophy, life, love and everything else in between! Type /brainpickings for an article from Brain Pickings, /aeon for an article from Aeon and /ald for an article from Arts and Letters Daily.'


def brain_pickings(bot,update):
    final_reply = pickings.get_pickings()
    bot.send_message(chat_id=update.message.chat_id,text=final_reply)
    

def my_start(bot,update):
    final_reply = WELCOME
    bot.send_message(chat_id=update.message.chat_id,text=final_reply)
    

def aeonco(bot,update):
    final_reply = aeon.get_aeon()
    bot.send_message(chat_id=update.message.chat_id,text=final_reply)
    

def aldaily(bot,update):
    final_reply =ald.get_ald()
    bot.send_message(chat_id=update.message.chat_id,text=final_reply)
    
    

#mybot = telepot.Bot()

updater = Updater(token=YOUR_TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', my_start))
dispatcher.add_handler(CommandHandler('brainpickings', brain_pickings))
dispatcher.add_handler(CommandHandler('aeon', aeonco))
dispatcher.add_handler(CommandHandler('ald', aldaily))

updater.start_polling()
print('it is happening!')
updater.idle()
print('it is idle!')
