import base64
import hashlib
import time
from Crypto.Cipher import AES
from binascii import b2a_hex
import collections


class AesCBC:
    key = 'BE45D593014E4A4EB4449737660876CE'.encode('utf-8')
    iv = b'A8909931867B0425'

    # 如果text不足16位的倍数就用空格补足为16位
    def add_to_16(self, text):
        if len(text.encode('utf-8')) % 16:
            add = 16 - (len(text.encode('utf-8')) % 16)
        else:
            add = 0
        text = text + ('\0' * add)
        return text.encode('utf-8')

    def encrypt(self, text) -> str:
        # 加密函数
        mode = AES.MODE_CBC
        text = self.add_to_16(text)
        cryptos = AES.new(self.key, mode, self.iv)
        cipher_text = cryptos.encrypt(text)
        # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
        return str(base64.b64encode(b2a_hex(cipher_text)), encoding='utf-8')

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        text = base64.b64decode(text)
        mode = AES.MODE_CBC
        cryptos = AES.new(self.key, mode, self.iv)
        plain_text = cryptos.decrypt(text)
        return bytes.decode(plain_text).rstrip('\0')



class test:
    def __init__(self):
        self.AesCBC = AesCBC()

    def md5(self,sign_str):
        result = hashlib.md5(sign_str.encode("utf-8")).hexdigest()
        return result

    def get_sign(self, params):
        params_1 = collections.OrderedDict(
            sorted(params.items(),
                   key=lambda x: x[0])
        )
        endStr = "3637CB36B2E54A72A7002978D0506CDF"
        for k, v in params_1.items():
            if not v:
                continue
            endStr += k + str(v)
        portal_sign = self.md5(endStr)
        return  portal_sign

    def manage(self):
        t = int(time.time() * 1000)
        params = {"KIND":"GCJS","PROTYPE":"","BeginTime":"2021-12-09 00:00:00","EndTime":"2022-06-09 23:59:59","ts":t}
        portal_sign = self.get_sign(params)
        print(portal_sign)


if __name__ == '__main__':
    test = test()
    test.manage()
