import requests
from requests import get
from Waifu import Waifu as app
from pyrogram import filters, enums 
from pyrogram.types import InputMediaPhoto
from aiohttp import ClientSession as cs
from json import loads
from bs4 import BeautifulSoup as BSP
from io import BytesIO
import re

            
@app.on_message(filters.regex(r'\b(?:pin\.it|pinterest\.com)\b') & (filters.group | filters.private))
async def pin_download(_, message):
    await scrap_pins(message)
    
snap_pattern = "(?:https\:\/\/t.snapchat.com\/\S\S\S\S\S\S\S\S)"            
async def scrap_snaps(message):
    text = re.findall(snap_pattern, message.text)
    async with cs() as sess:
        msg = await message.reply("`Downloading...`", parse_mode=enums.ParseMode.MARKDOWN)
        resp = await sess.get(text[0])
        soup = BSP(await resp.text(), 'html.parser')
        tag = soup.findAll("script", attrs={'data-react-helmet':'true', 'type':'application/ld+json'})[0]
        data = loads(tag.string.strip())
        video = BytesIO(await (await sess.get(data['contentUrl'])).read())
        thumb = BytesIO(await (await sess.get(data['thumbnailUrl'])).read())
        video.name = data['name'] if data['name'] else "@YaaraOP"
        await msg.delete()
        await message.reply_video(video, caption=f"Uploaded By [{app.me.first_name}](https://t.me/{app.me.username})", thumb=thumb, parse_mode=enums.ParseMode.MARKDOWN)
           
@app.on_message(filters.regex("(?:https\:\/\/t.snapchat.com\/\S\S\S\S\S\S\S\S)") & (filters.group | filters.private))
async def snap_download(_, message):
    await scrap_snaps(message)

async def download_ig(query):
	url = "https://instagram-bulk-scraper-latest.p.rapidapi.com/media_download_from_url"
	payload = { "url": query}
	headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "1852da1a0dmshb013cd0683d2903p12df7ajsnd5d070b1f894",
	"X-RapidAPI-Host": "instagram-bulk-scraper-latest.p.rapidapi.com"
	}
	response = requests.post(url, json=payload, headers=headers)
	return response.json()['data']

@app.on_message(filters.regex(r'https://www\.instagram\.com/reel/.*') & (filters.group | filters.private))
async def insta(client, message):
            			chat_id = message.chat.id
            			query = message.text
            			data = await download_ig(query)
            			if data:
            				await message.reply_video(video=data['main_media_hd'], caption=f"Download by {app.me.mention}")
            			else:
            				await message.reply("Give A Valid Url")