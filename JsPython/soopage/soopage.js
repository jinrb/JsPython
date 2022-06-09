i = "6f1d0e051a032f0a0602410e0a"

function r(e, t) {
    var r = e.substr(t, 2);
    return parseInt(r, 16)
}

function n(n, c) {
    for (var o = "", a = r(n, c), i = c + 2; i < n.length; i += 2) {
        var l = r(n, i) ^ a;
        o += String.fromCharCode(l)
    }
    return o
}

// http://ae.soopage.com/company/CONCORDE_TEXTILES_TRADING_L_L_C_j0R.html  email
var result =  n(i,0)
console.log(result)