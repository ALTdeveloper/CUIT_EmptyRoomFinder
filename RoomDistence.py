import roomfinder as rfd
#对应每个教学楼，每一层有几个教室，行是教学楼号，列是楼层号
RoomMaxNum = [[9, 9, 9, 9, 9, 4],  [8, 8, 8, 8, 8, 8], [0, 0, 0, 0, 0, 0], [13, 13, 13, 13, 12, 12]] 

def isCircle(room):
    return 0#返回布尔值，输入房间所属域是否为环

def disSameDomin(room1,room2):
    #floor=,i=,j= #获取参数
    build1, floor, Number1 = rfd.extract_classroom_info(room1)
    #print(floor)
    __, __, Number2 = rfd.extract_classroom_info(room2) #双下划线可以安全的丢弃返回值

    N = RoomMaxNum[build1,floor] #获取每一层最大教室数
    if isCircle(room1): #环
        return min(abs(Number1-Number2),N-abs(Number1-Number2))
    else:
        return abs(Number1-Number2)

def disNearstLinkPoint(room):
    LinkPoint = LinkPoints[floor] #floor为楼栋名称和楼层的部分，用于查找唯一平面区域上的节点
    LinkPointNum = len(LinkPoint)#共有几个同层连接点
    dists=[]
    for i in rang(LinkPointNum):
        dists.append(disSameDomin(room,LinkPoint[i]))
    return LinkPoint.index(min(dist)), min(dist) #返回最近节点名称和距离

def disLkPoint2LkPoint(room1,room2):
    building1 = ,building2 = #楼栋号
    floor1 = , floor2 = #楼层号
    if (building1 == building2): #节点同楼栋
        dist = StairHateRate * abs(floor1-floor2) + disSameDomin(room1, roomVirtul) #roomVirtul是构造的虚拟同层参考点
    else:
        #计算房间一节点距
        if (floor1 in range(1,3)):
            LinkPoint = BridgePoint[building1,floor1] #找到同层连接桥点
            distR1=disSameDomin(room1,LinkPoint)
        else:
            LinkPoint = BridgePoint[building1,3] #直接选第三层连接桥点
            distR1=disSameDomin(room1,LinkPoint)
        #计算房间二节点距
        if (floor2 in range(1,3)):
            LinkPoint = BridgePoint[building2,floor2] #找到同层连接桥点
            distR2=disSameDomin(room2,LinkPoint)
        else:
            LinkPoint = BridgePoint[building2,3] #直接选第三层连接桥点
            distR2=disSameDomin(room2,LinkPoint)
        dist = distR1+distR2+bridgeDistFix #bridgeDistFix是天桥修正距离参数
        
    return dist

if __name__ == '__main__':
    print(disSameDomin('H1201','H1203'))
    dist findDistRooms(room1,room2):
    domin1 = , domin2 = #获得房间所属域，即楼栋号和楼层号组成的两位数
    if (domin1==domin2):
        return disSameDomin(room1, room2)
    else:
        dis2LkPoint1, LkPointName1 = disNearstLinkPoint(room1)
        dis2LkPoint2, LkPointName2 = disNearstLinkPoint(room2)
        disLkPoints = disLkPoint2LkPoint(LkPointName1, LkPointName2)
        return dis2LkPoint1+dis2LkPoint2+disLkPoints
