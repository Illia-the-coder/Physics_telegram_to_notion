import os
import csv
import asyncio
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
import pandas as pd
# Replace these with your own API ID, hash, and the target group's username
api_id = 29848792
api_hash = '918e0e0057edfa32b962802c2659517f'
group_username = 'physics171'

# The directory to save the images
IMAGE_DIR = 'images'

if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)


# Create a CSV file and write the header
with open('images_info.csv', 'w', newline='') as csvfile:
    fieldnames = ['file_name', 'url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()


async def download_images(client):
    data = []
    async for message in client.iter_messages(group_username):
        if message.photo:
            data.append(message.photo[-1].file_id)
        elif message.video:
            data.append(message.video.file_id)
        elif message.audio:
            data.append(message.audio.file_id)
        elif message.document:
            data.append(message.document.file_id)

    df = pd.DataFrame(data, columns=['file_name', 'date', 'from'])
    print(df)
    # df.to_csv('images_info.csv', index=False)


async def main():
    async with TelegramClient('anon', api_id, api_hash) as client:
        await download_images(client)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
