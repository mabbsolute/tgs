import requests
import pandas as pd
from licensing.models import *
from licensing.methods import Key, Helpers
import subprocess
from telethon import utils
# GitHub repository URL
url = "https://raw.githubusercontent.com/mabbsolute/tgs/refs/heads/main/requestcr.csv"

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

print(f"DEVICE ID: {machine_code}")

# Mashina kodini tekshirish
if machine_code in hash_values_list: 
    from telethon.tl.functions.messages import ImportChatInviteRequest
    import time
    import requests
    from urllib.parse import unquote
    from fake_useragent import UserAgent
    from telethon import TelegramClient
    from telethon.sessions import StringSession
    from telethon.tl.functions.channels import JoinChannelRequest
    from telethon.tl.functions.messages import RequestWebViewRequest
    from telethon.tl.functions.account import UpdateStatusRequest
    import csv
    print("Oxirgi kod yangilangan vaqti: 18.12.2021 7:55 PM")
    with open(r"/storage/emulated/0/giv/ochiqkanal.csv", 'r') as f:
        premium_channels = [row[0] for row in csv.reader(f)]
    with open(r"/storage/emulated/0/giv/yopiqkanal.csv", 'r') as f:
        yopiq_channels = [row[0] for row in csv.reader(f)]
    with open(r"/storage/emulated/0/giv/giv.csv", 'r') as f:
        giv_ids_ozim = [row[0] for row in csv.reader(f)]
    with open(r"/storage/emulated/0/giv/captcha2.csv", 'r') as f: 
        reader = csv.reader(f)
        captchapai = next(reader)[0]
    #with open(r"C:\join\ochiqkanal.csv", 'r') as f:
    #    premium_channels = [row[0] for row in csv.reader(f)]
    #with open(r"C:\join\yopiqkanal.csv", 'r') as f:
    #    yopiq_channels = [row[0] for row in csv.reader(f)] 
    #with open(r"C:\join\givid.csv", 'r') as f:
    #    giv_ids_ozim = [row[0] for row in csv.reader(f)] 
    #captchapai = "1b8324721dc1628de785d91cb5f6a6da"
    
    from twocaptcha import TwoCaptcha

    RESET = "\033[0m"
    LIGHT_GREEN = "\033[92m" 
    LIGHT_CYAN = "\033[96m"  

    def get_init_data(auth_url):
        init_data = unquote(auth_url.split('tgWebAppData=', 1)[1].split('&tgWebAppVersion', 1)[0])
        return init_data

    async def get_auth_url(tg_client: TelegramClient, code: str):
        async with tg_client:
            bot = await tg_client.get_entity("@send")
            web_view = await tg_client(
                RequestWebViewRequest(
                    peer=bot,
                    bot=bot,
                    platform='tdesktop',
                    from_bot_menu=False,
                    url=f"https://app.send.tg/giveaways/{code}"
                )
            )
            url = web_view.url.replace('tgWebAppVersion=7.0', 'tgWebAppVersion=8.0')
            return url

    async def request_participate(api_key, site_key, url, auth_url, giveaway_code, tg_client: TelegramClient, name: str):
        try:
            http_client = requests.Session()

            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://app.send.tg',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://app.send.tg/',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24", "Microsoft Edge WebView2";v="131"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
            }

            http_client.headers.update(headers)

            init_data = get_init_data(auth_url)
            json_data = {'initData': init_data}

            response = http_client.post('https://api.send.tg/internal/v1/authentication/webapp', headers=headers, json=json_data)
            if response.ok:
                print(f"{LIGHT_GREEN}{name}{RESET} | Ro'yxatdan o'tildi")
            else:
                print(f"{LIGHT_GREEN}{name}{RESET} | Ro'yxatdan o'tishda xatolik | Response: <lr>{response.text}</lr>")
                return False
            
            

            response = http_client.get(f'https://api.send.tg/internal/v1/giveaway/{giveaway_code}')
            if response.ok:
                await tg_client.start()
                await tg_client(UpdateStatusRequest(offline=False))
                response_json = response.json()
                # Faqat kerakli ma'lumotlarni olish
                #invite_hash = response_json.get("invite_hash")
                #invited_users = response_json.get("invited_users")
                #win_chance = response_json.get("win_chance")
                summa = response_json.get("amount_usd")
                #prepared_inline_message_id = response_json.get("prepared_inline_message_id")
                member_status = response_json.get("member_status")
                status = response_json.get("status")
                can_join = response_json.get("can_join")
                winners_count = response_json.get("winners_count")
                asset = response_json.get("asset")
                qatnasgyabdimi = response_json.get("member_status")
                
                # Kerakli formatda chiqarish
                print(f"{LIGHT_CYAN}A'zolik holati: {member_status}{RESET}")
                print(f"{LIGHT_CYAN}Giveaway holati: {status}{RESET}")
                print(f"{LIGHT_CYAN}Bu givga qo'shila oladimi: {'Ha' if can_join else 'Yo‘q'}{RESET}")
                print(f"{LIGHT_CYAN}G'oliblar soni: {winners_count}{RESET}")
                print(f"{LIGHT_CYAN}Mukofot puli: {summa} - {asset}{RESET}")
                
            if can_join and qatnasgyabdimi == "not_member":
                
                print("Givga qo'shilishni boshladik!!!")
                for channel_link in premium_channels:
                    
                    try: 
                        await tg_client(JoinChannelRequest(channel_link))
                    except:
                        pass
                    try:
                        await tg_client(JoinChannelRequest(channel_link))
                        print(f"{LIGHT_GREEN}{name}{RESET} | Kanalga qo'shildi {LIGHT_CYAN}{channel_link}{RESET}")
                    except Exception as e:
                        print(f"{LIGHT_GREEN}{name}{RESET} | Kanalga qo'shilishda Xatolik {LIGHT_CYAN}{channel_link}{RESET}")
                for yopiq_link in yopiq_channels:
                    try: 
                        await tg_client(ImportChatInviteRequest(yopiq_link))
                        print(f"{LIGHT_GREEN}{name} | Kanalga qo'shildi {LIGHT_CYAN}{yopiq_link}{RESET}")
                    except:
                        print(f"{LIGHT_GREEN}{name}{RESET} | Kanalga qo'shilishda Xatolik {LIGHT_CYAN}{yopiq_link}{RESET}")
                print(f"{LIGHT_GREEN}{name}{RESET} | Cloudflarega xuyyer qilayabman |")
                solver = TwoCaptcha(api_key)
                result = solver.turnstile(sitekey=site_key, url=url)
                challenge_token = result.get('code')

                if not challenge_token:
                    print(f"{LIGHT_GREEN}{name}{RESET} | Cloudflare pizdes qildi")
                    return False

                print(f"{LIGHT_GREEN}{name}{RESET} | Cloudflareni pizdes qildik")
                

                for _ in range(3):
                    try:
                        response = http_client.post(
                            f'https://api.send.tg/internal/v1/giveaway/{giveaway_code}/participate',
                            json={'challenge_token': challenge_token}
                        )
                        if response.ok:
                            print(f"{LIGHT_GREEN}{name}{RESET} | Givda qatnashish so'rovi muvaffaqiyatli yuborildi")
                            return True
                        print(f"{LIGHT_GREEN}{name}{RESET} | Givda qatnashishda xatolik | Response: <lr>{response.json()}</lr>")
                        time.sleep(1)
                    except Exception as e:
                        print(f"{LIGHT_GREEN}{name}{RESET} | Requestda xatolik: {e}")
            elif qatnasgyabdimi == "member":
                print(f"{LIGHT_GREEN}Allqachon bu givda qatnashayabdi -- ")
            elif not can_join:
                print(f"{LIGHT_GREEN}Ushbu givga qatnasha olmaydi")
            else:
                print(f"{LIGHT_GREEN}{name}{RESET} | Givda qatnasha olmaydi")
        except Exception as e:
            print(f"{name} | Xatolik: {e}")
        return False
            

    async def main():
        indexx = 0
        import csv
        phonecsv = "phone"
        with open(f'{phonecsv}.csv', 'r') as f:
            phlist = [row[0] for row in csv.reader(f)]
        print('Jami Nomerlar: ' + str(len(phlist)))
        api_id = 22962676
        api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'
        captcha_api_key = captchapai
        captcha_site_key = '0x4AAAAAAActoBfh_En8yr3T'
        captcha_url = 'https://app.send.tg/giveaways/{code}'
        
        
        for phone in phlist:
            phone = utils.parse_phone(phone)
            indexx += 1
            print(f"\033[38;5;207mRaqam tartibi - {indexx}\033[0m")
            tg_client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
            try:
                await tg_client.connect()
                if not await tg_client.is_user_authorized():
                    print(f"❌ {phone} raqam sessiyadan chiqib ketgan yoki avtorizatsiya yo'q.")
                    await tg_client.disconnect()
                    continue 
                
                print(f"✅ {phone} muvaffaqiyatli ulanib ishlayapti.")
                await tg_client(UpdateStatusRequest(offline=False))

                for giveaway_code in giv_ids_ozim:
                    auth_url = await get_auth_url(tg_client, giveaway_code)
                    await request_participate(
                        api_key=captcha_api_key,
                        site_key=captcha_site_key,
                        url=captcha_url.format(code=giveaway_code),
                        auth_url=auth_url,
                        giveaway_code=giveaway_code,
                        tg_client=tg_client,
                        name=f"{phone}"
                    )

                print(f"✅ {phone} uchun barcha jarayonlar tugadi.")
                await tg_client.disconnect()

            except Exception as e:
                print(f"⚠️ {phone} uchun xatolik: {e}")
                await tg_client.disconnect()


    if __name__ == "__main__":
        import asyncio
        asyncio.run(main())
else:
    print("@Enshteyn40 ga murojat qiling")
