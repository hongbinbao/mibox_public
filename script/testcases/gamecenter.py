#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from uiautomatorplug.android import device as d

class GameCenterTest(unittest.TestCase):
    def setUp(self):
        """
        called before  each test method start.
        """
        d.wakeup()
        for i in xrange(3): d.press('back')
        d.press('home')
        d.press('home')
        for i in xrange(8): d.press('left')
        self.before_install = d.server.adb.cmd('shell pm list package -3').communicate()[0].split()

    def tearDown(self):
        """
        called after each test method end or exception occur.
        """
        self.after_install = d.server.adb.cmd('shell pm list package -3').communicate()[0].split()
        del_apk = [i.split('=')[1] for i in self.after_install if i not in self.before_install]
        for apk in del_apk:
            d.server.adb.cmd('shell pm uninstall %s' % apk)
            d.sleep(3)
        for i in xrange(8): d.press('back')
        d.press('home')
        d.press('home') 

    def testInstallAndUninstallGame(self):
        """
        launch  app store and exit
       """
        assert d(text="游戏中心").exists, 'Game Center icon not found!'
        d(text="游戏中心").sibling(className='android.view.View').click.wait()
        assert d(className='android.widget.FrameLayout').child(text="热门精选").wait.exists(timeout=20000), 'Launch Game Center failed!'
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
        if d(resourceId='com.xiaomi.mibox.gamecenter:id/update', text='打开').wait.exists(timeout=5000):
            #self.after_install = d.server.adb.cmd('shell pm list package -3').communicate()[0].split()
            #del_apk = [i.split('=')[1] for i in self.after_install if i not in self.before_install]
            #for apk in del_apk:
            #    d.server.adb.cmd('shell pm uninstall %s' % apk)
            #    d.sleep(3)
            assert d(resourceId='com.xiaomi.mibox.gamecenter:id/uninstall', text='卸载').wait.exists(timeout=5000), 'uninstall buuton not found!'
            #d(resourceId='com.xiaomi.mibox.gamecenter:id/uninstall', text='卸载').click.wait()
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('enter')
            assert d(text='取消').wait.exists(timeout=5000), 'cancel button not found!'
            d.press('left')
            d.sleep(3)
            d.press('enter')
            assert d(resourceId='com.xiaomi.mibox.gamecenter:id/pop_selector_2').wait.exists(timeout=5000), 'return button not found!'
            d.press('enter')
            assert d(className='android.widget.FrameLayout').child(text="热门精选").wait.exists(timeout=5000), 'game main screen not found!'
        elif d(resourceId='com.xiaomi.mibox.gamecenter:id/app_install_button', text='安装').exists:
            d(resourceId='com.xiaomi.mibox.gamecenter:id/app_install_button', text='安装').click.wait()
            d.sleep(60)
            #assert d(resourceId='com.xiaomi.mibox.gamecenter:id/update', text='打开').wait.exists(timeout=40000), 'install game failed in 30 seconds!'
            assert d(text='打开').wait.exists(timeout=5000), 'install game failed in 30 seconds!'
            d.press('back')
            assert d(className='android.widget.FrameLayout').child(text="热门精选").wait.exists(timeout=5000), 'game main screen not found!'
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
            assert d(resourceId='com.xiaomi.mibox.gamecenter:id/uninstall', text='卸载').wait.exists(timeout=5000), 'uninstall buuton not found!'
            #d(resourceId='com.xiaomi.mibox.gamecenter:id/uninstall', text='卸载').click.wait()
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('enter')
            assert d(text='取消').wait.exists(timeout=5000), 'cancel button not found!'
            d.press('left')
            d.sleep(3)
            d.press('enter')
            assert d(resourceId='com.xiaomi.mibox.gamecenter:id/pop_selector_2').wait.exists(timeout=5000), 'return button not found!'
            d.press('enter')
            assert d(className='android.widget.FrameLayout').child(text="热门精选").wait.exists(timeout=5000), 'game main screen not found!'
            #self.after_install = d.server.adb.cmd('shell pm list package -3').communicate()[0].split()
            #del_apk = [i.split('=')[1] for i in self.after_install if i not in self.before_install]
            #for apk in del_apk:
            #    d.server.adb.cmd('shell pm uninstall %s' % apk)
            #    d.sleep(3)
        else:
            assert False, 'game preview screen not appear!'
        d.press('back')