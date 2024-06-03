# Pushbullet WoL Listener

**Description:**
`pushbullet_wol_listener.py` is a Python script that monitors Pushbullet notifications and remotely wakes up a target computer using Wake-on-LAN (WoL) technology upon receiving specific messages.

**Features:**
- Listens for Pushbullet notifications.
- Triggers Wake-on-LAN packets when specific messages are received.
- Provides a seamless solution for remotely powering on a computer using Pushbullet messages.

**Usage:**
1. Replace placeholders with your Pushbullet API token, target computer's MAC address, and specific trigger message in the script.
2. Run the script using Python 3: `python pushbullet_wol_listener.py`.
3. Keep the script running to monitor Pushbullet notifications.

**Dependencies:**
- Python 3
- Required Python packages: `websocket-client`, `wakeonlan`

**Installation:**
1. Install Python 3 if not already installed.
2. Install required Python packages: `pip install websocket-client wakeonlan`.

**Configuration:**
- Replace placeholders in the script:
  - `YOUR_PUSHBULLET_API_TOKEN` with your Pushbullet API token.
  - `YOUR_PC_MAC_ADDRESS` with your target computer's MAC address.
  - `YOUR_SPECIFIC_MESSAGE` with the specific trigger message.

**License:**
This project is licensed under the [MIT License](LICENSE).
