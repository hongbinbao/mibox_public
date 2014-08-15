#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from uiautomatorplug.android import device as d

class GameCenterTest(unittest.TestCase):
    def setUp(self):
        """
        called before  each test method start.
        """
        #super(VideoPlay, self).setUp()
        #d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") .press.back.home()
        d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="强行关闭") .click(text="确定")
        d.wakeup()
        d.press('home')
        d.press('home')
        for i in xrange(8): d.press('left')
        self.before_install = d.server.adb.cmd('shell pm list package -3').communicate()[0].split()

    def testInstallAndUninstallGame(self):
        """
        launch  app store and exit
       """
        assert d(text="游戏中心").exists, 'Game Center icon not found!'
        d(text="游戏中心").sibling(className='android.view.View').click.wait()
        assert d(className='android.widget.FrameLayout').child(text="推荐").wait.exists(timeout=10000), 'Launch Game Center failed!'
        d.sleep(5)
        d.press('left')
        d.sleep(2)
        d.press('left')
        d.sleep(2)
        d.press('left')
        d.sleep(2)
        d.press('down')
        d.sleep(2)
        d.press('enter')
        d.sleep(3)
        if d(className='android.widget.Button', text='启 动').wait.exists(timeout=5000):
            self.after_install = d.server.adb.cmd('shell pm list package -3').communicate()[0].split()
            del_apk = [i.split('=')[1] for i in self.after_install if i not in self.before_install]
            for apk in del_apk:
                d.server.adb.cmd('shell pm uninstall %s' % apk)
                d.sleep(3)
            assert d(className='android.widget.Button', text='安 装').wait.exists(timeout=5000), 'uninstall game failed!'
        elif d(className='android.widget.Button', text='安 装').exists:
            d(className='android.widget.Button', text='安 装').click.wait()
            d.sleep(20)
            assert d(className='android.widget.Button', text='启 动').wait.exists(timeout=30000), 'install game failed in 30 seconds!'
            self.after_install = d.server.adb.cmd('shell pm list package -3').communicate()[0].split()
            del_apk = [i.split('=')[1] for i in self.after_install if i not in self.before_install]
            for apk in del_apk:
                d.server.adb.cmd('shell pm uninstall %s' % apk)
                d.sleep(3)
            assert d(className='android.widget.Button', text='安 装').wait.exists(timeout=10000), 'uninstall game failed!'
            d.sleep(3)
        else:
            assert False, 'game preview screen not appear!'
        d.press('back')
        d(className='android.widget.FrameLayout').child(text="推荐").wait.exists(timeout=5000)
        d.press('back') 

    def tearDown(self):
        """
        called after each test method end or exception occur.
        """
        #super(VideoPlay, self).tearDown()
        #d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") .press.back.home()
        self.after_install = d.server.adb.cmd('shell pm list package -3').communicate()[0].split()
        del_apk = [i.split('=')[1] for i in self.after_install if i not in self.before_install]
        for apk in del_apk:
            d.server.adb.cmd('shell pm uninstall %s' % apk)
            d.sleep(3)
        d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") .click(text="确定")
        for i in xrange(6): d.press('back')
        d.press('home')
        d.press('home') 