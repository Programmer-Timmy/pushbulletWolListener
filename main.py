import websocket  # WebSocket client library
import json  # Library to handle JSON data
import requests  # Library to make HTTP requests
import wakeonlan  # Library to send Wake-on-LAN packets

# Replace with your Pushbullet API token
API_TOKEN = 'your_api_token_here'
# Replace with your PC's MAC address
MAC_ADDRESS = 'your_mac_address_here'
# The specific message to trigger the WoL packet
TRIGGER_MESSAGE = 'your_trigger_message_here'


def send_wol_packet(mac_address):
    wakeonlan.send_magic_packet(mac_address)
    print(f"WoL packet sent")


def get_last_push(api_url, headers):
    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to get pushes: {response.status_code}")
        return
    pushes = response.json()
    return pushes['pushes'][0]['body']


def on_message(ws, message):
    print("Received message:", message)
    data = json.loads(message)
    if 'subtype' in data and data['subtype'] == 'push':
        push_body = get_last_push('https://api.pushbullet.com/v2/pushes', {'Access-Token': API_TOKEN})
        if push_body is None:
            print('No pushes found')
            return

        if TRIGGER_MESSAGE == push_body:
            print('Trigger message received')
            send_wol_packet(MAC_ADDRESS)


def on_error(ws, error):
    print(f"Error: {error}")


def on_close(ws):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")


websocket.enableTrace(True)
ws = websocket.WebSocketApp(
    f"wss://stream.pushbullet.com/websocket/{API_TOKEN}",
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,

)
ws.on_open = on_open
ws.run_forever()
