#!/usr/bin/python

# set battery
from psutil import sensors_battery

percent = round(sensors_battery().percent)
charging = sensors_battery().power_plugged

if percent <= 20 and not charging:
    import gi
    gi.require_version('Notify', '0.7')
    from gi.repository import Notify
    Notify.init("BAT")
    notify = Notify.Notification.new(
            "Low battery",
            "Only "+str(percent)+"% left",
            "BAT")
    notify.show()
elif percent >= 95 and charging:
    import gi
    gi.require_version('Notify', '0.7')
    from gi.repository import Notify
    Notify.init("BAT")
    notify = Notify.Notification.new(
            "Full battery",
            "Charged more than "+str(percent)+"%",
            "BAT")
    notify.show()
