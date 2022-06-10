// https://www.qimai.cn/rank/index/brand/free/country/cn/genre/36/device/iphone
var t = "1654854156.270"
var f = 1396
var a, o = +new Date - (f || 0) - 1515125653845, r = [];
var r = "36cnfreeiphone"
// base64(r)


function i(e) {
        var t, a = (t = "",
        ["66", "72", "6f", "6d", "43", "68", "61", "72", "43", "6f", "64", "65"].forEach((function(e) {
            t += unescape("%u00" + e)
        }
        )),
        t);
        return String[a](e)
    }

function h(e) {
        return function(e) {
            try {
                return btoa(e)
            } catch (t) {
                return Buffer.from(e).toString("base64")
            }
        }(encodeURIComponent(e).replace(/%([0-9A-F]{2})/g, (function(e, t) {
            return i("0x" + t)
        }
        )))
    }
function g(e, t) {
    t || (t = s());
    for (var a = (e = e.split("")).length, n = t.length, o = "charCodeAt", r = 0; r < a; r++)
        e[r] = i(e[r][o](0) ^ t[(r + 10) % n][o](0));
    return e.join("")
}

var e = "MzZjbmZyZWVpcGhvbmU=@#/rank/index@#139727108013@#1"
var t = "0000000c735d856"

var result = h(g(e, t))
console.log(result)


