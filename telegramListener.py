from telethon import TelegramClient, events

client = TelegramClient('anon', 12345, '<your Telegram Api Secret')

@client.on(events.NewMessage(chats='cardboty'))
async def my_event_handler(event):
    print(event.message.message)
    
        

client.start()
client.run_until_disconnected()