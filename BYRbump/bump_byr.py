# -*- coding: gbk -*-

#from urllib import urlencode
import cookielib, urllib2,urllib
from config_byr import *
from apscheduler.scheduler import Scheduler  
def bump():
    # cookie
    #��ȡһ������cookie�Ķ���
    cj = cookielib.LWPCookieJar()
    #���������cookie�Ķ��󣬺�һ��HTTP��cookie�Ĵ�������
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    #����һ��opener���󣬽�������cookie��http����������������һ��handler���ڴ���http��URL�Ĵ�
    opener = urllib2.build_opener(cookie_support)
    #"��װ"���opener,��װ���Ժ�Ϳ���ʹ��urllib2��������
    urllib2.install_opener(opener)

    # Login
    user_data = {
                    'CookieDate':'0',
                    'id': USERNAME,
                    'mode':'1',
                    'passwd': PASSWORD,
                    'kick_multi':'0'
                }
    #��ҪPOST��ȥ�����ݽ��б���
    url_data = urllib.urlencode(user_data)
    #r = opener.open(url,data)���û�������urllib2.install_opener�������ͱ�������д��
    #����һ��Request����ͬʱ��url_data��Ϊ�����ݷ��ͳ�ȥ
    req = urllib2.Request(LOGINURL,url_data)
    login_r = urllib2.urlopen(req)#���շ�������Ϣ
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
    sched = Scheduler(daemonic=False) # ע�����Ҫ���� daemonic=False  
    sched.add_cron_job(bump, day_of_week='mon-sun', hour='8,10,11,16,17,20,22') # args=[] ������job�������ݲ���  
    sched.start()  
