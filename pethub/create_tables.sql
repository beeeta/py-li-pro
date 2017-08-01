CREATE TABLE `pets` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `type` int(11) DEFAULT NULL COMMENT '0:狗,1:猫，2:稀有',
  `city` varchar(64) DEFAULT NULL,
  `age` int(11) DEFAULT NULL COMMENT '单位：月',
  `wechat` varchar(32) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `source` int(32) DEFAULT NULL COMMENT '信息源，个人发布，或网站发布',
  `status` int(32) DEFAULT NULL COMMENT '0：有效中，2：已收养，3：已过期',
  `createtime` varchar(32) DEFAULT NULL,
  `host` varchar(32) DEFAULT NULL COMMENT '发布人ID',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

