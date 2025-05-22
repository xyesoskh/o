from telethon import TelegramClient

# Вставь сюда свои данные от my.telegram.org
api_id = 19089460    # твой api_id
api_hash = 'bd81e729a0fbdde3071f8ec81c173d70'  # твой api_hash

# Параметры кастомизации, чтобы в Telegram в разделе "Устройства" показывалось свое имя
system_version = 'Windows 11 Pro'
device_model = 'Tvoy Nomer yje y zyami'
app_version = '1.0.0'

# Название файла сессии
session_name = 'custom_session'

client = TelegramClient(
    session_name,
    api_id,
    api_hash,
    system_version=system_version,
    device_model=device_model,
    app_version=app_version
)

async def main():
    await client.start()
    print("Клиент запущен с кастомным названием устройства!")
    # Здесь можно писать код, что делать дальше
    # Например, получить инфу о текущем пользователе
    me = await client.get_me()
    print(me.stringify())

import asyncio
asyncio.run(main())
