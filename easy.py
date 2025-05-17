from telethon import TelegramClient, events
import re
import asyncio

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
session_file = 'session.session'  # твой файл сессии

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
