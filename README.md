# pylib
pylib是一个用python编写的用于获取传感器芯片、硬件、服务、操作系统信息的库。
目前涵盖的库有：
- 物联网芯片AT指令库与数据通信库
- 硬件信息查询库
- 系统信息查询库
- MYSQL 驱动库

### 硬件信息库

- CPU
- Memory
- Net
- Disk
- GCard
### 目前支持的传感器芯片

- DL-20 (Zigbee)
- SIM7000C (GPS\GPRS\NB-IOT)
- SIM800C (GPS\GPRS\GSM)

## 芯片功能库 
- GPS
  - GPS+北斗联合定位
  - GPS独立定位
  - GPS 原子时 （UTC+8\北京时间）
  - GPS 原子日期
  - GPS 海拔
  - GPS 速率

- GPRS
  - 网络信号质量
  - 网络注册状态
  - 模块附着网络
  - APN
  - 移动场景激活
  - IP 地址
  - HTTP 连接
  - ICMP Ping 包
- SMS
  - 短信 TEXT 发送



### 更新日志

- 2018-11-8: 发布 GPS、GPRS、SMS 模块库,修复 Bug

- 2018-12-24: 增加sys系统库、MYSQL驱动库,修复 Bug
