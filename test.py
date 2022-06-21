import requests
import json
import time
import keyboard

always = 1
count = 0
url = "https://api.warframestat.us/profile/crater29224?language=en"

while always:
    requests_mission = []
    response = requests.get(url)

    print(response)

    data = response.text
    parsed = json.loads(data)
    requests_mission.append(parsed)
    count = count + 1
    print(count)
    time.sleep(1)
