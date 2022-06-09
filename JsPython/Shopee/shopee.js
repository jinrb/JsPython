var _hash;
function parse(t) {
    return c_parse(unescape(encodeURIComponent(t)))
}

function c_parse(t) {
    for (var e = t.length, n = [], r = 0; r < e; r++)
        n[r >>> 2] |= (255 & t.charCodeAt(r)) << 24 - r % 4 * 8;
    return new a_init(n,e)
}

function a_init(t, e) {
    t = this.words = t || [],
        this.sigBytes = null != e ? e : 4 * t.length
}

u = [];
for (var e = 0; e < 64; e++){
    u[e] = 4294967296 * Math.abs(Math.sin(e + 1)) | 0
}

function _doProcessBlock(t, e) {
    for (var n = 0; n < 16; n++) {
        var r = e + n
            , i = t[r];
        t[r] = 16711935 & (i << 8 | i >>> 24) | 4278255360 & (i << 24 | i >>> 8)
    }
    var o = _hash.words
        , a = t[e + 0]
        , s = t[e + 1]
        , p = t[e + 2]
        , d = t[e + 3]
        , v = t[e + 4]
        , y = t[e + 5]
        , m = t[e + 6]
        , g = t[e + 7]
        , _ = t[e + 8]
        , b = t[e + 9]
        , w = t[e + 10]
        , S = t[e + 11]
        , x = t[e + 12]
        , E = t[e + 13]
        , k = t[e + 14]
        , O = t[e + 15]
        , M = o[0]
        , T = o[1]
        , C = o[2]
        , I = o[3];
    M = c(M, T, C, I, a, 7, u[0]),
        I = c(I, M, T, C, s, 12, u[1]),
        C = c(C, I, M, T, p, 17, u[2]),
        T = c(T, C, I, M, d, 22, u[3]),
        M = c(M, T, C, I, v, 7, u[4]),
        I = c(I, M, T, C, y, 12, u[5]),
        C = c(C, I, M, T, m, 17, u[6]),
        T = c(T, C, I, M, g, 22, u[7]),
        M = c(M, T, C, I, _, 7, u[8]),
        I = c(I, M, T, C, b, 12, u[9]),
        C = c(C, I, M, T, w, 17, u[10]),
        T = c(T, C, I, M, S, 22, u[11]),
        M = c(M, T, C, I, x, 7, u[12]),
        I = c(I, M, T, C, E, 12, u[13]),
        C = c(C, I, M, T, k, 17, u[14]),
        M = l(M, T = c(T, C, I, M, O, 22, u[15]), C, I, s, 5, u[16]),
        I = l(I, M, T, C, m, 9, u[17]),
        C = l(C, I, M, T, S, 14, u[18]),
        T = l(T, C, I, M, a, 20, u[19]),
        M = l(M, T, C, I, y, 5, u[20]),
        I = l(I, M, T, C, w, 9, u[21]),
        C = l(C, I, M, T, O, 14, u[22]),
        T = l(T, C, I, M, v, 20, u[23]),
        M = l(M, T, C, I, b, 5, u[24]),
        I = l(I, M, T, C, k, 9, u[25]),
        C = l(C, I, M, T, d, 14, u[26]),
        T = l(T, C, I, M, _, 20, u[27]),
        M = l(M, T, C, I, E, 5, u[28]),
        I = l(I, M, T, C, p, 9, u[29]),
        C = l(C, I, M, T, g, 14, u[30]),
        M = f(M, T = l(T, C, I, M, x, 20, u[31]), C, I, y, 4, u[32]),
        I = f(I, M, T, C, _, 11, u[33]),
        C = f(C, I, M, T, S, 16, u[34]),
        T = f(T, C, I, M, k, 23, u[35]),
        M = f(M, T, C, I, s, 4, u[36]),
        I = f(I, M, T, C, v, 11, u[37]),
        C = f(C, I, M, T, g, 16, u[38]),
        T = f(T, C, I, M, w, 23, u[39]),
        M = f(M, T, C, I, E, 4, u[40]),
        I = f(I, M, T, C, a, 11, u[41]),
        C = f(C, I, M, T, d, 16, u[42]),
        T = f(T, C, I, M, m, 23, u[43]),
        M = f(M, T, C, I, b, 4, u[44]),
        I = f(I, M, T, C, x, 11, u[45]),
        C = f(C, I, M, T, O, 16, u[46]),
        M = h(M, T = f(T, C, I, M, p, 23, u[47]), C, I, a, 6, u[48]),
        I = h(I, M, T, C, g, 10, u[49]),
        C = h(C, I, M, T, k, 15, u[50]),
        T = h(T, C, I, M, y, 21, u[51]),
        M = h(M, T, C, I, x, 6, u[52]),
        I = h(I, M, T, C, d, 10, u[53]),
        C = h(C, I, M, T, w, 15, u[54]),
        T = h(T, C, I, M, s, 21, u[55]),
        M = h(M, T, C, I, _, 6, u[56]),
        I = h(I, M, T, C, O, 10, u[57]),
        C = h(C, I, M, T, m, 15, u[58]),
        T = h(T, C, I, M, E, 21, u[59]),
        M = h(M, T, C, I, v, 6, u[60]),
        I = h(I, M, T, C, S, 10, u[61]),
        C = h(C, I, M, T, p, 15, u[62]),
        T = h(T, C, I, M, b, 21, u[63]),
        o[0] = o[0] + M | 0,
        o[1] = o[1] + T | 0,
        o[2] = o[2] + C | 0,
        o[3] = o[3] + I | 0
}
function c(t, e, n, r, i, o, a) {
    var u = t + (e & n | ~e & r) + i + a;
    return (u << o | u >>> 32 - o) + e
}
function l(t, e, n, r, i, o, a) {
    var u = t + (e & r | n & ~r) + i + a;
    return (u << o | u >>> 32 - o) + e
}
function f(t, e, n, r, i, o, a) {
    var u = t + (e ^ n ^ r) + i + a;
    return (u << o | u >>> 32 - o) + e
}
function h(t, e, n, r, i, o, a) {
    var u = t + (n ^ (e | ~r)) + i + a;
    return (u << o | u >>> 32 - o) + e
}

function _process(tt) {
    var n = tt
        , r = n.words
        , i = n.sigBytes
        , o = 16
        , u = 4 * o
        , s = i / u
        , c = Math.max((0 | s) - 0, 0) * o
        , l = Math.min(4 * c, i);

    if (c) {
        for (var f = 0; f < c; f += o)
            _doProcessBlock(r, f);
        var h = r.splice(0, c);
        n.sigBytes -= l
    }

    return new a_init(h,l)
}

function _doFinalize(tt,t_leagth) {
    var e = tt
        , n = e.words
        , r = 8 * t_leagth //
        , i = 8 * e.sigBytes;
    n[i >>> 5] |= 128 << 24 - i % 32;

    var o = 0 //
        , a = r;
    n[15 + (i + 64 >>> 9 << 4)] = 16711935 & (o << 8 | o >>> 24) | 4278255360 & (o << 24 | o >>> 8),
        n[14 + (i + 64 >>> 9 << 4)] = 16711935 & (a << 8 | a >>> 24) | 4278255360 & (a << 24 | a >>> 8),
        e.sigBytes = 4 * (n.length + 1),

        _process(e);
    for (var u = _hash, s = u.words, c = 0; c < 4; c++) {
        var l = s[c];
        s[c] = 16711935 & (l << 8 | l >>> 24) | 4278255360 & (l << 24 | l >>> 8)
    }
    return u
}

function stringify(t) {
    for (var e = t.words, n = t.sigBytes, r = [], i = 0; i < n; i++) {
        var o = e[i >>> 2] >>> 24 - i % 4 * 8 & 255;
        r.push((o >>> 4).toString(16)),
            r.push((15 & o).toString(16))
    }
    return r.join("")
}

function get_params(t){
    _hash = new a_init([1732584193, 4023233417, 2562383102, 271733878])
    var a1 = "55b03" + stringify(_doFinalize(parse(t),t.length)) + "55b03"
    _hash = new a_init([1732584193, 4023233417, 2562383102, 271733878])
    var a2 = "55b03" + "-" + stringify(_doFinalize(parse(a1),a1.length))
    return a2
}

// module.exports = {
//     get_params,
// }
//  https://shopee.tw/     if-none-match-
var t = "itemid=4279753152&shopid=168252195"
console.log(get_params(t))