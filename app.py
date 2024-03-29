# -*- coding: UTF-8 -*-
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from mybase64 import *
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(
    "<Your API token>"
)
# Channel Secret
handler = WebhookHandler("895cb1c62b01c7da0c27995a23f6e291")


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    try:
        a=event.message.text
        b = a.split(' ')
        if b[0]=="0":
            print("0")
            #DAN.push('str0',b[1])
        if b[0]=="1":
            print("1")
            #DAN.push('str1',b[1])
         #Push data to an input device feature "Status"
        #==================================
        '''
        ODF_data= DAN.pull('str2') #Pull data from an output device feature "Name-O"
        if ODF_data :
            message = TextSendMessage(str(ODF_data[0]))
            line_bot_api.reply_message(event.reply_token, message)
        else :
        '''
        if b[0]=='0':
            a = Base64()
            message=TextSendMessage(a.Encode(str.encode(b[1])))
            print(message)
            line_bot_api.reply_message(event.reply_token,  message)
        if b[0]=="1":
            a = Base64()
            message=TextSendMessage(a.Decode(b[1]," ").decode("ISO-8859-1"))
            
            if message:
                print(message)
                line_bot_api.reply_message(event.reply_token,  message)
            
            #print(ODF_data)
    # you can write some codes here to handle the message sent by users
    #try:
    #    DAN.push('109062599_input', int(event.message.text)) #Push data to an input device feature "Status"
        #==================================
    #    ODF_data= DAN.pull('109062599_output') #Pull data from an output device feature "Name-O"
    #    if ODF_data :
    #        message = TextSendMessage(str(ODF_data[0]))
    #        line_bot_api.reply_message(event.reply_token, message)
            #print(ODF_data)
    except Exception as e:
        print(e)

import os

if __name__ == "__main__":

    # connect to IoTtalk server
    # ServerURL = 'http://XXX.XXX.XX.XX:XXXX'
    # Reg_addr = None

    # Define your IoTtalk Device
    # Hint: DAN.profile

    # Register

    # Deregister
    '''ServerURL = "http://140.114.77.90:9999"  # with non-secure connection
    Reg_addr = "7788"  # if None, Reg_addr= MAC address

    DAN.profile["dm_name"] = "109062599_DM"
    DAN.profile['df_list']=[ 'str0','str1', 'str2']
    # DAN.profile['d_name']= 'Assign a Device Name'

    DAN.device_registration_with_retry(ServerURL, Reg_addr)'''
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
