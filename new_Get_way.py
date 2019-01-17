#http://emweb.securities.eastmoney.com/PC_HKF10/FinancialAnalysis/PageAjax?code=00001
from socket import  *
import sys
from lxml import etree
import time
import json
import urllib.request
import csv
x=[]
data=[['股票代码','17-12-31','16-12-31']]
date1='17-12-31'
date2='16-12-31'
totalAcount='资产总额|1'
flag=0
error_data=[]
for i in range(500):
    x.append(str(i+1).zfill(5))
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
for i in range(500):
    url='http://emweb.securities.eastmoney.com/PC_HKF10/FinancialAnalysis/PageAjax?code='+x[i]
    content=urllib.request.urlopen(url).read()
    message = content.decode("utf8")
    if message == '{"msg":"股票代码不合法"}':
        print(x[i]+'error')
        error_data.append(x[i])
    else:
        rst =content.decode("utf-8")
        rst_dict=json.loads(rst)
        l=rst_dict['zcfzb']
        for count in range(len(l)):
            if l[count][0]==date1: dateOrder1=count;  flag=1
            if l[count][0]==date2: dateOrder2=count;  flag=1
        if flag==1:
            for y in range(len(l[0])):
                if l[0][y]==totalAcount: acountColumn=y
            data.append([x[i],l[dateOrder1][acountColumn],l[dateOrder2][acountColumn]])
        else:
            print(x[i] + 'error')
            error_data.append(x[i])
        print(data[-1])
    time.sleep(2)
with open('stockFinancial.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
with open('wrongStock.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in error_data:
        writer.writerow(row)