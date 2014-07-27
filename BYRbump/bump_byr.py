# -*- coding: gbk -*-

#from urllib import urlencode
import cookielib, urllib2,urllib
from config_byr import *
from apscheduler.scheduler import Scheduler  
def bump():
    # cookie
    #获取一个保存cookie的对象
    cj = cookielib.LWPCookieJar()
    #将这个保存cookie的对象，和一个HTTP的cookie的处理器绑定
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    #创建一个opener对象，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
    opener = urllib2.build_opener(cookie_support)
    #"安装"这个opener,安装完以后就可以使用urllib2来操作了
    urllib2.install_opener(opener)

    # Login
    user_data = {
                    'CookieDate':'0',
                    'id': USERNAME,
                    'mode':'1',
                    'passwd': PASSWORD,
                    'kick_multi':'0'
                }
    #将要POST出去的数据进行编码
    url_data = urllib.urlencode(user_data)
    #r = opener.open(url,data)如果没有上面的urllib2.install_opener方法，就必须这样写了
    #创建一个Request对象，同时将url_data作为表单数据发送出去
    req = urllib2.Request(LOGINURL,url_data)
    login_r = urllib2.urlopen(req)#接收反馈的信息
    #print login_r.read()
    #print USERNAME
    # Publish

    TITLE = titledata[random.randrange(0,4)]
    TEXT = textdata[random.randrange(0,4)]
    article_data={
                    'title':TITLE,
                    'text':TEXT
                 }
    data=urllib.urlencode(article_data)
    #postpage = opener.open("http://bbs.byr.cn/classic/bbssnd.php?board=Ad_Agent&reid=935486")
    #print postpage.read()
    #publish_data=urlencode(article_data)
    publish_article=opener.open("http://bbs.byr.cn/classic/bbssnd.php?board=Ad_Agent&reid=935486",data)
    #print publish_article.read()

if __name__ == '__main__':  
    #hello = 'hello world'  
    sched = Scheduler(daemonic=False) # 注意这里，要设置 daemonic=False  
    sched.add_cron_job(bump, day_of_week='mon-sun', hour='8,10,11,16,17,20,22') # args=[] 用来给job函数传递参数  
    sched.start()  
