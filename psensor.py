import os
import time
import commands
# from uiautomator import device as d

for i in range(500):
    print "test p-sensor enabled %s time(s)"%i
    commands.getoutput("adb shell sendevent /dev/input/event7 2 0 4294967169")
    commands.getoutput("adb shell sendevent /dev/input/event7 2 1 4294967169")
    commands.getoutput("adb shell sendevent /dev/input/event7 0 0 0")
    time.sleep(1)
    print "test p-sensor disabled %s time(s)"%i
    commands.getoutput("adb shell sendevent /dev/input/event7 2 0 127")
    commands.getoutput("adb shell sendevent /dev/input/event7 2 1 127")
    commands.getoutput("adb shell sendevent /dev/input/event7 0 0 0")
