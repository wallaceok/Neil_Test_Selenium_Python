#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 09
"""

from selenium_test import webdriver
import time

url = "http://list.taobao.com/itemlist/default.htm?cat=50000671&viewIndex=1&as=0&atype=b&style=grid&same_info=1&isnew=2&tid=0&_input_charset=utf-8"

browser = webdriver.Chrome()
browser.get(url)
time.sleep(5)
browser.maximize_window()

js1 = "return document.documentElement.scrollHeight;"  # 滑动条的位置值
js2 = "scroll(0,10000);"  # 滑动滚动条到页面底
scroll_height = 0

while scroll_height < 10200:
    browser.execute_script(js2)
    time.sleep(3)
    scroll_height = browser.execute_script(js1)

time.sleep(3)
parent_ele = browser.find_element_by_css_selector("a.J_Ajax.btn.next")  # 先查找父元素
parent_ele.find_element_by_tag_name("span")  # 再找子元素
#browser.find_element_by_xpath("a[@class='J_Ajax btn next']").click()

browser.quit()

13313875128