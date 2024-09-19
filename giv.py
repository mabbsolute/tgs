import requests
import pandas as pd
from licensing.models import *
from licensing.methods import Key, Helpers

# GitHub repository URL
url = "https://raw.githubusercontent.com/mabbsolute/tgs/main/givesharekod.csv"

# URL dan CSV faylni yuklab olish
response = requests.get(url)

# Ma'lumotlarni qatorlarga ajratish
lines = response.text.splitlines()

# Olingan qatorlarni tozalash
cleaned_lines = [line.strip() for line in lines]

# Ma'lumotlarni DataFrame'ga yuklash
data = pd.DataFrame(cleaned_lines, columns=['Hash Values'])

# Ma'lumotlarni ro'yxatga aylantirmoqchi bo'lsangiz
hash_values_list = data['Hash Values'].tolist()

def GetMachineCode():
    machine_code = Helpers.GetMachineCode(v=2)
    return machine_code

machine_code = GetMachineCode()

# Mashina kodini tekshirish
if machine_code in hash_values_list: 
    print("Tabriklayman")
    print("Yaratuvchi @Enshteyn40")
    from telethon.sync import TelegramClient
    from licensing.models import *
    from licensing.methods import Key, Helpers
    from telethon.sync import TelegramClient
    
    import ssl
    import csv
    import psutil
    import asyncio
    from urllib.parse import unquote
    from telethon.tl.functions.messages import ImportChatInviteRequest
    import cloudscraper
    from fake_useragent import FakeUserAgent
    import time
    import webbrowser
    from telethon import types, utils, errors
    from telethon.tl.functions.messages import RequestAppWebViewRequest
    from telethon.tl.types import InputBotAppShortName, InputUser
    from telethon.sync import TelegramClient
    from telethon.tl.functions.channels import LeaveChannelRequest, JoinChannelRequest
    from telethon.tl.functions.account import UpdateStatusRequest

    def terminate_chrome_processes():
        for proc in psutil.process_iter():
            if proc.name().lower() == "chrome.exe":
                proc.terminate()

    phonecsv = "phone"
    with open(f'{phonecsv}.csv', 'r') as f:
        global phlist
        phlist = [row[0] for row in csv.reader(f)]
    print('Jami Nomerlar: ' + str(len(phlist)))
    qowiwjm = 0
    qowiwjm2 = int(str(len(phlist)))
    channels = []
    channels1 = []
    with open(r"C:\join\gividgiv.csv", 'r') as f:
        giv_ids = [row[0] for row in csv.reader(f)]
    with open(r"C:\join\ochiqkanalgivshare.csv", 'r') as f:
        premium_channels = [row[0] for row in csv.reader(f)]
    with open(r"C:\join\yopiqkanalgivshare.csv", 'r') as f:
        yopi_channels = [row[0] for row in csv.reader(f)] 
    with open(r"C:\join\givesharetime.csv", 'r') as f:
        reader = csv.reader(f)
        first_row = next(reader)
        if first_row:
            timee = first_row[0]
            print(f"Kutish vaqti: {timee}")
    indexx = 0
    for deltaxd in phlist[qowiwjm:qowiwjm2]:
        try:
            indexx += 1
            phone = utils.parse_phone(deltaxd)
            print(f"Login {phone}")
            api_id = 22962676
            api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'
            client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
            client.start(phone)
            client(UpdateStatusRequest(offline=False))
            print(f'Index : {indexx}')
            async def main():
                try:
                    for channel_link in premium_channels:
                        try:
                            await client(JoinChannelRequest(channel_link))
                        except Exception as e:
                            print(f"Xatolik:  {e}")
                        try:
                            await client(JoinChannelRequest(channel_link))
                        except Exception as e:
                            print(f"Xatolik:  {e}")  
                    for yopiq_link in yopi_channels:
                        try:
                            await client(ImportChatInviteRequest(yopiq_link)) 
                        except Exception as e:
                            print(f"Xatolik: {e}")                
                except Exception as e:
                    print(f"Failed to join: {e}")    
                for give_id in giv_ids:
                    bot_entity = await client.get_entity("GiveShareBot")
                    bot = InputUser(user_id=bot_entity.id, access_hash=bot_entity.access_hash)
                    bot_app = InputBotAppShortName(bot_id=bot, short_name="app")
                    print(bot_app)
                    start_param = give_id
                    web_view = await client(
                        RequestAppWebViewRequest(
                            peer=bot,
                            app=bot_app,
                            platform="android",
                            write_allowed=True,
                            start_param=start_param
                        )
                    )
                    auth_url = web_view.url
                    tg_web_data = unquote(
                        string=auth_url.split('tgWebAppData=', maxsplit=1)[1].split('&tgWebAppVersion', maxsplit=1)[0])
                    #print(tg_web_data)
                    webbrowser.open(auth_url)
                    time.sleep(timee)  # Yuklanishni kutish
                    print("URL ochildi va kutish rejimida")
                terminate_chrome_processes()
                
                time.sleep(5)
            with client:
                client.loop.run_until_complete(main())
        except Exception as e:
            print("error:  ", e)
            continue
    else:
        print("@Enshteyn40 ga murojat qiling")    
