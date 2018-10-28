from flask import Flask, request, abort

from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('AN9zILzP2xb3X9OPNxUZkH9X+FACbmA2Q45gok3+7HNcSRZsvW+TvvEImQcmFyO7BC4DgWycK/ULQl1Z+WBxtiCyeEhfq9RkmsFqurpIBu1qadUTAorC3F+xusK3AclqhKCeL42+ru+qI91bEtmuXgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('015a9a38cb4d598c9e8f832dc86c2314')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print('signature:'+str(signature)+'body'+str(body)+'app.logger.info'+str(app.logger.info))
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event.message.text)
    if event.message.text==u"==":
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(u"都2018還有人==不加空格"))
    elif event.message.text==u"##":
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(u"都2018還有人##不加空格"))        
    else:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text=event.message.text))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
