#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "23270278")
API_HASH = os.environ.get("API_HASH", "87a837607d9761cdf98bbc3e61eef098")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7238067007:AAG1pDJTUBwKzeeu0o-G0acMrQUA4JN9Zug")
ADMIN = int(os.environ.get("ADMIN", '6890795853'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "Teluguzoneofc")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "BujjiSupport")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://parcel:malliga@cluster0.xoax6ur.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
CAPTION = os.environ.get("CAPTION", "")
group = environ.get('GROUP', '-1002191685064')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://graph.org/file/cfb3eb77fd01bae0a2344.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '809614790'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1002157233898)
