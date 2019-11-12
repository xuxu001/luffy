# -*- coding:utf-8 -*-
# coding=utf-8
import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://none.h5.xeknow.com/st/34lpxTQWy")
time.sleep(1)


print (driver.current_url) # current_url 方法可以得到当前页面的URL
driver.quit()