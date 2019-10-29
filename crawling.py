#/usr/bin/env python3
#-*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib import request
from urllib import parse

url = "http://srh.bankofchina.com/search/whpj/search.jsp"
with open("Australia.txt", "wb") as f:
    for page in range(1, 14104):
        fromData = {}
        fromData["erectDate"] = '2009-10-01'
        fromData["nothing"] = '2019-10-29'
        fromData["pjname"] = '1325'
        fromData["page"] = str(page)   #14104
        print(fromData["page"])

        data = parse.urlencode(fromData).encode('utf-8')
        html = request.urlopen(url, data).read()
        soup = BeautifulSoup(html, 'html.parser')

        div = soup.find('div', attrs = {'class':'BOC_main publish'})
        table = div.find('table')
        tr = table.find_all('tr')
        for t in tr:
            td = t.find_all('td')
            try:
                print(td[0].get_text(), td[1].get_text(), td[2].get_text(), td[3].get_text(), td[4].get_text(), td[5].get_text(), td[6].get_text())
            #f.write(string)
            #print(string)
            except:
                pass
