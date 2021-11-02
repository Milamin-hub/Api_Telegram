from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import time
import random

api_id = '1'
api_hash = '5'
amount_account = 10

group_list = open('Folder_txt\\group_list.txt', 'r').read().split()


def acc_join():
    i = 0
    while i < amount_account:

        account = f'account{i}'
        print(account)

        client = TelegramClient(account, api_id, api_hash)

        client.connect()

        if not client.is_user_authorized():
            print('account skip')
        else:
            for group in group_list:
                try:
                    client(JoinChannelRequest(group))
                    print(group)
                    time.sleep(random.randint(60, 120))
                except Exception as e:
                    print(e)

        client.disconnect()

        i += 1

        time.sleep(random.randint(60, 120))


acc_join()

