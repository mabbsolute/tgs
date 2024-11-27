# -*- coding: utf-8 -*-
import requests
import pandas as pd
from licensing.models import *
from licensing.methods import Key, Helpers

# GitHub repository URL
url = "https://raw.githubusercontent.com/Enshteyn40/crdevice/refs/heads/main/uzsolish.csv"

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

# Mashina kodini tekshirish
if machine_code in hash_values_list: 
    from telethon import functions
    import requests
    import time
    from telethon.tl.functions.channels import JoinChannelRequest
    import csv
    from telethon import types, utils, errors
    from telethon.sync import TelegramClient
    from telethon.tl.functions.account import UpdateStatusRequest
    from telethon.tl.types import InputUser
    from telethon.tl.functions.messages import RequestAppWebViewRequest
    from urllib.parse import unquote
    import asyncio
    from telethon.tl.types import InputBotAppShortName
    
    print("OXIRGI KOD YANGILANGAN VAQT: 27.11.2024  7:34 PM")

    phonecsv = "phone"
    with open(f'{phonecsv}.csv', 'r') as f:
        phlist = [row[0] for row in csv.reader(f)]
    print('Jami Nomerlar: ' + str(len(phlist)))
    qowiwjm = 0
    qowiwjm2 = len(phlist)
    indexx = 0
    current_start_param = str(input("Ref id kiriting: ")) 
    stikersorash = int(input("Stiker qo'yilsinmi: Ha = 0 || Yo'q = 1: "))
    sotash = int(input("21.11.2024 kungi zadaniyalar : HA = 0 || YO'QSA BOSHQA RAQAM:  "))
    for deltaxd in phlist[qowiwjm:qowiwjm2]:
        try:
            indexx += 1
            phone = deltaxd
            print(f"Login {phone}")
            phone = utils.parse_phone(deltaxd)
            api_id = 22962676
            api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'
            client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
            client.start(phone)
            client(UpdateStatusRequest(offline=False))
            print(f'Index : {indexx}')

            async def main():
                global current_start_param
                bot_entity = await client.get_entity("PAWSOG_bot")
                bot = InputUser(user_id=bot_entity.id, access_hash=bot_entity.access_hash)
                bot_app = InputBotAppShortName(bot_id=bot, short_name="PAWS")
                try:
                    await client(JoinChannelRequest("https://t.me/bums_official"))
                    await client(JoinChannelRequest("https://t.me/blumcrypto"))
                    await client(JoinChannelRequest("https://t.me/DuckChainAnn"))
                    await client(JoinChannelRequest("https://t.me/tonclayton"))
                except Exception as d:
                    print(f"Kanalga qoshilishd axatolik {d}")
                web_view = await client(
                    RequestAppWebViewRequest(
                        peer=bot,
                        app=bot_app,
                        platform="android",
                        write_allowed=True,
                        start_param=current_start_param
                    )
                )
                auth_url = web_view.url
                tg_web_data_encoded = unquote(auth_url.split('tgWebAppData=', maxsplit=1)[1].split('&tgWebAppVersion', maxsplit=1)[0])

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
                    "accept": "application/json",
                    "accept-encoding": "gzip, deflate, br, zstd",
                    "accept-language": "en-US,en;q=0.9",
                    "content-type": "application/json",
                    "origin": "https://app.paws.community",
                    "referer": "https://app.paws.community/",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site"
                }
                if stikersorash == 0:
                    me = await client.get_me()
                        
                    familya = me.last_name
                    if familya is None:
                        familya = ''
                    await client(functions.account.UpdateProfileRequest(
                        first_name=f'{me.first_name} 🐾',  
                        last_name=f'{familya}'
                    ))
                    print("Ismga stiker qo'shildi")
                else:
                    pass

                payload = {
                    "data": tg_web_data_encoded,
                    "referralCode": current_start_param
                }

                response = requests.post("https://api.paws.community/v1/user/auth", headers=headers, json=payload, timeout=10)
                response_data = response.json()
                if response_data.get("success"):
                    user_token = response_data["data"][0]
                    user_data = response_data["data"][1]
                    firstname = user_data["userData"]["firstname"]
                    referrals_count = user_data["referralData"]["referralsCount"]
                    referral_code = user_data["referralData"]["code"]
                    balance = user_data["gameData"]["balance"]

                    # Print the extracted information
                    print("Ismi:", firstname)
                    print("Referallari soni:", referrals_count)
                    print("Referal codi:", referral_code)
                    print("Balansi:", balance)

                    # Har 10 ta raqamdan keyin start_param ni yangilash
                    if indexx % 10 == 0:
                        current_start_param = referral_code
                        print(f"Yangi refid: {current_start_param}")

                    # Zadanyalar bajarish
                    leaders = {
                        "authority": "api.paws.community",
                        "method": "GET",
                        "path": "/v1/quests/list",
                        "scheme": "https",
                        "accept": "application/json",
                        "accept-encoding": "gzip, deflate, br, zstd",
                        "accept-language": "en-US,en;q=0.9",
                        "authorization": f"Bearer {user_token}",
                        "content-type": "application/json",
                        "origin": "https://app.paws.community",
                        "priority": "u=1, i",
                        "referer": "https://app.paws.community/",
                        "sec-ch-ua": '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99", "Microsoft Edge WebView2";v="130"',
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": '"Windows"',
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-site",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
                    }
                    if sotash == 0:
                        import time
                        #BUMS zadanyasi 
                        
                        #Follow bums tg
                        upfsytotos = {
                            "questId": "674227d69f3873c369783888"
                        }
                        response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=upfsytotos, timeout=20)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("Follow bums tg")
                        else:
                            print("Follow bums tg zadanyasi bajarilmadi")
                        time.sleep(3)
                        response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=upfsytotos, timeout=10)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("Follow bums tg bonus olindi")
                        else:
                            print("Follow bums tg bonus olinmadi yoki oldin olingan")
                        #Explore BUMS Tg
                        #zfuckchain
                        
                        #zfuckchain follow tg
                        zukchain = {
                            "questId": "67428fb29f3873c36978388c"
                        }
                        response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=zukchain, timeout=20)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("zfuckchain follow tg")
                        else:
                            print("zfuckchain follow tg zadanyasi bajarilmadi")
                        time.sleep(3)
                        response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=zukchain, timeout=10)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("zfuckchain follow tg bonus olindi")
                        else:
                            print("zfuckchain follow tg bonus olinmadi yoki oldin olingan")
                            
                        #layton
                        #Clayton follow tg
                        clayton = {
                            "questId": "674290c39f3873c369783892"
                        }
                        response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=clayton, timeout=20)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print(" Clayton follow tg zadanyasi bajarildi")
                        else:
                            print("Clayton follow tg zadanyasi bajarilmadi")
                        time.sleep(3)
                        response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=clayton, timeout=10)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("Clayton follow tg bonus olindi")
                        else:
                            print("Clayton follow tg bonus olinmadi yoki oldin olingan")
                            
                        #Clayton boti start
                        

                        pizdesquest = {
                            "questId": "674290209f3873c369783890"
                        }
                        response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=pizdesquest, timeout=20)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("Clayton explore  zadanyasi bajarildi")
                        else:
                            print("Clayton explore zadanyasi bajarilmadi")
                        response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=pizdesquest, timeout=10)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("Clayton explore bonus olindi")
                        else:
                            print("Clayton explore bonus olinmadi yoki oldin olingan")
                        
                    else:
                        #Study paws
                        rlayload = {
                            "questId": "673a23760f9acd0470329409"
                        }
                        
                        response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=rlayload, timeout=20)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("Study paws zadanyasi bajarildi")
                        else:
                            print("Study paws zadanya bajarilmadi")
                            
                        time.sleep(2)
                            
                        response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=rlayload, timeout=10)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("Study paws zadanyasi bonusi olindi")
                        else:
                            print("Study paws zadanyasi bonus olinmadi yoki oldin olingan")
                        time.sleep(3)
                        
                        #Join paws cults on x
                                            
                        layload = {
                            "questId": "67362326ce14073e9a9e0144"
                        }
                        response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=layload, timeout=20)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("Join paws cults on x bajarildi")
                        else:
                            print("Join paws cults on x yoki kutishda")
                            
                        time.sleep(3)
                            
                        response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=layload, timeout=10)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("Join paws cults on x  olindi")
                        else:
                            print("Join paws cults on x yoki oildin olingan")
                            
                        #ismga stiker qo'yish
                        valayload = {
                            "questId": "6729082b93d9038819af5e77"
                        }
                        
                        response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=valayload, timeout=20)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("Stiker zadanyasi bajarildi")
                        else:
                            print("Stikerni bot topa olmadi keyinroq urinib ko'ring")
                        
                        response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=valayload, timeout=15)
                        response_data = response.json()
                        time.sleep(2)
                        if response_data.get("success") and response_data.get("data"):
                            print("Stiker bonusi olindi")
                        else:
                            print("Stiker bonusini olinmadi yoki oldin olingan")
                        #Blumzadanya olish
                        time.sleep(2)
                        blumayload = {
                            "questId": "6727ca4c1ee144b53eb8c08a"
                        }
                        
                        response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=blumayload, timeout=20)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("Blum kanaliga qo'shilish zadanyasi bajarildi")
                        else:
                            print("Blum kanalga qoshilish zadanyasi bajarilmadi")
                        
                        response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=blumayload, timeout=15)
                        response_data = response.json()
                        time.sleep(2)
                        if response_data.get("success") and response_data.get("data"):
                            print("Blum kanal bonusi olindi")
                        else:
                            print("Blum kanal bonusi olinmadi yoki oldin olingan")
                            
                        time.sleep(4)
                        #Follow channel
                        klik2 = {
                            "questId": "6714e8b80f93ce482efae727"
                        }
                        import time
                        response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=klik2, timeout=20)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("Follow channel bajarildi")
                        else:
                            print("Follow channel zadanyasi bajarilmadi")
                        time.sleep(3)
                        response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=klik2, timeout=10)
                        response_data = response.json()
                        if response_data.get("success") and response_data.get("data"):
                            print("Follow channel bonusi olindi")
                        else:
                            print("Follow channel bonusi olinmadi yoki oldin olingan")
                    # Har bir sessiyadan keyin balansni qayta tekshirish
                    response = requests.post("https://api.paws.community/v1/user/auth", headers=headers, json=payload, timeout=10)
                    response_data = response.json()
                    if response_data.get("success"):
                        balance = user_data["gameData"]["balance"]
                        print("Balansi:", balance)
                    else:
                        print("sorov yuborilmadi")
            with client:
                client.loop.run_until_complete(main())

        except Exception as e:
            print("error: ", e)
            continue
else:
    print("@Enshteyn40 ga murojat qiling")

