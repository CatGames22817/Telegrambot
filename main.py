from telethon import TelegramClient
import asyncio

# Твої дані
api_id = 20882488
api_hash = 'cc9e8c2558b487f5e3066ca46f293676'
phone_number = '+380977293929'

# Текст повідомлення
message_text = """
💸💸💸💸💸💸

БЕРУ БАНКИ В ОРЕНДУ

🏦МоноБанк - 500  
🏦Пумб - 500  
🏦Нова Пей - 350  
🏦Бвр - 250  
🏦Райф - 250  
🏦Изи - 250  
🏦Акорд - 150

СВЯЗЬ СО МНОЮ ➡️@banksorenda👈
"""

# Список груп
targets = [
    'https://t.me/Reklamahc',
    'https://t.me/greenday13chat',
    'https://t.me/Piarchaat2',
    'https://t.me/pairreklama'
]

async def send_messages(client):
    for channel_link in targets:
        try:
            await client.send_message(channel_link, message_text)
            print(f"Надіслано в {channel_link}")
        except Exception as e:
            print(f"Помилка для {channel_link}: {e}")

async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone=phone_number)

    while True:
        await send_messages(client)
        await asyncio.sleep(60)  # чекати 60 секунд

asyncio.run(main())
