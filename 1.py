

import urllib.request
resp = urllib.request.urlopen("http://fanyi.baidu.com/")
html = resp.read()
html = html.decode("utf-8")
print("geturl打印信息：%s"%(resp.geturl()))
print('**********************************************')
print("info打印信息：%s"%(resp.info()))
print('**********************************************')
print("getcode打印信息：%s"%(resp.getcode()))
