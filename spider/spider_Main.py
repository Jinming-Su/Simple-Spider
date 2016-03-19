#coding:utf8
from spider import url_manager, html_downloader, html_outputer, html_parser


class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        
    def craw(self, rootUrl):
        cnt = 1
        self.urls.addNewUrl(rootUrl)
        while self.urls.hasNewUrl():
            try:
                newUrl = self.urls.getNewUrl()
                
                print ('craw %d: %s' % (cnt, newUrl))
                
                htmlContainer = self.downloader.download(newUrl)
                
                newUrls, newData = self.parser.parse(newUrl, htmlContainer)
                self.urls.addNewUrls(newUrls)
                self.outputer.collectData(newData)
                
                if cnt == 50:
                    print 'craw compeletly'
                    break;
                cnt = cnt + 1;
            except Exception as e:
                print e
                print 'craw failed'
                
        self.outputer.outputHtml()    
if __name__ == '__main__':
    rootUrl = 'http://baike.baidu.com/item/%E8%8B%8F%E9%87%91%E6%98%8E'
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)