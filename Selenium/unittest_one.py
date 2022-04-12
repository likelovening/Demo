#!/usr/bin/evn python
# -*- encoding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class PythonorgSearch(unittest.TestCase):
    def steUp(self):
        self.driver=webdriver.Firefox()
    def tearDown(self):
        self.driver.close()
    #测试用例以Test为开头
    def test_org_python_TestCase(self):
        driver=self.driver
        url_begin="https://wwww.baidu.com"
        driver.get(url_begin)
        self.assertIn("baidu",driver.title)
        elem=driver.find_element_by_xpath("//a[contains(@herf,'url')]")
        elem.send_keys(Keys.BACK_SPACE)
        assert 'hanhan' not in driver.page_source


if __name__ == "__main__":
    unittest.main()



























