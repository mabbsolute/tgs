# -*- coding: utf-8 -*-
import requests
import pandas as pd
from licensing.models import *
from licensing.methods import Key, Helpers
import time
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
    import struct
    import base64
    import asyncio
    import ipaddress
    from pathlib import Path
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
    from telethon.sessions import StringSession
    from typing import Union
    from dataclasses import dataclass

    from telethon import TelegramClient
    from telethon.sessions import StringSession

    import aiosqlite


    @dataclass
    class Session:
        dc_id: int
        test_mode: bool
        auth_key: bytes
        date: int
        user_id: int
        is_bot: bool


    async def get_data_from_sessions_table(session_file: Union[Path, str]) -> Session:
        async with aiosqlite.connect(session_file) as db:
            async with db.execute("SELECT dc_id, test_mode, auth_key, date, user_id, is_bot FROM sessions") as cursor:
                row = await cursor.fetchone()
                session = Session(
                    dc_id=row[0],
                    test_mode=bool(row[1]),
                    auth_key=row[2],
                    date=row[3],
                    user_id=row[4],
                    is_bot=bool(row[5])
                )

        return session


    async def get_pyrogram_session_string(session: Session) -> str:
        api_id = 2040  # edit
        STRING_FORMAT = ">BI?256sQ?"
        packed = struct.pack(
            STRING_FORMAT,
            session.dc_id,
            api_id,
            session.test_mode,
            session.auth_key,
            session.user_id,
            session.is_bot
        )

        session_string = base64.urlsafe_b64encode(packed).decode().rstrip("=")
        return session_string


    async def get_telethon_session_string(session: Session) -> str:
        _STRUCT_PREFORMAT = '>B{}sH256s'

        CURRENT_VERSION = '1'
        ip = ipaddress.ip_address("149.154.167.50")
        auth_key = session.auth_key
        packed = struct.pack(
            _STRUCT_PREFORMAT.format(len(ip.packed)),
            session.dc_id,
            ip.packed,
            443,
            auth_key
        )
        return CURRENT_VERSION + StringSession.encode(packed)

    import csv
    phonecsv = "phone"
    with open(f'{phonecsv}.csv', 'r') as f:
        phlist = [row[0] for row in csv.reader(f)]
    print('Jami Nomerlar: ' + str(len(phlist)))


    print("OXIRGI KOD YANGILANGAN VAQT: 12.12.2024  01:33 AM")
    current_start_param = str(input("Ref id kiriting: ")) 
    stikersorash = int(input("Stiker qo'yilsinmi: Ha = 0 || Yo'q = 1: "))
    sotash = int(input("12.12.2024 kungi zadaniyalar  = 0:  ||\nAdd Paws emoji qilish (NOQONUNIY)  = 1:  ||\n Doimiy zadaniyalar qilish = 2: "))

    async def main():
        indexx = 0
        import time
        
        for phone in phlist: 
            indexx += 1
            print(f'Index : {indexx}')
            print(f"Raqam {phone}")
            phone = utils.parse_phone(phone)
            path = f'memory/{phone}.session'
            session = await get_data_from_sessions_table(path)
            pyrogram_session_string = await get_pyrogram_session_string(session)
            telethon_session_string = await get_telethon_session_string(session)

            #print(pyrogram_session_string)
            #print(telethon_session_string)
            client = TelegramClient(session=StringSession(telethon_session_string), api_id=22962676, api_hash="543e9a4d695fe8c6aa4075c9525f7c57")
            try:
                async with client:
                    global current_start_param
                    bot_entity = await client.get_entity("PAWSOG_bot")
                    bot = InputUser(user_id=bot_entity.id, access_hash=bot_entity.access_hash)
                    bot_app = InputBotAppShortName(bot_id=bot, short_name="PAWS")
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
                            #Paws pizdes olnaxuy
                            upfsytotos1 = {
                                "questId": "675729bc8a00f11f8cf8c1fd"
                            }
                            response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=upfsytotos1, timeout=20)
                            response_data = response.json()
                            if response_data.get("success") and response_data.get("data"):
                                print("Reach 1 th Milistone  zadanyasi bajarildi")
                            else:
                                print("Reach 1 th Milistone  zadanyasi bajarilmadi")
                            time.sleep(3)
                            response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=upfsytotos1, timeout=10)
                            response_data = response.json()
                            if response_data.get("success") and response_data.get("data"):
                                print("Reach 1 th Milistone bonus olindi")
                            else:
                                print("Reach 1 th Milistone bonus olinmadi yoki claim hali ochilmagan keyinroq ishlating")
                            #2-milistone
                            upfsytotos2 = {
                                "questId": "67572a2c8a00f11f8cf8c1ff"
                            }
                            response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=upfsytotos2, timeout=20)
                            response_data = response.json()
                            if response_data.get("success") and response_data.get("data"):
                                print("Reach 2 th Milistone zadanyasi bajarildi")
                            else:
                                print("Reach 2 th Milistone  zadanyasi bajarilmadi")
                            time.sleep(3)
                            response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=upfsytotos2, timeout=10)
                            response_data = response.json()
                            if response_data.get("success") and response_data.get("data"):
                                print("Reach 2 th Milistone bonus olindi")
                            else:
                                print("Reach 2 th Milistone bonus olinmadi yoki claim hali ochilmagan keyinroq ishlating")
                            #3 reach milistone
                            upfsytotos3 = {
                                "questId": "6757a207ec9bc04f1beb0e75"
                            }
                            response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=upfsytotos3, timeout=20)
                            response_data = response.json()
                            if response_data.get("success") and response_data.get("data"):
                                print("Reach 3 th Milistone zadanyasi bajarildi")
                            else:
                                print("Reach 3 th Milistone  zadanyasi bajarilmadi")
                            time.sleep(3)
                            response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=upfsytotos3, timeout=10)
                            response_data = response.json()
                            if response_data.get("success") and response_data.get("data"):
                                print("Reach 3 th Milistone bonus olindi")
                            else:
                                print("Reach 3 th Milistone bonus olinmadi yoki claim hali ochilmagan keyinroq ishlating")
                            #rech 4 milistone
                            upfsytotos4 = {
                                "questId": "6757a21dec9bc04f1beb0e77"
                            }
                            response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=upfsytotos4, timeout=20)
                            response_data = response.json()
                            if response_data.get("success") and response_data.get("data"):
                                print("Reach 4 th Milistone zadanyasi bajarildi")
                            else:
                                print("Reach 4 th Milistone  zadanyasi bajarilmadi")
                            time.sleep(3)
                            response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=upfsytotos4, timeout=10)
                            response_data = response.json()
                            if response_data.get("success") and response_data.get("data"):
                                print("Reach 4 th Milistone bonus olindi")
                            else:
                                print("Reach 4 th Milistone bonus olinmadi yoki claim hali ochilmagan keyinroq ishlating")
                            #rech 5 milistone
                            upfsytotos5 = {
                                "questId": "6757a232ec9bc04f1beb0e79"
                            }
                            response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=upfsytotos5, timeout=20)
                            response_data = response.json()
                            if response_data.get("success") and response_data.get("data"):
                                print("Reach 5 th Milistone zadanyasi bajarildi")
                            else:
                                print("Reach 5 th Milistone  zadanyasi bajarilmadi")
                            time.sleep(3)
                            response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=upfsytotos5, timeout=10)
                            response_data = response.json()
                            if response_data.get("success") and response_data.get("data"):
                                print("Reach 5 th Milistone bonus olindi")
                            else:
                                print("Reach 5 th Milistone bonus olinmadi yoki claim hali ochilmagan keyinroq ishlating")
                            #milistone 6
                            #upfsytotos6 = {
                            #    "questId": "6758d84842df2161c728c742"
                            #}
                            #response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=upfsytotos6, timeout=20)
                            #response_data = response.json()
                            #if response_data.get("success") and response_data.get("data"):
                            #    print("Reach 6 th Milistone zadanyasi bajarildi")
                            #else:
                            #    print("Reach 6 th Milistone  zadanyasi bajarilmadi")
                            #time.sleep(3)
                            #response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=upfsytotos6, timeout=10)
                            #response_data = response.json()
                            #if response_data.get("success") and response_data.get("data"):
                            #    print("Reach 6 th Milistone bonus olindi")
                            #else:
                            #    print("Reach 6 th Milistone bonus olinmadi yoki claim hali ochilmagan keyinroq ishlating")
                        elif sotash == 1:
                            import time
                            print("Premium stiker zadanyasini o'zini bajaramiz")
                            #Add PAWS emoji
                            k5plus = {
                                "questId": "6740b2cb15bd1d26b7b71266"
                            }
                            response = requests.post("https://api.paws.community/v1/quests/completed", headers=leaders, json=k5plus, timeout=20)
                            response_data = response.json()
                            if response_data.get("success") and response_data.get("data"):
                                print("Add PAWS emoji zadanyasi bajarildi")
                            else:
                                print("Add PAWS emoji  zadanyasi bajarilmadi")
                            time.sleep(3)
                            response = requests.post("https://api.paws.community/v1/quests/claim", headers=leaders, json=k5plus, timeout=10)
                            response_data = response.json()
                            if response_data.get("success") and response_data.get("data"):
                                print("Add PAWS emoji bonus olindi")
                            else:
                                print("Add PAWS emoji bonus olinmadi yoki claim hali ochilmagan keyinroq ishlating")
                        else:
                            #Study paws
                            import time
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
                            
                            try:
                                await client(JoinChannelRequest("https://t.me/bums_official"))
                                print("Blum kanaliga qoshildi")
                            except Exception as d:
                                print(f"Kanalga qoshilishd axatolik {d}")
                            
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
                    
            except Exception as e:
                print("error: ", e)
                continue


    asyncio.run(main()) 
else:
    print("@Enshteyn40 ga murojat qiling")
