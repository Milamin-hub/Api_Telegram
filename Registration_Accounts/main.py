# -*- coding: utf-8 -*-QS
import os
from telethon.sync import TelegramClient

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
wh="\033[0m"
wi="\033[0;35m"
yl="\033[33m"
os.system('cls')


def log():
    
    api_id=input(f"{yl}Enter ur api id:{wh}")

    api_hash=input(f"{yl}Enter ur api_hash:{wh}")

    phone=input(f"{yl}Enter ur phone:{wh}")

    print(f"{yl}data: {wh}",api_id, api_hash, phone)

    client = TelegramClient(phone, api_id, api_hash)
    client.connect()

    if not client.is_user_authorized():

        print(f"{cy}w8 for code{wh}")

        client.send_code_request(phone)

        me = client.sign_in(phone, input(f"{yl}Enter code: {wh}"))

    print(f"{gr}session created{wh}")
    client.edit_2fa(new_password='wqemgv49815')

    print(f"{gr}2fa enabled{wh}")
    client.disconnect()


while True:
    log()