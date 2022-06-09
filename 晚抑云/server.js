var express = require("express")
var sdk = require("./wyy.js")
var bodyParser = require('body-parser')
var api = express()

api.use(bodyParser.urlencoded({
    parameterLimit: 50000,
    limit: '50mb',
    extended: false
}));

api.get('/wyy', function(req, res){
    var keyword = req.body['keyword']
    var token = sdk.getparam(keyword);
    res.send(token)
});

var server = api.listen(8090, function () {
})