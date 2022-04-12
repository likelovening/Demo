#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Firefox()
select=Select(driver.find_element_by_name('name'))
select.select_by_index(index="index")
select.select_by_visible_text('test')
select.select_by_value(value='value')


















