#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
描述:课设题目银行家算法的核心运算部分
作者:计嵌162 史学超 20160323
日期:2019-01-10
修改:改变了add_list为add_data.格式e.g [0,[1, 2, 3,4]],表示第0个资源需要添加的资源向量为[1, 2, 3,4]
"""


def write_file(total_list_, claim_list2_, own_list2_):
    # 把需要的数据写到文件中,即保存了结果,也方便其他程序的读取
    from simplejson import dump
    with open('./resource_total_list.txt', 'w') as ft:
        dump(total_list_, ft)
    with open('./resource_claim_list.txt', 'w') as fc:
        dump(claim_list2_, fc)
    with open('./resource_own_list.txt', 'w') as fo:
        dump(own_list2_, fo)
    print("成功将数据写到文件")


def read_file():
    # 从对应的文件中读出对应的数据并包装成合适的格式
    from simplejson import load
    with open('./resource_total_list.txt', 'r') as ft:
        total_list = load(ft)
    with open('./resource_claim_list.txt', 'r') as fc:
        claim_list2 = load(fc)
    with open('./resource_own_list.txt', 'r') as fo:
        own_list2 = load(fo)
    return total_list, claim_list2, own_list2


def check_safety(own_list2_, need_list2_, free_list_):
    """
    检查当前系统状态是否安全,如果安全返回True,否则返回False
    todo:最好能够返回出正确的序列结果
    :param own_list2_: List[List[int]]  已获得资源矩阵
    :param need_list2_: List[List[int]] 需要资源矩阵
    :param free_list_: List[int]        可用资源向量
    :return: Boolean                    是否安全
    """

    def satisfy_current(wait_list_, current_list_):
        """
        判断当前的可使用向量能否满足待申请进程的要求
        :param wait_list_: List[int]    需要资源向量
        :param current_list_: List[int] 当前可使用资源向量
        :return: Boolean                是否满足
        """
        for i in range(len(wait_list_)):
            if wait_list_[i] > current_list_[i]:
                return False
        else:
            return True

    for own_list in own_list2_:
        for value in own_list:
            if value < 0:
                print("系统中有进程过度占用资源")
                return False
    resource_current_list = [_ for _ in free_list_]
    process_wait_set = {_ for _ in range(len(own_list2_))}
    while True:
        for x in process_wait_set:
            if satisfy_current(need_list2_[x], resource_current_list):
                process_wait_set -= {x}
                for index in range(len(resource_current_list)):
                    resource_current_list[index] += own_list2_[x][index]
                break
        else:
            if not process_wait_set:
                return True
            else:
                return False


def main(total_list_=None, claim_list2_=None, own_list2_=None, add_data_=None):
    """
    程序运行的主函数部分,能够从对应的文件中读取所需的参数,也能接受传递的参数.能够判断当前程序是否安全,
    判断能否添加新的进程进入系统
    :param total_list_:  List[int]         系统总拥有资源向量
    :param claim_list2_: List[List[int]]   系统内所有进程所需最大资源矩阵
    :param own_list2_:   List[List[int]]   系统内所有进程已拥有资源矩阵
    :param add_data_:    List[int,List[int]]等待进入系统的资源向量
    :return:             Boolean           true对应系统安全,反之
    例子:前三个参数已经设置了从文件读取,最后一个添加资源向量如果有还是选择通过参数传递
    e.g.main(add_data_ =  _resource_add_data)
    """
    if total_list_ is None and claim_list2_ is None and own_list2_ is None:
        resource_total_list, resource_claim_list2, resource_own_list2 = read_file()
    else:
        resource_total_list = total_list_
        resource_claim_list2 = claim_list2_
        resource_own_list2 = own_list2_
    print("系统拥有的总共资源向量为:", resource_total_list)
    print("各个进程需要最大资源矩阵为:", resource_claim_list2)
    print("各个进程已经拥有资源矩阵为:", resource_own_list2)
    number_resource = len(resource_total_list)
    number_process = len(resource_claim_list2)
    print("系统中拥有的资源种类:{}\n系统正待命的进程数量:{}".format(number_resource, number_process))
    resource_need_list2 = [[resource_claim_list2[r][c] - resource_own_list2[r][c] for c in range(number_resource)]
                           for r in range(number_process)]
    print("各个进程仍需要资源矩阵为:", resource_need_list2)
    resource_free_list = [_ for _ in resource_total_list]
    for need_list in resource_own_list2:
        for i in range(number_resource):
            resource_free_list[i] -= need_list[i]

    for num_free in resource_free_list:
        if num_free < 0:
            print("警告!系统当前已经缺少资源")
            return False
    else:
        print("系统可用资源向量为:", resource_free_list)

    if add_data_ is None:
        if check_safety(resource_own_list2, resource_need_list2, resource_free_list):
            print("系统是安全的")
            return True
        else:
            print("系统是不安全的")
            return False
    else:
        pass
        for item_add, item_free in zip(add_data_[1], resource_free_list):
            if item_add > item_free:
                print("当前系统无法添加新的进程")
                return False
        # 修改当前的拥有资源矩阵,需求矩阵和空闲资源矩阵,然后重新检查安全性
        for _ in range(number_resource):
            resource_own_list2[add_data_[0]][_] += add_data_[1][_]
            resource_need_list2[add_data_[0]][_] -= add_data_[1][_]
            resource_free_list[_] -= add_data_[1][_]
        if check_safety(resource_own_list2, resource_need_list2, resource_free_list):
            print("该程序的申请是允许的")
            return True
        else:
            print("这次申请会破坏系统安全性")
            return False


if __name__ == '__main__':
    _resource_total_list = [17, 9, 13, 8]
    _resource_claim_list2 = [
        [3, 0, 2, 2],
        [4, 3, 1, 2],
        [3, 5, 5, 3],
        [4, 6, 7, 3],
        [6, 3, 4, 3]
    ]
    _resource_own_list2 = [
        [2, 0, 1, 2],
        [3, 2, 1, 1],
        [2, 2, 3, 1],
        [3, 3, 4, 2],
        [5, 1, 2, 1]
    ]
    _resource_add_data = [0, [1, 0, 0, 0]]
    write_file(_resource_total_list, _resource_claim_list2, _resource_own_list2)
    main(add_data_=_resource_add_data)
    print("---银行家算法运行结束---")
