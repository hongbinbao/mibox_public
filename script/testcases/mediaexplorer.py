#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from uiautomatorplug.android import device as d
import random

def fc_close(device):
    device.press.left()
    device.press.left()
    device.press.left()
    return False


class MediaExplorerTest(unittest.TestCase):
    def setUp(self):
        """
        called before  each test method start.
        """
        #super(MediaExplorerTest, self).setUp()
        #d.watcher("AUTO_FC_WHEN_ANR")#.when(text="ANR").when(text="Wait") .press.back.home()
        #d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="强行关闭") .click(text="确定")
        #d.watcher("AUTO_FC_WHEN_ANR").press.left.left.left.home()
        #d.handlers.on(fc_close)
        d.wakeup()
        for i in xrange(3): d.press('back')
        d.press('home')
        d.press('home')
        for i in xrange(8): d.press('left')

    def tearDown(self):
        """
        called after each test method end or exception occur.
        """
        for i in xrange(8): d.press('back')
        d.press('home')
        d.press('home') 

    def testPlayLocalVideo(self):
        """
        launch  app store and exit
        """
        for i in xrange(5):
            d.press('right')
        assert d(text="高清播放器").exists, 'Media Explorer icon not found!'
        d(text="高清播放器").click.wait()
        assert d(resourceId='com.xiaomi.mitv.mediaexplorer:id/entry_name', text='设备').wait.exists(timeout=5000), 'launch Media Explorer failed!'
        assert d(resourceId='com.xiaomi.mitv.mediaexplorer:id/entry_name', text="视频").wait.exists(timeout=5000), 'launch Media Explorer failed!'
        d.press('right')
        d.sleep(2)
        d.press('right')
        d.sleep(2)
        d.press('down')
        d.sleep(2)
        d.press('enter')
        assert d(resourceId='com.xiaomi.mitv.mediaexplorer:id/device_label', text="移动存储设备").wait.exists(timeout=10000), 'enter Device list screen failed!'
        d.press('enter')
        assert d(className="android.widget.ListView").child(text="视频").wait.exists(timeout=10000), 'enter USB device list failed!'
        d.press('enter')
        assert d(className="android.widget.ListView").child(resourceId="com.xiaomi.mitv.mediaexplorer:id/iv_image").wait.exists(timeout=10000), 'enter USB device video list failed!'
        for i in xrange(16):
            for j in xrange(random.randint(0, 16)):
                d.press('down')
                d.sleep(1)
            for k in xrange(random.randint(0, 8)):
                d.press('up')
                d.sleep(1)
            d.press('enter')
            assert d(className="android.widget.ListView").child(resourceId="com.xiaomi.mitv.mediaexplorer:id/iv_image").wait.gone(timeout=10000), 'start to play video failed!'
            d.sleep(600)
            d.press('back')
            assert d(className="android.widget.ListView").child(resourceId="com.xiaomi.mitv.mediaexplorer:id/iv_image").wait.exists(timeout=10000), 'enter USB device video list failed!'
