#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
from uiautomatorplug.android import device as d
import random

class FMTest(unittest.TestCase):
    def setUp(self):
        """
        called before  each test method start.
        """
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

    def testSwitchSong(self):
        """
        launch  app store and exit
        """
        for i in xrange(8):
            d.press('right')
        assert d(text="网络电台").exists, 'FM app icon not found!'
        d(text="网络电台").click.wait()
        assert d(resourceId='com.xiaomi.mimusic:id/play_btn').wait.exists(timeout=10000), 'Open FM failed!'
        d.sleep(10)
        assert d(resourceId='com.xiaomi.mimusic:id/title').child(className="android.widget.TextView").exists, 'song play screen not found!'
        first_song_name = d(resourceId='com.xiaomi.mimusic:id/title').child(className="android.widget.TextView").info['text']
        d.press('right')
        d.sleep(15)
        assert d(resourceId='com.xiaomi.mimusic:id/title').child(className="android.widget.TextView").exists, 'song play screen not found!'
        second_song_name = d(resourceId='com.xiaomi.mimusic:id/title').child(className="android.widget.TextView").info['text']
        assert not second_song_name == first_song_name, 'switch song failed!'
        d.press('right')
        d.sleep(15)
        assert d(resourceId='com.xiaomi.mimusic:id/title').child(className="android.widget.TextView").exists, 'song play screen not found!'
        third_song_name = d(resourceId='com.xiaomi.mimusic:id/title').child(className="android.widget.TextView").info['text']
        assert not third_song_name == second_song_name, 'switch song failed!'
        d.press('back')
        d.sleep(2)
        d.press('back')