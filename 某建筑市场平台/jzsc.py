import requests

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


'''
var CryptoJs = require('crypto-js');
var f = CryptoJs.enc.Utf8.parse("jo8j9wGw%6HbxfFn");
var m = CryptoJs.enc.Utf8.parse("0123456789ABCDEF");
function h(t) {
    var e = CryptoJs.enc.Hex.parse(t)
        , n = CryptoJs.enc.Base64.stringify(e)
        , a = CryptoJs.AES.decrypt(n, f, {
        iv: m,
        mode: CryptoJs.mode.CBC,
        padding: CryptoJs.pad.Pkcs7
    })
        , r = a.toString(CryptoJs.enc.Utf8);
    return r.toString()
}
var t = '95780ba0943730051dccb5fe3918f9fe65b3ee2a10eff8fe52aed10f663590e92a3c9d2c87c021f70554ece0b35af4ff86745eb6e9d25bc699aae1a46d3a2de2d4d04d7be370bdf26b25b503403a8748844216ccd71a1f5a2521f154e76511afd3a0e4c59022d56b86f47e7e053b9b38c0d88ff08a8b69bb37c17ea7e4c405eed39cb227cca476611c32feccc2a0d9ee1718df389043cf61a12668d71117d72054d5159e48385ac45386167b7c5d2b3eae8a1ff581e364d90f8fffb950f67ef45c6bc6c1ae693944ef6a15fdfa78d45d8c20e8c52665f64888682ca85e118e77aade38b97119ae5615947c11605a4ccfcdb1ce7807cb6c762421648d546d182d0fe61b2a281cf32a2e1a634e982b3092c127687248701c933b369dbc8e10c79743ffe0ddb0160b16df3ecbf9dd793d659d1fee57f1a1e35fdded27c3eee59a0386ba4053b79d022ad336bda42609bbebd29f01ef282645e0935aff4f013578f8841efa4f03d4702414c0009f0f3d52f40bd3561169bc8ca46f4730e68ae607efc01a0c68656d8ba96d83264447abbca271ce7d65fcc8943cd6e9cf6008e2a58a87e0f6d5284f09506488d240d95cdd267dac6dd57a90e8f3906fddadbd680c80336611ae46dcc49ea95d7efc9cd4e2997c2f5b6e3ce56197e9f221892cd65222be77e350e7e3d95df78fe2538d1c2922e7c71dea04ca37584feccb03082444ea1b8472eadd9314b41d1936875b1db5d6d8a9506bbe4341726b4d51f23c235e541c8c809f8a5411a9ef93afdfa30f07be3a41716ef47f6fea418dc98e3b370ce437561761954c2a27ceaf931e741dec0917c0e16cabdcc777e22f9065aae1ff913b40054ebbd1220335650bdad5345af456608313324459f9e8a815d414fdf613e777f8d4ccbbae074d97e40e2a271ab0607994d61d2ec3b0c145d317d3e545245e71c4cce42ca41dc38c5d71cfb516694f3536a5b7cc98c8bfa53c46d4d3270cbb58d9ea6d1af18f3c83cb02f00b3098745d034e3c25cfa65052cd391dbfb8a0395c2a30a712e691fa451495647ce3905a3d611fc03b3651ebdf04a45a90facbf33be9eae077263114a03d51df51d54cacac047bca3e9c97ceaefedf3736e0dbc672c649dfc4b56e6d4c80c5865c833c70bcc027dcedb76fe006f29ae062866fa92406487071c2cc3a5d80c9a90c36bc1f711e3e28ee87328dd755ce93de451acfab77cd42978d028d7c30bcb05a29212d4a8ff9a3448c789f87246b7100384472a43d769c476459f73d750e7a0d6bee3e3f6448ba9a5a944aa2c1c9741e82b1bb9be361b22a6e002e9963b4508847ddca164cb52b621f1e687396dc0b7f3a850c4f6e1c40c783fcff8d93668037dc37cb65725120892d8d690951f6ce3c161dd5dc0602b48bfe6541edb78050d93a958e35efd854b6455bdce0d65db68bd6ad801f3551df684e86bc4f1beba6308571a21aab8e31c19616c21720295fb1b28a01e7207739877f412fefa8b418075612b91eccb14388c87ec7b70841237d8ec57ac31334ed133c2a58c366b5838332f7f20506a2321c89c2f1e66cf16cc49306c1571162405b735c7e8dcbe56bf86356cb503f522938f49e17869727312d37a04a7b0c080d30df55993a0dfbe157089454348ca6cf63e7bbfef04769d66b45d57cc158d72a1da37a48742dabf9aff55adf0a82ef532588dcf4651d594ad3f0e3763a8c6e9390eff406cb4533e6aa7a1086349184f88596921768c88fe3edc6a1bf24bd871094047e0877c7bb2fa45f5df28d99e922496bbed346f796ad84cd27ec25567952c4f38fccd8d8d4ed7e3fd199e1715e9ed5188a7a6981085ad7c92fd12c58cd620039384c4ab65a18f464e905586a65af822b4df8423864fb992bf6518a17b2670a2bebc3d3303193b8d3c4d80bf820e0b39b36cd7c3fb5d9a75a1e6ee894a6b583f0127f084c674c4f36032243a683aae8a58135f2403216e4e3d1'
console.log(h(t))
'''

class PrpCrypt(object):
    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'0123456789ABCDEF')
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            # \0 backspace
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0123456789ABCDEF')
        plain_text = cryptor.decrypt(a2b_hex(text))
        # return plain_text.rstrip('\0')
        return bytes.decode(plain_text).rstrip('\0')


def parse_info(url):
  headers = {
    'Host': 'jzsc.mohurd.gov.cn',
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'timeout': '30000',
    # 'accessToken':'jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLUzzkwkislt7l4Iii+n3zpFhpUUKvcMtoMqfGfwdLCb8g==',
    'Referer': 'http://jzsc.mohurd.gov.cn/data/company',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1654861642; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1654861642'}
  s = requests.session()
  response = s.get(url, headers=headers)
  resp = response.text
  return resp

if __name__ == '__main__':
    pc = PrpCrypt('jo8j9wGw%6HbxfFn')  # 初始化密钥 key
    url = 'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=0&pgsz=15&orderby=time'
    info = parse_info(url)
    d = pc.decrypt(info)
    print("解密:",d, type(d))








