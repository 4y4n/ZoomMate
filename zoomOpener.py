import time
import datetime
import json
import os
import webbrowser

os.environ['path'] = '%PATH%;C:\Windows\System32;'
classes = json.load(open('classData.json'))
isStarted = False
for i in classes:
    date = datetime.datetime.now()
    if date.strftime("%a") in i["classActive"]:
        while True:
            date = datetime.datetime.now()
            if not isStarted:
                if date.strftime("%H") == i["startTime"].split(':')[0] and date.strftime("%M") == i["startTime"].split(':')[1]:
                    webbrowser.open(i["link"])
                    isStarted = True
            else:
                if date.strftime("%H") == i["endTime"].split(':')[0] and date.strftime("%M") == i["endTime"].split(':')[1]:
                    os.system("taskkill /f /im  Zoom.exe")
                    isStarted = False
                    break
            time.sleep(5)
