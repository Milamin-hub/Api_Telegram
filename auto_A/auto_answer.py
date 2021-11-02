from telethon.sync import TelegramClient
from telethon import utils
from telethon.tl.functions.messages import GetPeerDialogsRequest
import time
import random

api_id = '1'
api_hash = '5'
amount_session = 10
group = '...'

user_input = open('user_id.txt', 'a')


def Auto_answer():
    i = 0
    while i < amount_session:

        account = f'account{i}'
        print(account)

        client = TelegramClient(account, api_id, api_hash)

        client.connect()

        if not client.is_user_authorized():
            print('account skip')
        else:
            users = set()
            for dialog in client.iter_dialogs():
                try:
                    if dialog.is_user and dialog.id != 777000:
                        users.add(dialog)
                except:
                    print(e)
            for user in users:
                try:
                    user_id = utils.get_peer_id(user.id)
                    result = client(GetPeerDialogsRequest(
                        peers=[user_id]
                    ))
                    message_count = result.dialogs[0].unread_count
                except Exception as e:
                    print(e)
                print(user.title)
                print(message_count)
                if message_count == 0:
                    print(f'delete: {user_id}')
                    try:
                        client.delete_dialog(user_id)
                    except Exception as e:
                        print(e)
                    print('new massages: 0')
                elif message_count != 0:
                    try:
                        user.message.mark_read()
                        client.send_message(user_id, group)
                    except Exception as e:
                        print(e)
                    print(f'have massage: {user.entity.username}')
                    user_input.write(f'\n+ {user.entity.username}')

        client.disconnect()
        
        i += 1


Auto_answer()
