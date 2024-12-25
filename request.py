import requests
import pandas as pd
from licensing.models import *
from licensing.methods import Key, Helpers
import subprocess
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
    import requests
    from urllib.parse import unquote
    from fake_useragent import UserAgent
    from telethon import TelegramClient
    from telethon.sessions import StringSession
    import fake_useragent
    from telethon.tl.functions.channels import JoinChannelRequest
    from telethon.tl.functions.messages import RequestWebViewRequest
    from telethon.tl.functions.account import UpdateStatusRequest
    import csv
    print("Oxirgi kod yangilangan vaqti: 25.12.2021 9:37 AM")
    # with open(r"/storage/emulated/0/giv/ochiqkanal.csv", 'r') as f:
    #     premium_channels = [row[0] for row in csv.reader(f)]
    # with open(r"/storage/emulated/0/giv/yopiqkanal.csv", 'r') as f:
    #     yopiq_channels = [row[0] for row in csv.reader(f)]
    with open(r"/storage/emulated/0/giv/giv.csv", 'r') as f:
        giv_ids_ozim = [row[0] for row in csv.reader(f)]
    with open(r"/storage/emulated/0/giv/captcha2.csv", 'r') as f: 
        reader = csv.reader(f)
        captchapai = next(reader)[0]
    #with open(r"C:\join\captcha2.csv", 'r') as f:
    #    reader = csv.reader(f)
    #    captchapai = next(reader)[0]
    #with open(r"C:\join\givid.csv", 'r') as f:
    #    giv_ids_ozim = [row[0] for row in csv.reader(f)] 
        
    givsonlari = len(giv_ids_ozim)
    sorash = int(input("Referal sistema bilan bosilsinmi: Yo'q = 0 || Ha = 1: "))
    harnechtada = int(input("Har nechtada referal id almashsin: "))
    
    from twocaptcha import TwoCaptcha

    RESET = "\033[0m"
    LIGHT_GREEN = "\033[92m" 
    TOQ_OQ = "\033[38;2;230;230;250m"  # To'q oq rang RGB (230, 230, 250)
    LIGHT_CYAN = "\033[96m"  
    print(f"{TOQ_OQ}'Qatnashilayotgan Giveawaylar sonlari -- {givsonlari}{RESET}")

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
    async def join_channels(tg_client, chats_data):
        for chat in chats_data:
            chat_id = chat['link']
            try:
                if chat_id.startswith('https://t.me/+'):
                    chat_username = chat_id.split('+')[-1]
                    try: 
                        await tg_client(ImportChatInviteRequest(chat_username))
                        time.sleep(1)
                    except Exception as e:
                        print(f"{LIGHT_CYAN}Qo'shilishda xatolik {chat_username}: {e}")   
                else:
                    try: 
                        await tg_client(JoinChannelRequest(chat_id))
                        time.sleep(1)
                    except Exception as e:
                        print(f"{LIGHT_CYAN}Qo'shilishda xatolik {chat_id}: {e}")  
                print(f"{LIGHT_CYAN}Kanalalrga muvaffaqiyatli qo'shildi: {chat_id}")
            except Exception as e:
                print(f"Failed to join {chat_id}: {e}")
                
    referalid_map = {}
    async def request_participate(api_key, site_key, url, auth_url, giveaway_code, indexx, tg_client: TelegramClient, name: str):
        global referalid_map
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
                'user-agent': fake_useragent.UserAgent().random,
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
                summa = response_json.get("amount_usd")
                member_status = response_json.get("member_status")
                status = response_json.get("status")
                can_join = response_json.get("can_join")
                winners_count = response_json.get("winners_count")
                asset = response_json.get("asset")
                
                # Kerakli formatda chiqarish
                print(f"{LIGHT_CYAN}A'zolik holati: {member_status}{RESET}")
                print(f"{LIGHT_CYAN}Giveaway holati: {status}{RESET}")
                print(f"{LIGHT_CYAN}Bu givga qo'shila oladimi: {'Ha' if can_join else 'Yo‘q'}{RESET}")
                print(f"{LIGHT_CYAN}G'oliblar soni: {winners_count}{RESET}")
                print(f"{LIGHT_CYAN}Mukofot puli: {summa} - {asset}{RESET}")
                
            if can_join and member_status == "not_member":
                if response_json.get('chats'):
                    chats_data = response_json['chats']
                    await join_channels(tg_client, chats_data)
                        
                    
                    print("Givga qo'shilishni boshladik!!!")
                print(f"{LIGHT_GREEN}{name}{RESET} | Cloudflarega sorov yuborayabman")
                solver = TwoCaptcha(api_key)
                result = solver.turnstile(sitekey=site_key, url=url)
                challenge_token = result.get('code')

                if not challenge_token:
                    print(f"{LIGHT_GREEN}{name}{RESET} | Cloudflare pizdes qildi")
                    return False

                print(f"{LIGHT_GREEN}{name}{RESET} | Cloudflareni pizdes qildik")
                current_referalid = referalid_map.get(giveaway_code, "")
                

                for _ in range(3):
                    try:
                        if sorash == 0:
                            print("Referal sistemasiz bosilayabdi")
                            response = http_client.post(
                                f'https://api.send.tg/internal/v1/giveaway/{giveaway_code}/participate',
                                json={'challenge_token': challenge_token}
                            )
                        else:
                            print("Referal sistema bilan bosilayabdi")
                            if indexx == 1:
                                response = http_client.post(
                                    f'https://api.send.tg/internal/v1/giveaway/{giveaway_code}/participate',
                                    json={'challenge_token': challenge_token}
                                )
                            else:
                                response = http_client.post(
                                    f'https://api.send.tg/internal/v1/giveaway/{giveaway_code}/participate',
                                    json={'challenge_token': challenge_token, 'invite_hash': current_referalid}
                                )
                        if response.ok:
                            print(f"{LIGHT_GREEN}{name}{RESET} | Givda qatnashish so'rovi muvaffaqiyatli yuborildi")
                            await asyncio.sleep(3)
                            pesponse = http_client.get(f'https://api.send.tg/internal/v1/giveaway/{giveaway_code}',timeout = 5)
                            if pesponse.ok:
                                pesponse = pesponse.json()
                                # Faqat kerakli ma'lumotlarni olish
                                invite_hash = pesponse.get("invite_hash")
                                win_chance = pesponse.get("win_chance")
                                member_status = pesponse.get("member_status")
                                print(f"{TOQ_OQ}A'zolik holati: {member_status}{RESET}")
                                print(f"{TOQ_OQ}Givda yutish ehtimolligi: {win_chance}{RESET}")
                                print(f"{TOQ_OQ}Referal idsi: {invite_hash}{RESET}")
                                if member_status == "member":
                                    print(f"{TOQ_OQ}Print giveawayda qatnashayabdi")
                                    if  invite_hash != "none" and indexx % harnechtada == 0:
                                        referalid_map[giveaway_code] = invite_hash  # Yangilash
                                        print(f"{LIGHT_GREEN}Yangi referal ID saqlandi: {invite_hash}{RESET}")

                            return True
                        print(f"{LIGHT_GREEN}{name}{RESET} | Givda qatnashishda xatolik | Response: <lr>{response.json()}</lr>")
                        await asyncio.sleep(1)
                    except Exception as e:
                        print(f"{LIGHT_GREEN}{name}{RESET} | Requestda xatolik: {e}")
            elif member_status == "member":
                response = http_client.get(f'https://api.send.tg/internal/v1/giveaway/{giveaway_code}')
                if response.ok:
                    response = response.json()
                    # Faqat kerakli ma'lumotlarni olish
                    invite_hash = response.get("invite_hash")
                    win_chance = response.get("win_chance")
                    member_status = response.get("member_status")
                    print(f"{LIGHT_CYAN}A'zolik holati: {member_status}{RESET}")
                    print(f"{LIGHT_CYAN}Givda yutish ehtimolligi: {win_chance}{RESET}")
                    print(f"{LIGHT_CYAN}Ushbu Giv uchun referal idsi: {invite_hash}{RESET}")
                    if member_status == "member":
                        print(f"{TOQ_OQ}Print giveawayda qatnashayabdi")
                        
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
        phonecsv = "toza"
        with open(f'{phonecsv}.csv', 'r') as f:
            phlist = [row[0] for row in csv.reader(f)]
        print(f'{TOQ_OQ}Jami Nomerlar: ' + str(len(phlist)))
        api_id = 22962676
        api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'
        captcha_api_key = captchapai
        captcha_site_key = '0x4AAAAAAActoBfh_En8yr3T'
        captcha_url = 'https://app.send.tg/giveaways/{code}'
        
        
        for phone in phlist:
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
                        name=f"{phone}",
                        indexx = indexx
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
