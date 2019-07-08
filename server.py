#!/bin/env python

from sys import argv
import telegram
from flask import Flask, request

TOKEN=argv[1]
CHAT_ID=argv[2]

app = Flask(__name__)
bot = telegram.Bot(TOKEN)

@app.route('/', methods=['POST'])
def notify():
    bot.send_message(chat_id=CHAT_ID, text=request.form['message'])
    return 'OK'

def main():
    app.run(threaded=True,port=5001,debug=False)    

if __name__ == '__main__':
    main()
