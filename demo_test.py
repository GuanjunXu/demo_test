#coding=utf-8

from uiautomator import Device
import unittest
import os
import time
import random
import commands

d = Device("92593704")

pkgname = "com.qualcomm.boxworld"
actname = "%s/com.unity3d.player.UnityPlayerActivity"%pkgname

TEST_CYCLE = 500
CASE_NOW = ''
CYCLE_NOW = 0
start_time = 0

class DemoTest(unittest.TestCase):

    def setUp(self):
        super(DemoTest, self).setUp()
        try:
            self.exitDemo()
        except:
            d.press("back")
        global CASE_NOW
        global CYCLE_NOW
        global start_time
        CASE_NOW = ''
        CYCLE_NOW = 0
        start_time = time.time()
        print "start: \t%s"%(time.strftime('%Y%m%d_%H%M%S',time.localtime(start_time)))
        print "case name: ",
        # self.launchDemo()

    def tearDown(self):
        super(DemoTest, self).tearDown()
        global CASE_NOW
        global CYCLE_NOW
        global start_time
        end_time = time.time()
        print "\nend: \t%s"%(time.strftime('%Y%m%d_%H%M%S',time.localtime(end_time)))
        print "duration: \t%s"%(end_time-start_time)
        print "\t ... end at %s time(s)"%(CYCLE_NOW),
        if CYCLE_NOW < TEST_CYCLE:
            print ": Fail..."
            whatnow = time.time()
            fmtime  = time.strftime('%Y%m%d_%H%M%S',time.localtime(whatnow))
            commands.getoutput('adb shell /system/bin/screencap -p /sdcard/%s.png'%(fmtime))
            strpath = 'Demo_Test/%s_end_at_%s_%s'%(CASE_NOW,CYCLE_NOW,fmtime)
            os.makedirs(strpath)
            commands.getoutput('adb shell logcat -d > %s/logcat_%s.txt'%(strpath,fmtime))
            # commands.getoutput('adb bugrepot > %s/0_bugreport.log'%strpath)
            commands.getoutput('adb pull /sdcard/%s.png ./%s'%(fmtime,strpath))
        else:
            print ": - Pass -"
        self.exitDemo()
        CASE_NOW = ''
        CYCLE_NOW = 0

    def testLaunchExit(self):
        '''
            Steps:
                1. Launch (in setUp)
                2. Exit & Launch multi-times
                3. Exit (in tearDown)
        '''
        global CASE_NOW
        global CYCLE_NOW
        CASE_NOW = "testLaunchExit"
        print "%s ...\t"%CASE_NOW,
        d(text = "boxworld").click.wait()
        time.sleep(2)
        for i in range(TEST_CYCLE):
            CYCLE_NOW = i + 1
            self.exitDemo()
            self.launchDemo()

    def testHome(self):
        '''
            Steps:
                1. Launch (in setUp)
                2. Home key
                3. Return to demo
                4. Re-run 2~3
                5. Exit (in tearDown)
        '''
        global CASE_NOW
        global CYCLE_NOW
        CASE_NOW = "testHome"
        print "%s ...\t"%CASE_NOW,
        d(text = "boxworld").click.wait()
        time.sleep(2)
        for i in range(TEST_CYCLE):
            print "cycle now is: " + str(i)
            CYCLE_NOW = i + 1
            d.press('home')
            self.launchDemo()

    def testRecent(self):
        '''
            Steps:
                1. Launch (in setUp)
                2. Menu key
                3. Back to demo
                4.Re-run 2~3
                5. Exit (in tearDown)
        '''
        global CASE_NOW
        global CYCLE_NOW
        CASE_NOW = "testRecent"
        self.launchDemo()
        print "%s ...\t"%CASE_NOW,
        d(text = "boxworld").click.wait()
        time.sleep(2)
        for i in range(TEST_CYCLE):
            CYCLE_NOW = i + 1
            d.press('recent')
            d(resourceId = 'com.android.systemui:id/leui_recent_thumbnail', instance = 1).click.wait()
            assert d(packageName = pkgname).wait.exists(timeout = 3000)

    def testPower(self):
        '''
            Steps:
                1. Launch (in setUp)
                2. Power key twice
                3. Unlock screen
                4. Re-run 2~3
                5. Exit (in tearDown)
        '''
        global CASE_NOW
        global CYCLE_NOW
        CASE_NOW = "testPower"
        print "%s ...\t"%CASE_NOW,
        d(text = "boxworld").click.wait()
        time.sleep(2)
        self.launchDemo()
        for i in range(TEST_CYCLE):
            CYCLE_NOW = i + 1
            d.press('power')
            time.sleep(1)
            d.press('power')
            time.sleep(1)
            d().swipe.up()
            time.sleep(5)
            assert d(packageName = pkgname).wait.exists(timeout = 5000)

    # def testSlideBall(self):
    #     '''
    #         Steps:
    #             1. Launch (in setUp)
    #             2. Slide on screen multi-times
    #             3. Exit (in tearDown)
    #     '''
    #     global CASE_NOW
    #     global CYCLE_NOW
    #     CASE_NOW = "testSlideBall"
    #     print "%s ...\t"%CASE_NOW,
        d(text = "boxworld").click.wait()
        time.sleep(2)
    #     for i in range(TEST_CYCLE):
    #         CYCLE_NOW = i + 1
    #         for j in range(10):
    #             self.randomSwipe()
    #             assert d(packageName = pkgname).wait.exists(timeout = 3000)

    # def testPinchBall(self):
    #     '''
    #         Steps:
    #             1. Launch (in setUp)
    #             2. Pinch in/out on screen multi-times
    #             3. Exit (in tearDown)
    #     '''
    #     global CASE_NOW
    #     global CYCLE_NOW
    #     CASE_NOW = "testPinchBall"
    #     print "%s ...\t"%CASE_NOW,
        d(text = "boxworld").click.wait()
        time.sleep(2)
    #     for i in range(TEST_CYCLE):
    #         CYCLE_NOW = i + 1
    #         method = random.choice(["in", "out"])
    #         self.randomPinch(method)
    #         assert d(packageName = pkgname).wait.exists(timeout = 3000)

    # def testPsensor(self):
    #     '''
    #         Steps:
    #             1. Launch (in setUp)
    #             2. P-sensor enabled/disabled multi-times
    #             3. Exit (in tearDown)
    #     '''
    #     global CASE_NOW
    #     global CYCLE_NOW
    #     CASE_NOW = "testPsensor"
    #     print "%s ...\t"%CASE_NOW,
        d(text = "boxworld").click.wait()
        time.sleep(2)
    #     for i in range(TEST_CYCLE):
    #         CYCLE_NOW = i + 1

    def testSwitchLVRSVR(self):
        global CASE_NOW
        global CYCLE_NOW
        CASE_NOW = "testSwitchLVRSVR"
        print "%s ...\t"%CASE_NOW,
        d(text = "boxworld").click.wait()
        time.sleep(2)
        d.press("home")
        time.sleep(2)
        d(textContains = "LeVR_2016").click.wait()
        time.sleep(2)
        for i in range(500):
            CYCLE_NOW = i + 1
            d.press("recent")
            d(resourceId = 'com.android.systemui:id/leui_recent_thumbnail', instance = 2).click.wait()
            time.sleep(2)
            if i%2 == 0:
                assert d(packageName = 'com.qualcomm.boxworld').wait.exists(timeout = 5000)
            else:
                assert d(packageName = 'com.LeEco.LeVR').wait.exists(timeout = 5000)

    def launchDemo(self):
        if d(resourceId = "android:id/le_bottomsheet_default_confirm").wait.exists(timeout = 5000):
            d(resourceId = "android:id/le_bottomsheet_default_confirm").click.wait()
        # commands.getoutput("adb shell am start -n %s")%pkgname # Launch
        while d(text = 'boxworld').wait.gone(timeout = 2000):
            d.press('home')
            d.swipe(1400,1300,0,1300,5)
        d(text = 'boxworld').click.wait()
        time.sleep(1)
        # assert d(packageName = pkgname).wait.exists(timeout = 3000)

    def exitDemo(self):
        if d(packageName = pkgname).wait.exists(timeout = 3000):
            if d(resourceId = "android:id/le_bottomsheet_default_confirm").wait.exists(timeout = 5000):
                d(resourceId = "android:id/le_bottomsheet_default_confirm").click.wait()
            d.press('recent')
            time.sleep(1)
            # assert d(resourceId = 'com.android.systemui:id/leui_recent_thumbnail').wait.exists(timeout = 3000)
            info_th = d(resourceId = 'com.android.systemui:id/leui_recent_thumbnail', instance = 1).info
            boun_th = info_th['bounds']
            cent_th_y = (boun_th['bottom'] + boun_th['top'])/2
            cent_th_x = (boun_th['right'] + boun_th['left'])/2
            d.swipe(cent_th_x, cent_th_y, cent_th_x, boun_th['top']/2, 5) # Slide up to remove recent task
            d.press('back')

    def randomSwipe(self, half_screen = None):
        deviceInfo = d.info
        w = deviceInfo['displayWidth']
        h = deviceInfo['displayHeight']
        if half_screen != None:
            w = w / 2
        d.swipe(random.randrange(w),random.randrange(100,h),random.randrange(w),random.randrange(100,h),random.randrange(1,20))
        
    def randomPinch(self, method):
        if method == "in":
            d().pinch.In(percent = random.randrange(1,100), steps = random.randrange(1,20))
        elif method == "out":
            d().pinch.Out(percent = random.randrange(1,100), steps = random.randrange(1,20))
