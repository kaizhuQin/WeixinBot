CREATE TABLE `user_msg_log_2` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `msgId` varchar(255) DEFAULT NULL,
  `FromUserName` varchar(100) DEFAULT NULL,
  `ToUserName` varchar(100) DEFAULT NULL,
  `msg_content` text,
  `ctime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `msgType` int(11) DEFAULT NULL,
  `GroupName` varchar(255) DEFAULT NULL,
  `ChatRoomType` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=258 DEFAULT CHARSET=utf8;