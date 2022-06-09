import requests
import execjs

js_code = '''
function l() {
    var o = new Array(16);
    for (var t, i = 0; i < 16; i++)
        0 == (3 & i) && (t = 4294967296 * Math.random()),
            o[i] = t >>> ((3 & i) << 3) & 255;
    m = o
    f  = [1 | m[0], m[1], m[2], m[3], m[4], m[5]]
    v  = 16383 & (m[6] << 8 | m[7])
    var i =0;
        var b = []
        var y = (new Date).getTime()
            , w = 0
        var A = (1e4 * (268435455 & (y += 122192928e5)) + w) % 4294967296;
        b[i++] = A >>> 24 & 255,
            b[i++] = A >>> 16 & 255,
            b[i++] = A >>> 8 & 255,
            b[i++] = 255 & A;
        var x = y / 4294967296 * 1e4 & 268435455;
        b[i++] = x >>> 8 & 255,
            b[i++] = 255 & x,
            b[i++] = x >>> 24 & 15 | 16,
            b[i++] = x >>> 16 & 255,
            b[i++] = v >>> 8 | 128,
            b[i++] = 255 & v;
        for (var T = 0; T < 6; ++T)
            b[i + T] = f[T];
       // console.log(b,b.length)

    for (var n = [], i = 0; i < 256; ++i)
        n[i] = (i + 256).toString(16).substr(1);
    var r = n,t = b,i=0
    return [r[t[i++]], r[t[i++]], r[t[i++]], r[t[i++]], "-", r[t[i++]], r[t[i++]], "-", r[t[i++]], r[t[i++]], "-", r[t[i++]], r[t[i++]], "-", r[t[i++]], r[t[i++]], r[t[i++]], r[t[i++]], r[t[i++]], r[t[i++]]].join("")
    }
'''

reqId = execjs.compile(js_code).call('l')
print(reqId)
url = f"http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key=%E5%A6%88%E5%A6%88%E7%9A%84%E8%AF%9D&pn=1&rn=30&httpsStatus=1&={reqId}"

headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'Accept': 'application/json, text/plain, */*',
  'csrf': '96R7EAHH1UO',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
  'Referer': 'http://www.kuwo.cn/search/list?key=%E4%B8%8B%E5%B1%B1',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': '_gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1595992253; _ga=GA1.2.481122481.1595992253; _gid=GA1.2.1312879213.1595992253; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1595992262; kw_token=96R7EAHH1UO; kw_token=9C0X38LYYXS'
}

response = requests.get(url, headers=headers)

print(response.json())
