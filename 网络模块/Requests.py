#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
import requests
# url_login="http://httpbin.org/"
# r=requests.get(url_login)
# r=requests.post(url_login)
#requests返回状态码：
"""
100: ('continue',),
101: ('switching_protocols',),
102: ('processing',),
103: ('checkpoint',),
122: ('uri_too_long', 'request_uri_too_long'),
200: ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\o/', '✓'),
201: ('created',),
202: ('accepted',),
203: ('non_authoritative_info', 'non_authoritative_information'),
204: ('no_content',),
205: ('reset_content', 'reset'),
206: ('partial_content', 'partial'),
207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
208: ('already_reported',),
226: ('im_used',),

Redirection.
300: ('multiple_choices',),
301: ('moved_permanently', 'moved', '\o-'),
302: ('found',),
303: ('see_other', 'other'),
304: ('not_modified',),
305: ('use_proxy',),
306: ('switch_proxy',),
307: ('temporary_redirect', 'temporary_moved', 'temporary'),
308: ('permanent_redirect',
'resume_incomplete', 'resume',), # These 2 to be removed in 3.0

Client Error.
400: ('bad_request', 'bad'),
401: ('unauthorized',),
402: ('payment_required', 'payment'),
403: ('forbidden',),
404: ('not_found', '-o-'),
405: ('method_not_allowed', 'not_allowed'),
406: ('not_acceptable',),
407: ('proxy_authentication_required', 'proxy_auth', 'proxy_authentication'),
408: ('request_timeout', 'timeout'),
409: ('conflict',),
410: ('gone',),
411: ('length_required',),
412: ('precondition_failed', 'precondition'),
413: ('request_entity_too_large',),
414: ('request_uri_too_large',),
415: ('unsupported_media_type', 'unsupported_media', 'media_type'),
416: ('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable'),
417: ('expectation_failed',),
418: ('im_a_teapot', 'teapot', 'i_am_a_teapot'),
421: ('misdirected_request',),
422: ('unprocessable_entity', 'unprocessable'),
423: ('locked',),
424: ('failed_dependency', 'dependency'),
425: ('unordered_collection', 'unordered'),
426: ('upgrade_required', 'upgrade'),
428: ('precondition_required', 'precondition'),
429: ('too_many_requests', 'too_many'),
431: ('header_fields_too_large', 'fields_too_large'),
444: ('no_response', 'none'),
449: ('retry_with', 'retry'),
450: ('blocked_by_windows_parental_controls', 'parental_controls'),
451: ('unavailable_for_legal_reasons', 'legal_reasons'),
499: ('client_closed_request',),

Server Error.
500: ('internal_server_error', 'server_error', '/o\', '✗'),
501: ('not_implemented',),
502: ('bad_gateway',),
503: ('service_unavailable', 'unavailable'),
504: ('gateway_timeout',),
505: ('http_version_not_supported', 'http_version'),
506: ('variant_also_negotiates',),
507: ('insufficient_storage',),
509: ('bandwidth_limit_exceeded', 'bandwidth'),
510: ('not_extended',),
511: ('network_authentication_required', 'network_auth', 'network_authentication'),
"""
#?+键值配对，get传递参数（params传递参数）
response1=requests.get("http://httpbin.org/get")
print(response1.url)

params1={"key1":"vaule1",
                "key2":"value2"}
response2=requests.get("http://httpbin.org/",params=params1)
print(response2.url)

params2={"key1":"value1",
         "key2":["value1","value2"]}
response3=requests.get("http://httpbin.org/",params=params2)
print(response3.url) #链接
print(response3.encoding)  #utf-8
# print(response3.text)  #Json格式
print(type(response3.content))  #<class 'bytes'>
# print(response3.json())   #json数据
print(response3.status_code)     #200；状态码
print(response3.raise_for_status())  #none


#headers部署头文件
import requests
new_headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)"
                          " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
response4=requests.get("https://zhihu.com",headers=new_headers)
print(response4.text)


"----------------------------------------------------------"
#Post请求  要有payload--→data参数

payload={"key1":"vaule1",
                "key2":"value2"}
response5=requests.post("http://httpbin.org/post",data=payload)
print(response5.status_code)

payload1 = (("key1","value1"),("key1","value2"))
response6 = requests.post("http://httpbin.org/post",data = payload1)
print(response6.url)

payload2={"key":["value1","value2"]} #俩个value取最后一个
response6=requests.post("http://httpbin.org/post",data = payload2)
print(response6.history)
print(response6.cookies)

#超时
#指timeout时间内无响应则报错
response7=requests.get("http://www.liangdawang.com",timeout=1)
print(response7)  #200

'''
1、遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。
2、如果 HTTP 请求返回了不成功的状态码， Response.raise_for_status() 会抛出一个 HTTPError 异常。
3、若请求超时，则抛出一个 Timeout 异常。
4、若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。
5、所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 。
'''

# 将CookieJar转为字典：
jar = requests.cookies.RequestsCookieJar()
r=jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
cookies = requests.utils.dict_from_cookiejar(r.cookies)

# 将字典转为CookieJar：
cookie_dict=dict(cookies="dict")
cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)

# 其中cookie_dict是要转换字典
#转换完之后就可以把它赋给cookies
#并传入到session中了：
s = requests.Session()
s.cookies = cookies


#在所有请求保持cookie
session=requests.Session()
session.get("url1")
response8=session.get("url2")
print(response8.text)
























