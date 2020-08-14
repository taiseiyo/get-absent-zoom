#!/usr/bin/env python3
from PIL import Image
import pyocr
import pyocr.builders
from rocketchat_API.rocketchat import RocketChat
import getpass

password = getpass.getpass()
user = "***"
name_list = ["***"]
rocket = RocketChat(user, password, server_url='***')


def read_name():
    tools = pyocr.get_available_tools()
    tool = tools[0]  # tesseract
    langs = tool.get_available_languages()
    lang = langs[0]  # english

    txt = tool.image_to_string(
        Image.open('./photo.png'),
        lang=lang,
        builder=pyocr.builders.TextBuilder())

    return txt.lower()


def trimming():
    pic = Image.open('./name.png')
    pic.crop((50, 20, 1000, 700)).save('./photo.png', quality=100)


def make_message(pic_name):
    message = ["欠席者"]
    for name in name_list:
        if(name not in pic_name):
            message.append(name)
    message = "\n".join(message)
    return message


def rocket_chat_tools(message):
    rocket.chat_post_message(message, channel="***").json()


def main():
    trimming()
    pic_name = read_name()
    message = make_message(pic_name)
    rocket_chat_tools(message)


main()
