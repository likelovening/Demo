#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  # 导入鼠标滑动，点击等库
from xpinyin import Pinyin
class org_jizhou(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def test_jizhou_build(self):
        driver=self.driver
        # 设置全局响应时间
        driver.implicitly_wait(10)
        # 设置最大屏幕尺寸打开
        driver.maximize_window()
        driver.get("http://test.liangdawang.com:8085/portal/")
        print("业务员登陆中....")
        # xpath寻找“请登录”按钮
        driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div/div[1]/span/span[2]/a[1]").click()
        time.sleep(1)
        # xpath寻找账户框，并输入
        driver.find_element_by_class_name("ant-input").send_keys("ldwywy")
        time.sleep(1)
        # xpath寻找密码框，并输入
        driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").send_keys("123456")
        # xpath点击登陆按钮
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/button").click()
        time.sleep(1)
        print("业务员登陆成功")
        # 点击我得粮达
        driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[2]/ul/li[2]/a').click()
        time.sleep(1)
        new_window = driver.window_handles
        driver.switch_to.window(new_window[1])
        # 选择我得粮达
        driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[1]/a').click()
        # 选择寄售报告填写
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/dl/dd[1]/ul/li[1]/a').click()
        print("寄售可行性报告填写中...")
        # 点击委托方信息公司并选择
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[1]/div[2]/div[1]/a/span[1]').click()
        # 选择某一家公司
        elem = driver.find_element_by_xpath('/html/body/div[9]/ul/li[17]/div')
        Title1 = ("%s：自动化可行性报告"%elem.text)
        #print("客户名称：",elem.text)
        ActionChains(driver).move_to_element(elem).click().perform()
        # 选择品名
        chose_yumi = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[4]/div[2]/ul/li[1]')
        chose_yumi1 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[4]/div[2]/ul/li[1]/p/a')
        ActionChains(driver).move_to_element(chose_yumi).click(chose_yumi1).perform()
        # 填写数量
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[6]/input").send_keys("2000")
        # 滚动滑动条
        ActionChains(driver).key_down(Keys.DOWN).perform()
        # 选择年份
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[8]/select').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[8]/select/option[2]').click()
        # 滚动滑动条
        ActionChains(driver).key_down(Keys.DOWN).perform()
        # 填写产地
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[11]/div[1]/div[1]/div').click()
        time.sleep(0.5)
        Chandi = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[11]/div[1]/div[2]/div/div[2]/ul/li[10]/a')
        ActionChains(driver).move_to_element(Chandi).click().perform()
        # 滚动滑动条
        ActionChains(driver).key_down(Keys.DOWN).perform()
        # 填写单价
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[13]/input').send_keys('1400')
        # 价格类型
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[14]/select').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[14]/select/option[2]').click()
        # 滚动滑动条
        ActionChains(driver).key_down(Keys.DOWN).perform()
        # 自办理完毕
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[16]/select').click()
        time.sleep(0.5)
        Huoquan = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[16]/select/option[1]')
        ActionChains(driver).move_to_element(Huoquan).click().perform()
        # 滚动滑动条到填写交易信息界面
        elem1 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[25]/textarea')
        driver.execute_script("arguments[0].scrollIntoView();", elem1)
        # 选择交易类型
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[3]/p/span/input[2]').click()
        # 选择天数
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[5]/select[1]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[5]/select[1]/option[3]').click()
        # 选择操作服务费
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[8]/input').clear()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[8]/input').send_keys(2)
        # 滚动滑动条
        ActionChains(driver).key_down(Keys.DOWN).perform()
        #确认标题
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[2]/input[3]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[2]/input[1]').clear()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[2]/input[1]').send_keys(Title1)
        # 保证金比例
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[11]/input').send_keys(10)
        # 选择运输方式
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[12]/select').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[12]/select/option[2]').click()
        # 滚动滑动条
        ActionChains(driver).key_down(Keys.DOWN).perform()
        # 选择大区
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[5]/div[4]/select').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[5]/div[4]/select/option[4]').click()
        # 发起人大区
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[5]/div[3]/select').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[5]/div[3]/select/option[4]').click()
        # 滚动滑动条
        time.sleep(0.5)
        ActionChains(driver).key_down(Keys.DOWN).perform()
        # 到达大区
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[5]/div[5]/select').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[5]/div[5]/select/option[4]').click()
        # 发布&确认
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[6]/input[2]').click()
        time.sleep(2)
        #点击提交
        driver.find_element_by_class_name('szBut').click()
        time.sleep(2)
        #点击确认
        driver.find_element_by_class_name('ui-dialog-button-orange').click()
        #assert "可行性报告操作成功" in driver.page_source
        record1= driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/h1')
        Equal1=record1.text
        self.assertEqual(Equal1,"可行性报告操作成功",'可行性报告创建失败')
        print("可行性报告创建成功")
        #返回可行性报告管理
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/h3/a').click()
        #查看审批人
        time.sleep(3)
        print("获取审批人中...")
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/span[4]/span').click()
        BpmRen=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/span[4]/div/table/tbody/tr/td[2]')
        BpmMZ=BpmRen.text
        print("审批人:",BpmMZ)
        p=Pinyin()
        useN=p.get_pinyin(BpmMZ, '')
        pws="123456"
        #打开Bpm审批界面,新界面
        js="window.open('http://113.105.116.65:8066/bas/page/login/login.html')"
        driver.execute_script(js)
        #记录当前句柄
        bpm_windows=driver.window_handles
        driver.switch_to.window(bpm_windows[-1])
        #输入审批人账户密码并登陆
        print("进入BPM审批界面中...")
        driver.find_element_by_xpath('/html/body/div/form/div/p[1]/input').clear()
        driver.find_element_by_xpath('/html/body/div/form/div/p[1]/input').send_keys(useN)
        driver.find_element_by_xpath('/html/body/div/form/div/p[2]/input').clear()
        driver.find_element_by_xpath('/html/body/div/form/div/p[2]/input').send_keys(pws)
        driver.find_element_by_xpath('/html/body/div/form/div/div[1]/a').click()
        #选择审批项
        driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[1]/a/div/div').click()
        driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[1]/div[2]/a[1]/div').click()
        #确认标题是否一致
        BpmTitle=driver.find_element_by_xpath('/html/body/ul[1]/a/li/span/p[1]/span').text
        if BpmTitle==Title1:
            print("寻找审批项成功")
        else:
            print("审批项有误")

        #选择需审批项
        driver.find_element_by_xpath('/html/body/ul[1]/a').click()
        time.sleep(0.5)
        #提交审批
        driver.find_element_by_xpath('/html/body/div/div[4]/div[3]/a').click()
        driver.find_element_by_xpath('/html/body/div/div[2]/button[1]').click()
        driver.find_element_by_xpath('/html/body/div/div[4]/button').click()
        #审批弹窗处理
        alert1=driver.switch_to.alert
        alert1.accept()
        print('可行性报告审批完成')
        #确认是这个报告
        driver.switch_to.window(bpm_windows[1])
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/a[1]').click()  #刷新报告状态
        time.sleep(1)
        Title2=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[1]/div/div[1]/a[1]").text
        print("可行性报告名称：",Title2)
        self.assertEqual(Title2, Title1, '不是这个可行性报告')
        #确认报告状态
        BaogaoZT=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[4]/span').text
        self.assertEqual(BaogaoZT,'物流方案待补充','报告状态有误')
        print("确认可行性报告审批成功")
        #切换账户
        time.sleep(1)
        wuliuyuan=driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li/a/span')
        out1=driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li/div/p/a')
        ActionChains(driver).move_to_element(wuliuyuan).click(out1).perform()
        #登陆物流员
        print("切换物流员登陆中....")
        driver.find_element_by_class_name("ant-input").clear()
        driver.find_element_by_class_name("ant-input").send_keys("ldwwly")
        time.sleep(1)
        # xpath寻找密码框，并输入
        driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").clear()
        driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").send_keys("123456")
        # xpath点击登陆按钮
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/button").click()
        # 点击我得粮达
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[2]/ul/li[2]/a').click()
        time.sleep(1)
        new_window2= driver.window_handles
        driver.switch_to.window(new_window2[-1])
        print("物流员登陆完成")
        # 选择我得粮达
        driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[1]/a').click()
        #选择可行性报告管理
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/dl/dd[1]/ul/li[2]/a').click()
        #核对报告名称
        time.sleep(1)
        WLMC=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[1]/div/div[1]/a[1]').text
        self.assertEqual(WLMC,Title1,"物流：可行性报告选择有误")
        #补充物流信息
        print("寻找可行性报告并添加物流信息中....")
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[5]/div/a').click()
        new_window3= driver.window_handles
        driver.switch_to.window(new_window3[-1])
        #物流方案填写
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[1]/div[2]/select').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[1]/div[2]/select/option[3]').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[1]/div[3]/input').send_keys('测试1')
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[1]/div[5]/input').send_keys('测试2')
        #物流方案保存
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/input[2]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div/div/div[2]/a').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/div[2]/div[1]/a').click()
        #校验是否物流方案是否提交成功
        WLFA=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/h1').text
        self.assertEqual(WLFA,"物流信息操作成功","物流信息填写有误")
        print("物流方案填写成功")
        #返回可行性报告列表界面
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/h3/a').click()
        #查看物流信息审批人
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/span[4]/span').click()
        WLBpmRY=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/span[4]/div/table/tbody/tr[1]/td[2]').text
        useW = p.get_pinyin(WLBpmRY, '')
        print('物流审批人为：%s'%WLBpmRY)
        #跳转BPM界面
        print("跳转BPM审批中....")
        driver.switch_to.window(bpm_windows[-1])
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[1]/span[1]/a/img').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[1]/span[1]/a/img').click()
        #弹框确认
        alert2=driver.switch_to.alert
        alert2.accept()
        #BPM账户输入切换
        driver.find_element_by_xpath('/html/body/div/form/div/p[1]/input').clear()
        driver.find_element_by_xpath('/html/body/div/form/div/p[1]/input').send_keys(useW)
        driver.find_element_by_xpath('/html/body/div/form/div/p[2]/input').clear()
        driver.find_element_by_xpath('/html/body/div/form/div/p[2]/input').send_keys(pws)
        #点击登陆
        driver.find_element_by_xpath('/html/body/div/form/div/div[1]/a').click()
        print("BPM切换用户登陆完成")
        # 选择审批项
        driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[1]/a/div/div').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[2]/div[2]/a[1]/div').click()
        # 确认标题是否一致
        BpmTitle2= driver.find_element_by_xpath('/html/body/ul[1]/a[1]/li/span/p[1]/span').text
        if BpmTitle2== Title1:
            pass
        else:
            print("审批项有误")
        print("确认审批项....")
        # 选择需审批项
        driver.find_element_by_xpath('/html/body/ul[1]/a[1]/li/span/p[3]').click()
        time.sleep(0.5)
        # 提交审批
        driver.find_element_by_xpath('/html/body/div/div[4]/div[3]/a/span').click()
        driver.find_element_by_xpath('/html/body/div/div[2]/button[1]').click()
        driver.find_element_by_xpath('/html/body/div/div[4]/button').click()
        # 审批弹窗处理
        alert3= driver.switch_to.alert
        alert3.accept()
        print('物理方案审批完成')
        #切换界面
        new_window4=driver.window_handles
        driver.switch_to.window(new_window4[-1])
        #刷新可行性报告状态
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/a[1]').click()
        time.sleep(1)
        WLZT=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[4]/span').text
        self.assertEqual(WLZT,"可行性报告待提交","物流审批有误")
        print("确认物流方案审批成功")
        #切换交易员账户
        time.sleep(1)
        JYY=driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li/a/span')
        out1=driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li/div/p/a')
        ActionChains(driver).move_to_element(JYY).click(out1).perform()
        #登陆交易员
        print("切换交易员登陆中....")
        driver.find_element_by_class_name("ant-input").clear()
        driver.find_element_by_class_name("ant-input").send_keys("ldwjyy")
        time.sleep(1)
        # xpath寻找密码框，并输入
        driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").clear()
        driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").send_keys(pws)
        # xpath点击登陆按钮
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/button").click()
        # 点击我得粮达
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[2]/ul/li[2]/a').click()
        time.sleep(1)
        new_window5= driver.window_handles
        driver.switch_to.window(new_window5[-1])
        print("交易员登陆完成")
        #进入可行性报告列表界面
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/dl/dd[1]/ul/li[6]/a').click()
        new_window6 = driver.window_handles
        driver.switch_to.window(new_window6[-1])
        time.sleep(1)
        #选择全部可行性报告
        print("可行性报告查询中...")
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[1]/a/span[1]').click()
        driver.find_element_by_xpath('/html/body/div[8]/ul/li[2]/div').click()
        time.sleep(0.5)
        #确认可行性报告名称
        JYname=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[1]/div/div[1]/a[1]').text
        self.assertEqual(JYname,Title1,"可行性报告选择错误")
        print("可行性报告选择成功")
        #签署框架协议
        print("签章框架协议中....")
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[5]/div/a[1]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[9]/div/table/tbody/tr[2]/td/div/div/div[1]/label[1]/input').click()
        #选择框架合同
        driver.find_element_by_xpath('/html/body/div[9]/div/table/tbody/tr[2]/td/div/div/div[2]/div/a/span[1]').click()
        driver.find_element_by_xpath('/html/body/div[11]/ul/li[2]/div').click()
        driver.find_element_by_xpath('/html/body/div[8]/div/table/tbody/tr[2]/td/div/div/div[6]/a').click()
        time.sleep(0.5)
        #弹框确认
        driver.find_element_by_xpath('/html/body/div[12]/div[2]/div/div[2]/div[2]/div[1]/a').click()
        print('框架协助签署完成')
        #提交审批
        print('提交审批中....')
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[5]/div/a[2]').click()
        #弹框确认
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[10]/div/table/tbody/tr[2]/td/div/div/div[3]/a').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[12]/div[2]/div/div[2]/div[2]/div[1]/a').click()
        time.sleep(0.5)
        JYZT=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[4]/span').text
        self.assertEqual(JYZT,"领导待审",'可行性报告状态有误，未提交审批')
        print('提交审批成功')
        #查询审批人
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/span[4]/span').click()
        JYSP=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/span[4]/div/table/tbody/tr/td[2]').text
        useJ=p.get_pinyin(JYSP, '')
        print("获取审批人为：%s"%JYSP)
        #切换BPM审批界面
        print("跳转BPM审批中....")
        driver.switch_to.window(bpm_windows[-1])
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[1]/span[1]/a/img').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[1]/span[1]/a/img').click()
        # 弹框确认
        alert2 = driver.switch_to.alert
        alert2.accept()
        # BPM账户输入切换
        driver.find_element_by_xpath('/html/body/div/form/div/p[1]/input').clear()
        driver.find_element_by_xpath('/html/body/div/form/div/p[1]/input').send_keys(useJ)
        driver.find_element_by_xpath('/html/body/div/form/div/p[2]/input').clear()
        driver.find_element_by_xpath('/html/body/div/form/div/p[2]/input').send_keys(pws)
        # 点击登陆
        driver.find_element_by_xpath('/html/body/div/form/div/div[1]/a').click()
        print("BPM切换用户登陆完成")
        # 选择审批项
        driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[1]/a/div/div').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[3]/div[2]/a[1]/div').click()
        # 确认标题是否一致
        BpmTitle3 = driver.find_element_by_xpath('/html/body/ul[1]/a/li/span/p[1]/span').text
        if BpmTitle3 == Title1:
            pass
        else:
            print("审批项有误")
        print("确认审批项完成")
        #进入审批项
        driver.find_element_by_xpath('/html/body/ul[1]/a/li/span/p[2]/span[1]').click()
        #审批处理
        driver.find_element_by_xpath('/html/body/div/div[4]/div[3]/a/span').click()
        #弹框确认
        driver.find_element_by_xpath('/html/body/div/div[2]/button[1]').click()
        driver.find_element_by_xpath('/html/body/div/div[4]/button').click()
        time.sleep(0.5)
        alert4=driver.switch_to.alert
        alert4.accept()
        print("BPM审批完成")
        #刷新可行性报告状态
        driver.switch_to.window(new_window6[-1])
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/a[1]').click()
        time.sleep(1)
        #确认可行性报告标题
        KXMZ=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[1]/div/div[1]/a[1]').text
        self.assertEqual(KXMZ,Title1,"可行性报告查看有误")
        #状态确认
        KXZT=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[4]/span').text
        self.assertEqual(KXZT,"可行性报告审批通过","可行性报告审批异常")
        print("可行性报告审批通过；流程结束")
    def tearDown(self):
        time.sleep(100)
        self.driver.quit()
if __name__=="__main__":
    unittest.main()





