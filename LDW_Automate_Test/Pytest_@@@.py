#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
"""
_author_='Jianing'
_date_=21/12/15
_data_='pytest中装饰器'
"""
import pytest
#参数化---parametrize
@pytest.mark.parametrize('x',[(1),(2)])
def test_Para(x):    #下方参数必须使用x
    assert x==x

#测试顺序---ordering
@pytest.mark.run(order=1)   #按照数字小→大的顺序执行==1，2，3，无标记，-3，-2，-1
def test_ord():
    assert 0==1

#跳过测试----skip
@pytest.mark.skip(reason='')
def test_add(a):
    assert a==1

#预期失败的函数----xfail
@pytest.mark.xfail()
def test_xfail(a):
    assert a==1

#失败重跑----rerunfailure    安装插件，运行中使用--rerun n
@pytest.mark.flaky(reruns=3)
def test_rerunfailure():
    assert 1==1















