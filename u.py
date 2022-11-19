import requests
from random import choice
from time import sleep
import os
import sys

def readuidarr():
    file = open('dictionary.txt', 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    file_data = file_data.split("\n")
    return file_data

def getvido(ttt):
    url = p + ttt + l
    header = {
        "accept":"*/*",
        "accept-encoding":"gzip, deflate, br",
        "accept-language":"zh,zh-TW;q=0.9,zh-CN;q=0.8",
        "referer":m,
        "sec-ch-ua":"\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"\"Windows\"",
        "sec-fetch-dest":"script",
        "sec-fetch-mode":"no-cors",
        "sec-fetch-site":"cross-site",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=header)
    trs = res.text
    ra = trs.find('"authenable":')
    rd = trs.find(',', ra)
    palyurl = trs[ra+13: rd]
    if str(palyurl) == '1':
        ra = trs.find('"playurl":"')
        rd = trs.find('",', ra)
        palyurl = trs[ra+11: rd]
        print(palyurl)
        print(ttt)
        requests.get(url = n + ttt + "'")
        sys.exit()
    else:
        print('不对')
        

def main():
    file_data = readuidarr()
    for i in file_data:
        getvido(ttt)

if __name__ == '__main__':
    p = os.environ.get("p", None)
    l = os.environ.get("l", None)
    m = os.environ.get("m", None)
    n = os.environ.get("n", None)
    main()
