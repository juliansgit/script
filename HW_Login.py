#coding=utf-8
import os
import time
from selenium import webdriver
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

#配置设备和应用信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.nantian.ydyw'
desired_caps['appActivity'] = 'com.nantian.ydyw.CordovaApp'
desired_caps['udid'] = 'F7R6R14315001200'
desired_caps['noReset'] = 'false'
desired_caps['unicodeKeyboard'] = 'false'
desired_caps['newCommandTimeout'] = '6000'

#连接设备
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)

#点击确认root按钮
el1 = driver.find_element_by_id("android:id/button1")
el1.click()
time.sleep(5)
#
TouchAction(driver).press(x=1063, y=172).move_to(x=0, y=0).release().perform()
time.sleep(3)
el2 = driver.find_element_by_accessibility_id("我的")
el2.click()
time.sleep(3)
el3 = driver.find_element_by_xpath("(//android.view.View[@content-desc=\"登录\"])[1]/android.view.View[2]/android.widget.EditText")
el3.send_keys("zhwangl")
time.sleep(1)
el4 = driver.find_element_by_xpath("(//android.view.View[@content-desc=\"登录\"])[1]/android.view.View[3]/android.view.View")
el4.send_keys("123456qwe")
time.sleep(1)
el5 = driver.find_element_by_xpath("(//android.view.View[@content-desc=\"登录\"])[2]")
el5.click()
time.sleep(1)






