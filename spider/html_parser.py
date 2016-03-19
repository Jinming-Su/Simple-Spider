#coding:utf8

from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    
    
    def _getNewUrls(self, pageUrl, soup):
        
        newUrls = set()
        
        links = soup.find_all('a', href = re.compile(r"/view/\d+\.htm"))
        for link in links:
            newUrl = link['href']
            newFullUrl = urlparse.urljoin(pageUrl, newUrl)  #将new按照page的格式进行拼接
            newUrls.add(newFullUrl)
    
        return newUrls
    
    def _getNewData(self, pageUrl, soup):
        resData = {}
        resData['url'] = pageUrl
        
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        titleNode = soup.find('dd',class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        #test
        #print titleNode.get_text();
        resData['title'] = titleNode.get_text()
        
        summaryNode = soup.find('div', class_ = 'lemma-summary')
        #test
        #print summaryNode.get_text()
        resData['summary'] = summaryNode.get_text()
        
        return resData
    
    def parse(self, pageUrl, htmlContainer):
        if pageUrl is None or htmlContainer is None:
            return
        
        soup = BeautifulSoup(htmlContainer, 'html.parser', from_encoding= 'utf-8')
        newUrls = self._getNewUrls(pageUrl, soup)
        newData = self._getNewData(pageUrl, soup)
        return newUrls,newData
    
    



