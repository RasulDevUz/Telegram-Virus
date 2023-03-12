from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from PIL import Image, ImageDraw, ImageFont
import time
client = TelegramClient(StringSession(),
                        api_id="22350870", api_hash="0f665ebc5b49b033663ad56d9bf92dff")
client.start()
time1 = ''
time2 = ''

def tick():
    global time1
    global time2
    time2 = time.strftime('%H:%M')
    if time2 != time1:
        time1 = time2
    else:
        return "NO"
    Time_teletips = time.strftime("%I:%M %p")
    Image_teletips = Image.open("image.jpg")
    Image_text_teletips = f"{Time_teletips}"
    Image_font_teletips = ImageFont.truetype("ds-digit.ttf", 360)
    Image_edit_teletips = ImageDraw.Draw(Image_teletips)
    Image_edit_teletips.text((690, 550), Image_text_teletips, (0, 255, 255), font = Image_font_teletips)
    Image_teletips.save("photo.jpg")


while True:
    t = tick()
    if t != "NO":
        client(DeletePhotosRequest(client.get_profile_photos('me')))

        result = client(UploadProfilePhotoRequest(
            file=client.upload_file('photo.jpg')
        ))

