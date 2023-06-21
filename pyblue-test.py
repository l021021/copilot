import time
from bluetooth import *

#列表，用于存放已搜索过的蓝牙名称
alreadyFound = []

#搜索蓝牙
def findDevs():
    foundDevs = discover_devices(lookup_names=True)
    # 循环遍历,如果在列表中存在的就不打印
    for (addr,name) in foundDevs:
        if addr not in alreadyFound:
            print("[*]蓝牙设备:" + str(name))
            print("[+]蓝牙MAC:" + str(addr))
            # 新增的设备mac地址定到列表中,用于循环搜索时过滤已打印的设备
            alreadyFound.append(addr)

# 循环执行,每5秒执行一次
while True:
    findDevs()
#discover_devices的放回参数
#[(u'00:0C:BF:0B:BD:8C', u'Nexus 5'), (u'00:0C:BF:15:8B:9C', u'Nexus 5'), (u'00:0C:BF:0B:BD:8C', u'Nexus 5'), (u'00:0C:BF:15:8B:9C', u'Nexus 5')]
    time.sleep(5)