import struct
import asyncio
import hashlib
from licensing.models import *
from licensing.methods import Key, Helpers
from telethon import utils, functions, types
import traceback
from urllib.parse import unquote
import csv
from fake_useragent import UserAgent
from telethon.sync import TelegramClient
import random
from telethon.tl.functions.channels import JoinChannelRequest
ovoz_berildi = []
qayta_ovoz = []
ovoz_berilamadi = []
premium_channels = []
num_channels = int(input("Qancha kanalga a'zo bo'lishni xohlaysiz? "))
for i in range(num_channels):
    channel_link = input(f'Kanal linkini kiriting #{i + 1:}: ')
    premium_channels.append(channel_link)

def get_visitor_id():
    ua = UserAgent()
    user_agent = ua.random
    screen_resolution = "1920x1080"
    language = "en-US"

    device_data = f"{user_agent}-{screen_resolution}-{language}"
    visitor_id = hashlib.md5(device_data.encode()).hexdigest()
    return visitor_id

phonecsv = "phone"
with open(f'{phonecsv}.csv', 'r') as f:
    phlist = [row[0] for row in csv.reader(f)]
print('Jami Nomerlar: ' + str(len(phlist)))
startkim = str(input("Qaysi vote masalan( /start 232): "))
yondan = int(input("Nechinchi knopkani bosish kerak: "))
qanchakutish = int(input("Qancha oraliq kutish kerak: "))


async def main():
    indexx = 0
    for phone in phlist:
        api_id = 22962676
        api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'
        phone = utils.parse_phone(phone)
        indexx += 1
        print(f'Index : {indexx}')
        tg_client = TelegramClient(f'sessions/{phone}', api_id, api_hash)
        try:
            await tg_client.connect()
            print(indexx)
            if not await tg_client.is_user_authorized():
                print('Sessiyasi yoq raqam ')
            else:
                async with tg_client:
                    for ochiq_link in premium_channels:
                        try:
                            await tg_client(JoinChannelRequest(ochiq_link)) 
                            print((f" Kanalga a'zo bo'ldi {ochiq_link}"))
                        except Exception as e:
                            print((f"Kanalga qo'shilishda xatolik {ochiq_link}"))  
                    username = await tg_client.get_entity("namanganlivebot")
                    await tg_client.send_message(username, startkim)
                    await asyncio.sleep(qanchakutish)
                    m = await tg_client.get_messages(username, limit=1)
                    try:
                        await m[0].click(yondan - 1)
                    except Exception:
                        print("Knopkaga bosishda xatolik yuz berdi.")

                    await asyncio.sleep(qanchakutish)

                    visitor_id = get_visitor_id()

                    button_text = "Овоз беришни тасдиқлаш"
                    result = await tg_client(functions.messages.SendWebViewDataRequest(
                        bot=username,
                        random_id=random.randint(0, 2**63 - 1),
                        button_text=button_text,
                        data=visitor_id
                    ))

                    await asyncio.sleep(0.3)
                    import time
                    
                    time.sleep(qanchakutish)

                    max = await tg_client.get_messages(username, limit=1)
                    if any("✅ Сизнинг" in message.text for message in max[:2]):
                        ovoz_berildi.append(len(ovoz_berildi))
                    elif any("❗️Сизнинг" in message.text for message in max[:2]):
                        qayta_ovoz.append(len(qayta_ovoz))
                    else:
                        ovoz_berilamadi.append(len(ovoz_berilamadi))
                    s1 = len(ovoz_berildi)
                    s2 = len(qayta_ovoz)
                    s3 = len(ovoz_berilamadi)
                    print(max[0].text)
                    print(f"\n{s1} -   ovoz berildi \n{s2} -   qayta ovoz \n{s3} -   ovoz berilmadi")
        except Exception as e:
            traceback.print_exc()
            print(f"Telefon: {phone} ishlamadi. Xato: {e}")
if __name__ == '__main__':
    asyncio.run(main())
