#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cherrypy
import telebot
from requests_to_the_router import mac_filter_off, mac_filter_on,\
    mac_filter_on_for_all, mac_filter_on_for_homedevice
from config import token



bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def command_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот - сисадмин")

@bot.message_handler(commands=["on_all"])
def on(message):
    bot.send_message(message.chat.id, "on all")
    print('on')
    mac_filter_off()

@bot.message_handler(commands=["off_all"])
def off(message):
    bot.send_message(message.chat.id, "off all")
    print('off')
    mac_filter_on_for_all()
    

@bot.message_handler(commands=["child"])
def child(message):
    bot.send_message(message.chat.id, "off child")
    print('child')
    mac_filter_on()

@bot.message_handler(commands=["devices"])
def devices(message):
    bot.send_message(message.chat.id, "off devices")
    print('devices')
    mac_filter_on_for_homedevice() 

@bot.message_handler(commands=["on_devices"])
def on_devices(message):
    bot.send_message(message.chat.id, "on devices")
    print('ON devices')
    mac_filter_on()

class WebhookServer(object):
    # index равнозначно /, т.к. отсутствию части после ip-адреса (грубо говоря)
    @cherrypy.expose
    def index(self):
        length = int(cherrypy.request.headers['content-length'])
        json_string = cherrypy.request.body.read(length).decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        print('index')
        bot.process_new_updates([update])
        return ''


'''class Server_Handler(object):
    @cherrypy.expose
    def index(self): # on all
        print('on')
        mac_filter_off()
        return ""

    @cherrypy.expose
    def off(self): # off all
        print('off')
        mac_filter_on_for_all()
        return ''

    @cherrypy.expose
    def child(self): # off child
        print('child')
        mac_filter_on()
        return ''
    
    @cherrypy.expose
    def devices(self): # off devices
        print('devices')
        mac_filter_on_for_homedevice()
        return ''
'''

if __name__ == '__main__':

    cherrypy.config.update({
        'server.socket_host': '10.8.0.10',
        'server.socket_port': 888,
        'engine.autoreload.on': False
    })
    cherrypy.quickstart(WebhookServer())
