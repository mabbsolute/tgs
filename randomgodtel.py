import requests
import pandas as pd
from licensing.models import *
from licensing.methods import Key, Helpers
import subprocess
# GitHub repository URL
url = "https://raw.githubusercontent.com/mabbsolute/tgs/refs/heads/main/randomize.csv"

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

print(machine_code) 

print(f"DEVICE ID: {machine_code}")

# Mashina kodini tekshirish
if machine_code in hash_values_list: 
    import base64
    import asyncio
    from urllib.parse import unquote
    from telethon.tl.functions.messages import ImportChatInviteRequest
    import aiohttp
    import aiohttp_proxy
    import fake_useragent
    from telethon import TelegramClient
    from telethon.tl.functions.channels import JoinChannelRequest
    from telethon.tl.types import InputUser, InputBotAppShortName
    from telethon.tl.functions.messages import RequestAppWebViewRequest
    import csv
    from termcolor import colored

    with open(r"/storage/emulated/0/giv/proxy.csv", 'r') as f: 
        reader = csv.reader(f)
        ROTATED_PROXY = next(reader)[0]

    # Load givs from randogiv.csv
    givs = []
    with open(r"/storage/emulated/0/giv/rangiv.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            givs.append(row[0])
    with open(r"/storage/emulated/0/giv/ranochiqkanal.csv", 'r') as f:
        premium_channels = [row[0] for row in csv.reader(f)]
        
    with open(r"/storage/emulated/0/giv/ranyopiqkanal.csv", 'r') as f:
        yopiq_channels = [row[0] for row in csv.reader(f)]

    channels = premium_channels + yopiq_channels
    async def run(phone, start_params, channels):
        api_id = 22962676
        api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'

        tg_client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
        await tg_client.connect()
        if not await tg_client.is_user_authorized():
            print('Sessiyasi yoq raqam ')
        else:
            async with tg_client:
                me = await tg_client.get_me()
                name = me.username or me.first_name + (me.last_name or '')

                bot_entity = await tg_client.get_entity("@RandomGodBot")
                bot = InputUser(user_id=bot_entity.id, access_hash=bot_entity.access_hash)
                bot_app = InputBotAppShortName(bot_id=bot, short_name="JoinLot")

                for start_param in start_params:
                    web_view = await tg_client(
                        RequestAppWebViewRequest(
                            peer=bot,
                            app=bot_app,
                            platform="android",
                            write_allowed=True,
                            start_param=start_param
                        )
                    )

                    init_data = unquote(web_view.url.split('tgWebAppData=', 1)[1].split('&tgWebAppVersion')[0])
                    
                    for yopiq_link in yopiq_channels:
                        try:
                            await tg_client(ImportChatInviteRequest(yopiq_link)) 
                            print(colored(f"{name} | Kanalga a'zo bo'ldi {yopiq_link}", "green"))
                        except Exception as e:
                            print(colored(f"{name} | Kanalga qo'shilishda xatolik {yopiq_link}: {e}", "red")) 
                    for ochiq_link in premium_channels:
                        try:
                            await tg_client(JoinChannelRequest(ochiq_link)) 
                            print(colored(f"{name} | Kanalga a'zo bo'ldi {ochiq_link}", "green"))
                        except Exception as e:
                            print(colored(f"{name} | Kanalga qo'shilishda xatolik {ochiq_link}: {e}", "red"))            
                    headers = {
                        'accept': '*/*',
                        'accept-language': 'ru-RU,ru;q=0.5',
                        'cache-control': 'no-cache',
                        'dnt': '1',
                        'pragma': 'no-cache',
                        'priority': 'u=1, i',
                        'referer': f'https://randomgodbot.com/api/lottery/snow/main.html?tgWebAppStartParam={start_param}',
                        'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'sec-gpc': '1',
                        'user-agent': fake_useragent.UserAgent().random,
                        'x-requested-with': 'XMLHttpRequest',
                    }

                    proxy_conn = aiohttp_proxy.ProxyConnector().from_url(ROTATED_PROXY) if ROTATED_PROXY else None
                    async with aiohttp.ClientSession(headers=headers, connector=proxy_conn) as http_client:
                        try:
                            encoded_init_data = base64.b64encode(init_data.encode()).decode()
                            url = f"https://95.217.212.109/lot_join?userId={me.id}&startParam={start_param}&id={encoded_init_data}"
                            response = await http_client.get(url=url, ssl=False)
                            response.raise_for_status()

                            response_json = await response.json()
                            if response_json.get('ok') and response_json.get('result') == 'success':
                                print(colored(f"{name} | Giv uchun muvaffaqiyatli qo'shildi:", "green"))
                            else:
                                print(colored(f"{name} | Giv uchun qo'shilish muvaffaqiyatsiz yoki givda allaqachon qatnashib bo'lgan: {response_json}", "red"))

                        except Exception as err:
                            print(colored(f"{name} | Giv so'rov yuborishda xatolik: {err}", "yellow"))

    async def main():
        try:
            with open('phone.csv', 'r') as file:
                phones = [line.strip() for line in file if line.strip()]
        except Exception as e:
            print(f"Telefon raqamlarini yuklashda xatolik: {e}")
            return

        success_count = 0

        for index, phone in enumerate(phones, start=1):
            print(colored(f"[{index}] {phone} uchun jarayon boshlanmoqda...", "blue"))
            await run(phone, givs, channels)
            success_count += 1
            print(colored(f"[{index}] Phone: {phone} | Jarayon yakunlandi.", "magenta"))

        print(colored(f"Umumiy muvaffaqiyatli hisoblar: {success_count}", "green"))

    if __name__ == '__main__':
        asyncio.run(main())
else:
    print("@Enshteyn40 ga murojat qiling")
