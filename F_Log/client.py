from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.photos import DeletePhotosRequest
from telethon import functions
import time
import spintax


api_id = '1'
api_hash = '5'
last_name = ''
name_user = ''
amount_session = 10


def main():
    acc = 1
    while True:
        account = f'account{acc}'
        print(account)

        client = TelegramClient(account, api_id, api_hash)

        client.connect()

        if acc > amount_session:
            break
        elif not client.is_user_authorized():
            print('account skip')
        else:
            try:
                client(UpdateUsernameRequest(name_user))
                print(name_user)
            except Exception as e:
                print(e)

            try:
                names = open(file='Folder_txt\\names.txt', mode='r', encoding='UTF-8').readlines()[0]
                first_name = spintax.spin(names)
                client(functions.account.UpdateProfileRequest(
                    first_name=first_name,
                    last_name=last_name,
                ))
                print(first_name, last_name)
                print('+name')
                print('-last_name')
            except Exception as e:
                print(e)

            try:
                client(DeletePhotosRequest(
                    client.get_profile_photos('me')
                ))
                print('delete photo')
                client(UploadProfilePhotoRequest(
                    client.upload_file(f'Photos\\{acc}.jpg')
                ))
                print('upload photo')
            except Exception as e:
                client(UploadProfilePhotoRequest(
                    client.upload_file(f'Photos\\{acc}.jpg')
                ))
                print('upload photo')
                print(e)


        client.disconnect()

        acc += 1

        time.sleep(3)


main()
