import requests
import time
import random
import execjs

s = requests.session()

headers = {
  'Host': 'www.qichamao.com',
  'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://www.qichamao.com/search/all/%E5%8D%B0%E8%8A%B1%E6%9D%A5%E4%BA%86?mfccode=-7',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': 'qznewsite.uid=2rvt0wmnrqc0vj2123yvtmdi; Hm_lvt_55ad112b0079dd9ab00429af7113d5e3=1595811820; Hm_lpvt_55ad112b0079dd9ab00429af7113d5e3=1595815475'
}


def get_mfccode():
    t = random.random()
    _ = int(time.time() * 1000)
    url = f"https://www.qichamao.com/home/GetJsVerfyCode?t={t}&_={_}"
    response = s.get(url, headers=headers)
    resp = response.text
    text1 = 'window = {};window.document = {"cookie":"qznewsite.uid=2rvt0wmnrqc0vj2123yvtmdi; Hm_lvt_55ad112b0079dd9ab00429af7113d5e3=1595811820; Hm_lpvt_55ad112b0079dd9ab00429af7113d5e3=1595813900"};'
    text2 = 'function mfccode(){return window["__qzmcf"]();}'
    mfccode = text1 + resp + text2
    # print(mfccode)
    return mfccode

def parse_url(antistop,mfccode):
    url = f'https://www.qichamao.com/search/all/{antistop}?o=0&area=0&mfccode={mfccode}'
    response = s.get(url, headers=headers)
    print(response.status_code)
    resp = response.text
    print(resp)

if __name__ == '__main__':

    mfccode = get_mfccode()
    ctx = execjs.compile(mfccode)
    mfccode = ctx.call("mfccode")
    print(mfccode)
    parse_url('腾讯',mfccode)

