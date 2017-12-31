create table c_e_usdt_detail
(
	status varchar(8) null comment '状态',
	ch varchar(64) null comment '渠道',
	ts mediumtext null comment '时间戳',
	amount decimal(32,16) null comment '交易数量',
	open decimal(32,16) null comment '开盘价格',
	close decimal(32,16) null comment '当前价格/收盘价格',
	high decimal(32,16) null comment '最高价',
	id mediumtext null,
	count mediumtext null,
	low decimal(32,16) null comment '最低价',
	version mediumtext null,
	askprice decimal(32,16) null comment '卖一价格',
	askamount decimal(32,16) null comment '卖一数量',
	vol decimal(32,16) null,
	bidprice decimal(32,16) null,
	bidamount decimal(32,16) null
)
comment 'usdt行情'
;
