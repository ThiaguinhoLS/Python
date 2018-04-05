# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup as BS

URL = 'http://google.com'

class Page(object):

    def __init__(self, driver):
        self._driver = driver

driver = webdriver.Firefox()
driver.get(URL)
page = driver.page_source

print(page)
