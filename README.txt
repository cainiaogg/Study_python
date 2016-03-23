<<<<<<< HEAD
+---------------+--------------+------+-----+---------+-------+
| Field         | Type         | Null | Key | Default | Extra |
+---------------+--------------+------+-----+---------+-------+
| secID         | varchar(255) | NO   |     | NULL    |       |
| ticker        | varchar(255) | NO   |     | NULL    |       |
| secShortName  | varchar(255) | NO   |     | NULL    |       |
| date          | varchar(255) | YES  |     | NULL    |       |
| preClosePrice | double       | YES  |     | NULL    |       |
| openPrice     | double       | YES  |     | NULL    |       |
| highestPrice  | double       | YES  |     | NULL    |       |
| lowestPrice   | double       | YES  |     | NULL    |       |
| closePrice    | double       | YES  |     | NULL    |       |
| turnoverVol   | int(11)      | YES  |     | NULL    |       |
| turnoverValue | int(11)      | YES  |     | NULL    |       |

+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| typeID       | varchar(255) | YES  |     | NULL    |       |
| typeName     | varchar(255) | YES  |     | NULL    |       |
| secID        | varchar(255) | YES  |     | NULL    |       |
| exchangeCD   | varchar(255) | YES  |     | NULL    |       |
| secShortName | varchar(255) | YES  |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+
| 101001004006001003 |
 鞍山市             
 | 300210.XSHE 
| XSHE       
| 森远股份     |



| 000014.XSHE |
 000014 | 
 沙河股份     
 | 2015-12-03 00:00:00 
 |  22.42 | 
  22.43 |        
  22.88 |       
  22.22 |      
  22.68 |     
  4786602 |     
  108361880 |

COPY weixin_user (openid, nickname, sex, 
country, province, city, section, 
headimgurl, update_datetime, 
last_visit_datetime, subscribe, 
subscribe_time, unionid, 
auth, x, y, location_updatetime) FROM stdin;
=======
暴力尝试安大校园网 Get_School_Internet
>>>>>>> ff5a8f394adaa4c97b58d33892561353aef080d0
