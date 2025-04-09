from telethon.sync import TelegramClient
import asyncio

api_id = 20882488
api_hash = 'cc9e8c2558b487f5e3066ca46f293676'

groups = [
    'https://t.me/Reklamahc',
    'https://t.me/greenday13chat',
    'https://t.me/Piarchaat2',
    'https://t.me/pairreklama'
]

message = '''💸💸💸💸💸💸

БЕРУ БАНКИ В ОРЕНДУ

🏦МоноБанк - 500
🏦Пумб - 500
🏦Нова Пей - 350
🏦Бвр - 250
🏦Райф - 250
🏦Изи - 250
🏦Акорд - 150

СВЯЗЬ СО МНОЮ ➡️@banksorenda👈'''

async def main():
    async with TelegramClient('session', api_id, api_hash) as client:
        while True:
            for group in groups:
                try:
                    await client.send_message(group, message)
                    print(f"Повідомлення надіслано до {group}")
                except Exception as e:
                    print(f"Помилка при надсиланні в {group}: {e}")
            await asyncio.sleep(60)

asyncio.run(main())
