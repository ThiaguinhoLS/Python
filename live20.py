# -*- coding: utf-8 -*-

from selenium import webdriver

class Google(object):

    def __init__(self, driver):
        self._driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'lst-ib'
        self.btn_search = 'btnK'

    def navigate(self):
        self._driver.get(self.url)

    def search(self, word = ""):
        self._driver.find_element_by_id(self.search_bar).send_keys(word)
        self._driver.find_element_by_name(self.btn_search).click()


driver = webdriver.Firefox()
browser = Google(driver)
browser.navigate()
browser.search("Live de Python")
