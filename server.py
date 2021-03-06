#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cherrypy
import telebot
from requests_to_the_router import mac_filter_off, mac_filter_on,\
    mac_filter_on_for_all, mac_filter_on_for_homedevice
from config import token
from telebot import types



bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def command_start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('вкл wi-fi всем')
    itembtn2 = types.KeyboardButton('выкл wi-fi всем')
    itembtn3 = types.KeyboardButton('выключить wi-fi ребёнку')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Привет! Я бот - сисадмин", reply_markup=markup)

@bot.message_handler(regexp=r"вкл wi-fi всем")
def on(message):
    mac_filter_off()
    bot.send_message(message.chat.id, "wi-fi доступен всем устройствам")
    print('on')

@bot.message_handler(regexp=r"выкл wi-fi всем")
def off(message):
    mac_filter_on_for_all()
    bot.send_message(message.chat.id, "wi-fi не доступен всем устройствам")
    print('off')
    

@bot.message_handler(regexp=r"выключить wi-fi ребёнку")
def child(message):
    mac_filter_on()
    bot.send_message(message.chat.id, "wi-fi не доступен для телефона ребёнка")
    print('child')

@bot.message_handler(commands=["devices"])
def devices(message):
    mac_filter_on_for_homedevice()
    bot.send_message(message.chat.id, "off devices")
    print('devices')

@bot.message_handler(commands=["on_devices"])
def on_devices(message):
    mac_filter_on()
    bot.send_message(message.chat.id, "on devices")
    print('ON devices')

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




if __name__ == '__main__':

    cherrypy.config.update({
        'server.socket_host': '10.8.0.10',
        'server.socket_port': 888,
        'engine.autoreload.on': False
    })
    cherrypy.quickstart(WebhookServer())
