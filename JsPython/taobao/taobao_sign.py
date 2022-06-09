
#### sign值 加密逻辑
# j = md5(d.token + "&" + i + "&" + g + "&" + c.data)
# d.token 7815183f205965f9833be9600d195a06   cookie中获取：_m_h5_tk=7815183f205965f9833be9600d195a06_1624362479609
# i  1624353341073  时间搓
# g  12574478	 appKey 固定
# c.data  {"m":"shopitemsearch","vm":"nw","sversion":"4.6","shopId":"57303596","sellerId":"196993935","style":"wf","page":4,"sort":"_coefp","catmap":"","wirelessShopCategoryList":""}   (需要shopId，sellerId，page，其他可固定)
