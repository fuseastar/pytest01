from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 输入中文需要开启的两个参数
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.implicitly_wait(30)
e1 = driver.find_element_by_xpath("//*[contains(@text, 'WLAN')]")
e2 = driver.find_element_by_xpath("//*[contains(@text, '电池')]")
driver.drag_and_drop(e2, e1)
e3 = driver.find_element_by_xpath("//*[contains(@text, '安全')]")
e3.click()
driver.find_element_by_xpath("//*[contains(@text, '屏幕锁定方式')]").click()
driver.find_element_by_xpath("//*[contains(@text, '图案')]").click()

sleep(2)

# 1. 移动元素时，必须按下指定元素或坐标
# 2. move_to()方法能解决多个元素或坐标之间的移动。
# 3. 切记由于硬件配置问题，必须跟着wait(100)及释放操作。
# 4. appium在1.9以上，如果基于坐标滑动，那么就是单独坐标之间的滑动，appium1.9以下，是基于坐标的偏移量滑动
# (偏移量：200,150,x=60,y=-30)

# 241,850 720,850 1198,850
# 720,1334
# 241,1807 720,1807 1200,1807

# move_to(el=None,x=xx,y=yy)
TouchAction(driver).press(x=241,y=850).wait(100).move_to(x=720,y=850).wait(100).\
    move_to(x=1198,y=850).wait(100).move_to(x=720,y=1334).wait(100).move_to(x=241,y=1807).\
    wait(100).move_to(x=720,y=1807).wait(100).move_to(x=1200,y=1807).release().perform()

sleep(3)
driver.quit()
