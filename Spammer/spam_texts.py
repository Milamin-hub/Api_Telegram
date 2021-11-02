from telethon.sync import TelegramClient

import time
import random

api_id = '1'
api_hash = '5'
amount_acc = 10

group_list = open('Folder_txt\\group_list.txt', 'r').read().split()
count_group = len(group_list)

def Spam():
    i = 0
    while i < amount_acc:

        account = f'account{i}'
        print(account)

        client = TelegramClient(account, api_id, api_hash)

        client.connect()

        if not client.is_user_authorized():
            print('account skip')
        else:
            v = 0
            for group in group_list:
                if v < count_group:
                    if v == count_group - 1:
                        v = 0
                    else:
                        texts = open(file=f'txt_Massages\\text{v}.txt', mode='r', encoding='utf-8')
                        text = (texts.read())
                        try:
                            client.send_message(group, text)
                            print(f'done send massage: {group}, {text}')
                            v += 1
                        except Exception as e:
                            print(e)

        client.disconnect()

        i += 1

        time.sleep(random.randint(120, 240))


Spam()
