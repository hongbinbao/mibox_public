#!/usr/bin/python
# -*- coding:utf-8 -*- 

import unittest
from uiautomatorplug.android import device as d

class OnlineVideoTest(unittest.TestCase):
    def setUp(self):
        """
        called before  each test method start.
        """
        #a watcher to aviod dialog block test
        d.watcher("AUTO_FC_WHEN_ANR").when(text="稍后升级").click(text="稍后升级")
        d.wakeup()
        for i in xrange(3): d.press('back')
        d.press('home')
        d.press('home')
        for i in xrange(8): d.press('left')

    def tearDown(self):
        """
        called after each test method end or exception occur.
        """
        d.watchers.remove("AUTO_FC_WHEN_ANR")
        for i in xrange(8): d.press('back')
        d.press('home')
        d.press('home') 

    def testPlayOnlineVideo(self):
        """
        launch  app store and exit
        """
        #d.start_activity('--activity-clear-task', component='com.duokan.duokantv/.MainActivity')
        assert d(text="在线影视").exists, 'Online Video icon not found!'
        d(text="在线影视").sibling(className='android.view.View').click.wait()
        #menu_hot_highlight_focus_png =  os.path.join(PIC_DIR, 'menu_hot_highlight_focus.png')
        #menu_hot_highlight_nofocus_png  =  os.path.join(PIC_DIR, 'menu_hot_highlight_nofocus.png')
        #preview_shoucang_png =  os.path.join(PIC_DIR, 'video_preview_sub_shoucang.png')
        #preview_pinglun_png =  os.path.join(PIC_DIR, 'video_preview_sub_pinglun.png')
        if  d.find('menu_hot_highlight_nofocus.png', timeout=30):
            d.press('left')
            d.sleep(3)
            d.press('left')
            d.sleep(3)
            d.press('left')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('enter') 
            d.sleep(5)
            d.press('enter')
        elif  d.find('menu_hot_highlight_focus.png', threshold=0.01, timeout=30) :
            d.press('down')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('enter') 
            d.sleep(5)
            d.press('enter')
        else:
            assert False, 'launch video failed'
        d.expect('video_preview_sub_shoucang.png', threshold=0.05 ,timeout=30)
        d.sleep(2)
        d.press('enter')
        assert d(resourceId='com.duokan.duokantv:id/main_frame').wait.exists(timeout=30000), 'video not start!'
        #assert not d.find('video_preview_sub_shoucang.png', timeout=30), 'video not start!'
        d.sleep(180)
        assert not d(textContains='播放失败').exists or not d(textContains='无法获取视频地址').exists or not d(textContains="正在读取视频信息").exists, 'Video start failed!'
        d.press('back')
        d.expect('video_preview_sub_shoucang.png', threshold=0.05 , timeout=30)
        d.press('back')

    def testPlayOnlineVideoLong(self):
        """
        launch  app store and exit
        """
        #d.start_activity('--activity-clear-task', component='com.duokan.duokantv/.MainActivity')
        assert d(text="在线影视").exists, 'Online Video icon not found!'
        d(text="在线影视").sibling(className='android.view.View').click.wait()
        if  d.find('menu_hot_highlight_nofocus.png', timeout=30):
            d.press('left')
            d.sleep(3)
            d.press('left')
            d.sleep(3)
            d.press('left')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('enter') 
            d.sleep(5)
            d.press('enter')
        elif  d.find('menu_hot_highlight_focus.png', threshold=0.01, timeout=30) :
            d.press('down')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('enter') 
            d.sleep(5)
            d.press('enter')
        else:
            assert False, 'launch video failed' 
        d.expect('video_preview_sub_shoucang.png', threshold=0.05 ,timeout=30)
        d.sleep(2)
        d.press('enter')
        assert d(resourceId='com.duokan.duokantv:id/main_frame').wait.exists(timeout=30000), 'video not start!'
        #assert not d.find('video_preview_sub_shoucang.png', timeout=30), 'video not start!'
        d.sleep(1200)
        assert not d(textContains='播放失败').exists or not d(textContains='无法获取视频地址').exists or not d(textContains="正在读取视频信息").exists, 'Video start failed!'
        d.press('back')
        d.expect('video_preview_sub_shoucang.png', threshold=0.05 , timeout=30)
        d.press('back')

    def testPlayOnlineVideoBack(self):
        """
        launch  app store and exit
        """
        #d.start_activity('--activity-clear-task', component='com.duokan.duokantv/.MainActivity')
        assert d(text="在线影视").exists, 'Online Video icon not found!'
        d(text="在线影视").sibling(className='android.view.View').click.wait()
        #menu_hot_highlight_focus_png =  os.path.join(PIC_DIR, 'menu_hot_highlight_focus.png')
        #menu_hot_highlight_nofocus_png  =  os.path.join(PIC_DIR, 'menu_hot_highlight_nofocus.png')
        #preview_shoucang_png =  os.path.join(PIC_DIR, 'video_preview_sub_shoucang.png')
        #preview_pinglun_png =  os.path.join(PIC_DIR, 'video_preview_sub_pinglun.png')
        if  d.find('menu_hot_highlight_focus.png', threshold=0.01, timeout=30) :
            d.press('down')
            d.sleep(2)
            d.press('enter') 
        elif  d.find('menu_hot_highlight_nofocus.png', timeout=30):
            d.press('enter')
        else:
            assert False, 'launch video failed'  
        d.expect('video_preview_sub_shoucang.png', threshold=0.05 ,timeout=30)
        d.sleep(2)
        d.press('enter')
        assert d(resourceId='com.duokan.duokantv:id/main_frame').wait.exists(timeout=30000), 'video not start!'
        #assert not d.find('video_preview_sub_shoucang.png', timeout=30), 'video not start!'
        d.sleep(120)
        assert not d(textContains='播放失败').exists or not d(textContains='无法获取视频地址').exists or not d(textContains="正在读取视频信息").exists, 'Video start failed!'
        d.press('back')
        d.expect('video_preview_sub_shoucang.png', threshold=0.05 , timeout=30)
        d.press('back')

    def testPlayOnlineVideoLongBACK(self):
        """
        launch  app store and exit
        """
        #d.start_activity('--activity-clear-task', component='com.duokan.duokantv/.MainActivity')
        assert d(text="在线影视").exists, 'Online Video icon not found!'
        d(text="在线影视").sibling(className='android.view.View').click.wait()
        #menu_hot_highlight_focus_png =  os.path.join(PIC_DIR, 'menu_hot_highlight_focus.png')
        #menu_hot_highlight_nofocus_png  =  os.path.join(PIC_DIR, 'menu_hot_highlight_nofocus.png')
        #preview_shoucang_png =  os.path.join(PIC_DIR, 'video_preview_sub_shoucang.png')
        #preview_pinglun_png =  os.path.join(PIC_DIR, 'video_preview_sub_pinglun.png')
        if  d.find('menu_hot_highlight_focus.png', threshold=0.01, timeout=30) :
            d.press('down')
            d.sleep(2)
            d.press('enter') 
        elif  d.find('menu_hot_highlight_nofocus.png', timeout=30):
            d.press('enter')
        else:
            assert False, 'launch video failed'  
        d.expect('video_preview_sub_shoucang.png', threshold=0.05 ,timeout=30)
        d.sleep(2)
        d.press('enter')
        assert d(resourceId='com.duokan.duokantv:id/main_frame').wait.exists(timeout=30000), 'video not start!'
        #assert not d.find('video_preview_sub_shoucang.png', timeout=30), 'video not start!'
        d.sleep(1200)
        assert not d(textContains='播放失败').exists or not d(textContains='无法获取视频地址').exists or not d(textContains="正在读取视频信息").exists, 'Video start failed!'
        d.press('back')
        d.expect('video_preview_sub_shoucang.png', threshold=0.05 , timeout=30)
        d.press('back')

    def testPlayVideoBetweenApp_short(self):
        """
        Suma: play a video
        Step1: click  " video online" 
        Step2: verify the new screen was luanched successfully
        Step3: click the top video
        Step4: verify the new screen was luanched successfully
        Step4: click "play  icon"  to play the video.
        Step5: 
        """
        #APP1 VST
        d.start_activity('--activity-clear-task', component='net.myvst.v2/.component.activity.homepage.LancherActivity')
        assert d(text="最新推荐").wait.exists(timeout=30000), "最新推荐 not found on screen"
        d.press('right')
        d.sleep(2)
        d.press('enter') 
        assert d(text="收藏").wait.exists(timeout=15000), "收藏 not found on screen"
        d.press('enter')
        d.sleep(120)
        d.press('back')
        d.press('back')
        d.sleep(5)
        d.press('back') 
        assert d(text="最新推荐").wait.exists(timeout=15000), "最新推荐 not found on screen"
        d.press('back')
        d.sleep(2)
        d.press('enter')
        ##return to home
        d.sleep(3)
        #enter APP2
        APP2 = '优酷'
        ###for i in xrange(8):
         ###   d.press('right')
        ###assert d(text=APP2 ).wait.exists(timeout=3000), "优酷 not found on screen"     
        ###d(text=APP2).click.wait()
        d.start_activity('--activity-clear-task', component="com.youku.tv/.WelcomeActivity")
        assert d(text="首页").wait.exists(timeout=20000), " 首页 not found on screen"
        d(text="首页").click.wait() 
        d.press('down')
        d.sleep(2)
        d.press('right') 
        d.sleep(2)
        d.press('enter') 
        assert d(text="收藏").wait.exists(timeout=15000), "收藏 not found on screen"
        d.press('enter')
        d.sleep(120)
        d.press('back')
        #assert d(text='确定').wait.exists(timeout=5000), "结束观看 not found on screen" 
        #d(text='确定').click.wait()
        d.press('enter')
        d.sleep(5)
        assert d(text='收藏').wait.exists(timeout=15000), "收藏 not found on screen" 
        d.press('back')
        assert d(text='首页').wait.exists(timeout=15000), "首页 not found on screen" 
        d.press('back')
        d.press('back')

        ##return to home
        d.sleep(3)
        #APP3 = '搜狐视频TV版'
        d.start_activity('--activity-clear-task', component='com.sohutv.tv/.activity.WelcomeActivity')
        assert d(text="推荐").wait.exists(timeout=20000), " 推荐 not found on screen"
        d.press('enter')
        d.sleep(120)
        d.press('back')
        d.sleep(3)
        d.press('back')
        d.sleep(2)
        d.press('left')
        d.sleep(2)
        d.press('enter')
