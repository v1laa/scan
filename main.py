import pywifi
import time
import re

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.scan()
time.sleep(0.5)
results = iface.scan_results()


for i in results:
    bssid = i.bssid
    ssid  = i.ssid
    bssidFIX = re.sub('[:|-]','',bssid)
    print(f"{bssidFIX}: {ssid}")
