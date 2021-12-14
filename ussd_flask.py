from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "sandbox"
api_key = "1ced43c113f68200d21c17b742a453eb0f052336d23466e2c4e0c35bfe16b936"
africastalking.initialize(username, api_key)

response = ""

@app.route("/", methods=['POST'])
def ussd_callback():
    text = request.values.get("text", None)

    if text      == '':
        response  = "CON What would you want to check \n"
        response += "1. My Account \n"
        response += "2. My phone number"

    elif text    == '1':
        response  = "CON Choose account information you want to view \n"
        response += "1. Account number \n"
        response += "2. Account balance"

    else :
        response = "END Invalid choice"

    return response

if __name__ == '__main__':
    app.debug =True
    app.run()
