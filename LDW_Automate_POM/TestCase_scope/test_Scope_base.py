#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
"""
_author_='Jianing'
_date_=21/10/20
_data_='初始化角色权限功能，创建新的角色并赋予全部权限'
order=01
"""
import sys
sys.path.append('/root/.jenkins/workspace/selenium')
from LDW_Automate_POM.pages.element_Aloginpage import login_LDW_new
from selenium.webdriver.chrome.options import Options
from LDW_Automate_POM.pages.element_scope import Page_scope
from selenium import webdriver
import pytest
class Test_scope():
    LDW_new_url=None
    LDW_new_name = "ceshi123"
    LDW_new_psw = "123456A@"
    @pytest.fixture(scope='function', autouse=True)
    def begin(self):
        chrome_options=Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("window-size=1920x1080")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=chrome_options)
        #self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
    def test_scope_base(self):
        #实例化登陆
       loginin_LDW_new= login_LDW_new(self.driver,self.LDW_new_url)
       loginin_LDW_new.login_ldw_new(self.LDW_new_name,self.LDW_new_psw)
        #实例化新增唯一权限
       scope_fix=Page_scope(self.driver,self.LDW_new_url)
       scope_fix.change_scope_rulename()








