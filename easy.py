from telethon import TelegramClient, events
import re
import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 29459757
api_hash = '7cc969764c4de8a52169570ac20000a8'
session_string = "1ApWapzMBu4Sbmc7c5s44pLQ22UEse-Uyc0U0xWkxcOshYoED_Fb71Sq54idI6hqSNWQVG_gCDQhnUQVAFd_fQMcbRbNWvmoqDM4uS02q-RTcvwQT3mDOGcabfPwYaPV8oXtHfNTOHHY8vukH6NP7gSUBA4itvhpGn74nC1SfngevCA_LfGpeoOtN_jZDMG_zlWtlpAHxlJl6w5zS7qIR6kwSvD-HfKBCKlHOAdgMndoFEda47mrj35Glz1v7OVgFcv2RhxKPWCOkcynMIwLDpDyCjj1k_1zr_LtAuaDgrLKJVz0h5Khj7122_7b0H2kypMDzGOp5fqATdKt5KeS3PzkawZENeH0="
client = TelegramClient(StringSession(session_string), api_id, api_hash)

client = TelegramClient(session_file, api_id, api_hash)

@client.on(events.NewMessage(from_users='Telegram'))
async def handler(event):
    text = event.message.message
    codes = re.findall(r'\b\d{5,6}\b', text)
    if codes:
        code = codes[0]
        print(f'Получен код: {code}')
        # Тут можно добавить автоматическую обработку, например,
        # отправить код куда-то, или вызвать функцию подтверждения.

async def main():
    await client.start()
    print('Клиент запущен, ожидаю коды...')
    await client.run_until_disconnected()

asyncio.run(main())
