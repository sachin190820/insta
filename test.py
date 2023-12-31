from flask import Flask, request

app = Flask(__name__)
VERIFY_TOKEN = '123'

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Instagram webhook verification
        hub_mode = request.args.get('hub.mode')
        hub_verify_token = request.args.get('hub.verify_token')
        hub_challenge = request.args.get('hub.challenge')

        if hub_mode == 'subscribe' and hub_verify_token == VERIFY_TOKEN:
            print('Webhook verified successfully.')
            return hub_challenge, 200
        else:
            print('Failed to verify webhook.')
            return '', 403
    elif request.method == 'POST':
        # JSON data received from Instagram
        json_data = request.get_json()
        print(json_data)  # You can customize this to store or process the data as needed
        return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
