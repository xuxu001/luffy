# -*- coding:utf-8 -*-
# coding=utf-8
import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://none.h5.xeknow.com/st/34lpxTQWy")
time.sleep(1)


print (driver.current_url) # current_url 方法可以得到当前页面的URL
driver.quit()


def sendTemplateSMS(self, to, datas, tempId):
    self.accAuth()
    nowdate = datetime.datetime.now()
    self.Batch = nowdate.strftime("%Y%m%d%H%M%S")
    # 生成sig
    signature = self.AccountSid + self.AccountToken + self.Batch;
    sig = md5(signature.encode('utf-8')).hexdigest().upper()
    # 拼接URL
    url = "https://" + self.ServerIP + ":" + "%s" % self.ServerPort + "/" + self.SoftVersion + "/Accounts/" + self.AccountSid + "/SMS/TemplateSMS?sig=" + sig
    # 生成auth
    src = self.AccountSid + ":" + self.Batch;
    auth = base64.encodebytes(src.encode()).strip()
    req = urllib.request.Request(url)
    self.setHttpHeader(req)
    req.add_header("Authorization", auth)
    # 创建包体
    b = ''
    for a in datas:
        b += '<data>%s</data>' % (a)

    body = '<?xml version="1.0" encoding="utf-8"?><TemplateSMS><datas>' + b + '</datas><to>%s</to><templateId>%s</templateId><appId>%s</appId>\
            </TemplateSMS>\
            ' % (to, tempId, self.AppId)
    if self.BodyType == 'json':
        # if this model is Json ..then do next code
        b = '['
        for a in datas:
            b += '"%s",' % (a)
        b += ']'
        body = '''{"to": "%s", "datas": %s, "templateId": "%s", "appId": "%s"}''' % (to, b, tempId, self.AppId)
    req.data = body.encode('utf-8')
    data = ''
    try:
        res = urllib.request.urlopen(req);
        data = res.read()
        res.close()

        if self.BodyType == 'json':
            # json格式
            locations = json.loads(data)
        else:
            # xml格式
            xtj = xmltojson()
            locations = xtj.main(data)
        if self.Iflog:
            self.log(url, body, data)
        return locations
    except Exception as error:
        if self.Iflog:
            self.log(url, body, data)
        return {'172001': '网络错误'}

