#!/bin/env python
#coding=utf-8
def combine_zone(zone_List):
    #按照起点排序
    sort_list = sorted(zone_list, key=lambda d:d[0])

    #合并后的区间
    new_zone_list = []
    zone = sort_list[0] #初始化
    for item in sort_list[1:]:
        if item[0] == zone[0]:#如果起点相同
            if item[1] > zone[1]: #新的区间终点大于先有终点，则扩展zone
                zone[1] = item[1] #如果小于则不做任何处理
        else: #如果起点大于zone的起点
            if item[0] <= zone[1]: #如果起点位于zone的内部
                if item[1] > zone[1]: #新的区间终点大于先有终点，则扩展zone
                    zone[1] = item[1] #如果小于则不做任何处理
            else: #如果起点位于zone的外部，则说明有截断的情况，更新
                new_zone_list.append(zone)
                zone = item
    #处理最后一个元素
    if len(new_zone_list)==0 or new_zone_list[-1] != zone:
        new_zone_list.append(zone)
    return new_zone_list

if __name__=="__main__":
    zone_list = [[1,2],[2,5],[4,6],[1,5],[7,10],[10,14]]
    print zone_list
    print combine_zone(zone_list)
