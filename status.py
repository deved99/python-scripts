#!/usr/bin/python
def time2str(num):
    if num<10:
        return "0"+str(num)
    else:
        return str(num)

# Import battery
import psutil
battery0 = psutil.sensors_battery()
battery = str(round(battery0.percent))+'%'
if battery0.power_plugged:
    battery = battery+" 🔌"
else:
    battery = battery+" 🔋"

# Import time
import datetime
time = datetime.datetime.now()
time = time2str(time.hour)+":"+time2str(time.minute)+" 🕒"

# Export notification
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Time")
notify = Notify.Notification.new(time, battery, "Time")
notify.show()
