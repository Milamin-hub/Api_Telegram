from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest
import random
import time

api_id = '1'
api_hash = '5'
group = '@...'
users = open('Folder_txt\\names.txt', mode='+r', encoding='UTF-8').read().split()
amount_session = 10


def delay():
    time.sleep(random.randint(60, 120))


def invite_group():
    acc = 1
    while acc < amount_session:

        account = f'account{acc}'

        client = TelegramClient(account, api_id, api_hash)

        client.connect()

        print(f'{acc}')

        if not client.is_user_authorized():
            print('account skip')
        else:
            try:
                client(JoinChannelRequest(group))
            except Exception as e:
                print(e)

            for user in users:
                try:
                    client(InviteToChannelRequest(group, [user]))
                    print(f'invite_channel: {user}')
                    name_users = open('Folder_txt/done_ivite.txt', mode='a', encoding='UTF-8')
                    name_users.write(f'\n{user}')
                    delay()
                except Exception as j:
                    print(j)
                    delay()

        client.disconnect()

        acc += 1

        delay()


invite_group()
