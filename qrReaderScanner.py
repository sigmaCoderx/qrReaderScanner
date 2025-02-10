
import requests
from telebot import TeleBot,types,util
from telebot.util import user_link
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = TeleBot("BotToken",parse_mode="HTML")

markup = InlineKeyboardMarkup()
group = InlineKeyboardButton("Group", url="https://t.me/neuralg")
channel = InlineKeyboardButton("Channel", url="https://t.me/neuralp")
markup.add(group, channel)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id,
                      f"Hey {user_link(msg.from_user)}Send text or any string to create a qr and \nalso you can send me a QR code to scan.",
                      reply_markup=markup)

@bot.message_handler(content_types=["text"])
def createQr(msg):
    text = msg.text
    createQr = f"https://api.qrserver.com/v1/create-qr-code/?data={text}"
    bot.send_chat_action(chat_id=msg.chat.id,action="upload_photo")
    bot.send_photo(msg.chat.id, createQr,caption=f"Here is a qr for your query: {text}",reply_markup=markup)

@bot.message_handler(content_types=["photo"])
def scanQr(msg):
    # print(msg)
    file_info = bot.get_file(msg.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    with open("qr.png", 'wb') as new_file:
        new_file.write(downloaded_file)
    
    with open("qr.png", "rb") as img:
        url = "https://api.qrserver.com/v1/read-qr-code/"
        files = {"file": img}
        
        response = requests.post(url, files=files)
        
        if response.status_code == 200:
            data = response.json()
            scannedData = data[0]['symbol'][0]['data']
            bot.send_chat_action(chat_id=msg.chat.id,action="typing")
            bot.send_message(msg.chat.id, f"Scanned Output: ```\n{scannedData}```",
                             reply_markup=markup,disable_web_page_preview=True,parse_mode="MarkdownV2")
        else:
            bot.send_message(msg.chat.id, f"Error: {response.status_code}\nsend the correct qr img",reply_markup=markup)
                
bot.infinity_polling()