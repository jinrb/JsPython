import requests

def get_param(keyword):
    url = "http://localhost:8090/wyy"
    result = requests.get(url, data={"keyword": keyword}).json()
    print(result)
    return result

def get_info(result):
    url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
    payload = {
        'params':result['encText'],
       'encSecKey':result['encSecKey']
    }
    headers = {
      'authority': 'music.163.com',
      'pragma': 'no-cache',
      'cache-control': 'no-cache',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
      'content-type': 'application/x-www-form-urlencoded',
      'accept': '*/*',
      'origin': 'https://music.163.com',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://music.163.com/search/',
      'accept-language': 'zh-CN,zh;q=0.9',
      'cookie': '_iuqxldmzr_=32; _ntes_nnid=e945cd8b48414a9e67475f2d2e073431,1595917374288; _ntes_nuid=e945cd8b48414a9e67475f2d2e073431; WM_NI=gXStQQEes5eTIn3%2FWU497LUVdI20MftQj8nEovNrBuBogBvEgx4Ulk4U0LBdJz5fRaNE9iwmq8oRTeSyl2UQpBzzoBhlWCUWJt4FWo6NF6RTB1gmrxkhMOaa5NsEGDO9WUw%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8fc53f8e94878ef465fc8e8ea2d54b879b9eaff549fcbdb9b7f77d938da9d7fc2af0fea7c3b92aa5889d95d45b87bbbdd6e8608bb2fdd0d65ff8e7f9add85ea897fed1d06eb88fa6d9ed4fadaa8293c17f82b1a9a3f54fa5a8fcb6ef61f88b00adc1708aa6fb87d16b8e9bf78af667b3e8a1b3d76f91a7a4d3d85bb49eb69bee4aacb499a4d85d8aacfca7d665f6928ad7d16082efa98ef174a9b883b0e46bf792bda6c6508de799b6f637e2a3; WM_TID=CPM0Z5giLf5EABEEAVcuW4ZgV9wEGhrz; JSESSIONID-WYYY=Yg7xF2yXQWxkcbzmC6pkNExyWusxS%2BoDknnnUCWT%2Fbb4evymhqGN1KTD4DdKm5%2FcRbIUCb%2BGOT%2FbXz3pZRnR2fkEzWkGpxM5rCi%2FiNzZmScD7zV0zG%2FEth2hatzRlZj2s7mfdGvSnSjqhe6oB442rRW9j8guoVAMzzWtm0jkFxc6HKrh%3A1595920914290'
    }

    response = requests.post( url, headers=headers, data = payload)
    print(response.status_code)
    result = response.json()
    print(result)


if __name__ == '__main__':
    keyword = '沧海一声笑'
    params = get_param(keyword)
    get_info(params)
