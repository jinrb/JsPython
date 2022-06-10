// https://m.ehsy.com/#/pages/categoryList/index?catId=1904
// 1653911178
//
// md5
//
// 1b654fee02578648858b4ac0af869f51
//
// n.splice(2, 1, "e"),
// n.splice(6, 1, "h"),
// n.splice(12, 1, 6),
// n.splice(25, 1, "b"),
//
// e 1be54fhe02576648858b4ac0ab869f511653911178
//
// s "GvcaHhBsKa9kkHmf"
//
// o "Soo1sjI6DrJD+F/kgGe4tSY7q3f8lWCphq19LqVxrWPe9qCwIL9/lSJ+2LgSCyh+"

function g(e) {
    var n = t.default.enc.Utf8.parse(e)
      , i = t.default.MD5(s)
      , o = t.default.AES.encrypt(n, i, {
        mode: t.default.mode.ECB,
        padding: t.default.pad.Pkcs7
    });
    return o.toString()
}


var CryptoJS = require("crypto-js");
var s = 'GvcaHhBsKa9kkHmf'

function g(e) {
        var n = CryptoJS.enc.Utf8.parse(e)
          , i = CryptoJS.MD5(s)
            console.log(i)
          , o = CryptoJS.AES.encrypt(n, i, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        });
        return o.toString()
    }


var result = g("44ec94h0008b68d107de9f7b6b6acf251653963638")
console.log(result)