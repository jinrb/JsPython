import json
import requests
from lxml.etree import HTML
from urllib.parse import quote


def search_page(search_url):
    url = f"http://www.tool168.cn/?m=history&a=view&k={quote(search_url)}&btnSearch=%E6%90%9C%E7%B4%A2"
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://www.tool168.cn/?m=history&a=view&k=https%253A%252F%252Fitem.jd.com%252F100015969858.html&btnSearch=%E6%90%9C%E7%B4%A2',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'JM_SESSION_X=1; BFPD=JNUMBWVFPUCEEWUCLDJ_1654667363; PHPSESSID=ik5h1htsppv8equsvh69lbcc27; Hm_lvt_61e842dc51946642fa309fd4e1c752aa=1654667364; Hm_lpvt_61e842dc51946642fa309fd4e1c752aa=1654668395'
    }
    response = requests.get(url, headers=headers)
    html = HTML(response.text)
    checkCodeId = html.xpath('//input[@id="checkCodeId"]/@value')[0]
    reqid = html.xpath('//input[@id="reqid"]/@value')[0]
    reqid2 = reqid[::-1]
    checkCodeId = checkCodeId + 'P' + reqid2[7:10]
    return checkCodeId, reqid


def getptinfo(checkCodeId, reqid, search_url):
    url = f"http://www.tool168.cn/dm/ptinfo.php?ud=&reqid={reqid}"
    payload = f'checkCode={checkCodeId}&con={search_url}'
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://www.tool168.cn',
        'Referer': 'http://www.tool168.cn/?m=history&a=view&k=https%253A%252F%252Fitem.jd.com%252F100015969858.html&btnSearch=%E6%90%9C%E7%B4%A2',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    code = response_json['code']
    return code

def manage(search_url):
    checkCodeId, reqid = search_page(search_url)
    print(checkCodeId, reqid)
    code = getptinfo(checkCodeId, reqid, search_url)
    print(code)

if __name__ == '__main__':
    search_url = 'https://item.jd.com/100015969858.html'
    manage(search_url)

