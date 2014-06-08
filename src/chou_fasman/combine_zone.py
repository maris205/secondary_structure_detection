#!/bin/env python
#coding=utf-8
def combine_zone(zone_List):
    #�����������
    sort_list = sorted(zone_list, key=lambda d:d[0])

    #�ϲ��������
    new_zone_list = []
    zone = sort_list[0] #��ʼ��
    for item in sort_list[1:]:
        if item[0] == zone[0]:#��������ͬ
            if item[1] > zone[1]: #�µ������յ���������յ㣬����չzone
                zone[1] = item[1] #���С�������κδ���
        else: #���������zone�����
            if item[0] <= zone[1]: #������λ��zone���ڲ�
                if item[1] > zone[1]: #�µ������յ���������յ㣬����չzone
                    zone[1] = item[1] #���С�������κδ���
            else: #������λ��zone���ⲿ����˵���нضϵ����������
                new_zone_list.append(zone)
                zone = item
    #�������һ��Ԫ��
    if len(new_zone_list)==0 or new_zone_list[-1] != zone:
        new_zone_list.append(zone)
    return new_zone_list

if __name__=="__main__":
    zone_list = [[1,2],[2,5],[4,6],[1,5],[7,10],[10,14]]
    print zone_list
    print combine_zone(zone_list)
