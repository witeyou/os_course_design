#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
描述:本程序是为银行家算法的核心代码提供一个图形化的操作界面,方便用户使用
作者:计嵌162 史学超 20160323
日期:2019-01-07
修改:增加了将list对象写到指定文件的功能
     增加了将string按一定格式转换成一维list的功能
     为锁定资源总量按钮和添加数据按钮绑定了事件
todo:1.tkinter中文本还是字符串形式,但是传入核心代码或从文件中读的时候都是List格式这个地方需要转换函数
TODO:2.程序的数据除了通过UI来添加最好是也能够能够文件直接区读取的.并且能够实现复位,用两个按钮来解决
"""

import tkinter


def str_to_list(str_):
    """
    用于将读到的字符串按一定的格式转换成一维的List,供核心代码运算
    :param str_:     String  待转换的字符串
    :return:         List[int]
    """
    from copy import deepcopy
    res_list = []
    tmp_str = deepcopy(str_)
    tmp_str.strip()
    for _ in tmp_str.split("-"):
        res_list.append(int(_))
    return res_list


def list_to_file(src_list_, filename_):
    """
    用于将一个List对象写入一个指定的文件中
    :param src_list_: Sting     要写入的文件名
    :param filename_: List[Int] 待写入的List对象
    """
    from simplejson import dump
    with open(filename_, 'w')as f:
        dump(src_list_, f)
    print("成功将文件写入", filename_)


def total_edit():
    """
    对应锁定资源向量的那个按钮
    """
    tmp_str = resource_total_entry.get()
    global resource_total_list
    resource_total_list = str_to_list(tmp_str)
    list_to_file(resource_total_list, './UI_total_list.txt')
    resource_total_entry.config(state=tkinter.DISABLED)


def add_edit():
    """
    对应添加数据那个按钮的功能
    """
    claim_tmp_str = claim_add_var.get()
    own_tmp_str = own_add_var.get()
    global resource_claim_list2, resource_own_list2
    resource_claim_list2.append(str_to_list(claim_tmp_str))
    resource_own_list2.append(str_to_list(own_tmp_str))
    list_to_file(resource_claim_list2, './UI_claim_list2.txt')
    list_to_file(resource_claim_list2, './UI_own_list2.txt')
    claim_var.set(claim_var.get() + claim_tmp_str + "\n")
    own_var.set(own_var.get() + own_tmp_str + "\n")
    claim_add_var.set("")
    own_add_var.set("")


root_window = tkinter.Tk()  # root frame
root_window.title("银行家算法界面")
root_window.geometry('800x450')
root_window.columnconfigure(0, weight=1)
root_window.rowconfigure(0, weight=4)
root_window.rowconfigure(1, weight=1)
root_window.rowconfigure(2, weight=1)
root_window.rowconfigure(3, weight=2)

main_frame = tkinter.Frame(root_window)
main_frame.grid(row=0, column=0, sticky=tkinter.W + tkinter.E)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=3)

# 这边用来声明UI相关的变量
total_var = tkinter.StringVar()
total_var.set("输入系统总资源向量")
claim_var = tkinter.StringVar()
own_var = tkinter.StringVar()
claim_add_var = tkinter.StringVar()
own_add_var = tkinter.StringVar()
claim_var.set("")
own_var.set("")
help_info_string = """
输入时统一用资源向量来表示资源,
输入的格式是1-2-3-4 这样表示有4种资源,每个数表示对应资源的数量
"""
# 这边用来声明计算相关的变量
resource_total_list = []
resource_claim_list2 = []
resource_own_list2 = []
# 第一行的内容,系统资源总数相关
tkinter.Label(main_frame, text="当前系统总资源向量").grid(row=0, column=0, sticky=tkinter.E + tkinter.W)
resource_total_frame = tkinter.Frame(main_frame)
resource_total_frame.columnconfigure(0, weight=1)
resource_total_frame.columnconfigure(1, weight=1)
resource_total_frame.rowconfigure(0, weight=1)
resource_total_frame.grid(row=0, column=1)

resource_total_entry = tkinter.Entry(resource_total_frame, width=20, justify=tkinter.LEFT, textvariable=total_var)
resource_total_entry.grid(row=0, column=0, sticky=tkinter.W)
resource_total_button = tkinter.Button(resource_total_frame, text="锁定系统总资源", command=total_edit)
resource_total_button.grid(row=0, column=1, sticky=tkinter.W)

# 第二三行的内容,系统中已有进程的状态
tkinter.Label(main_frame, text="系统中进程最大需要资源").grid(row=1, column=0, sticky=tkinter.E + tkinter.W)
tkinter.Label(main_frame, text="系统中进程已经占用资源").grid(row=1, column=1, sticky=tkinter.E + tkinter.W)
tkinter.Label(main_frame, textvariable=claim_var).grid(row=2, column=0, sticky=tkinter.N)
tkinter.Label(main_frame, textvariable=own_var).grid(row=2, column=1, sticky=tkinter.N)
# 该行用于向系统中添加进程(无条件)
resource_append_frame = tkinter.Frame(root_window)
resource_append_frame.grid(row=1, column=0, sticky=tkinter.N)
append_claim_entry = tkinter.Entry(resource_append_frame, textvariable=claim_add_var).grid(row=0, column=0)
append_own_entry = tkinter.Entry(resource_append_frame, textvariable=own_add_var).grid(row=0, column=1)
append_button = tkinter.Button(resource_append_frame, text="添加数据", command=add_edit).grid(row=0,
                                                                                          column=2)  # todo:按钮事件没有绑定
# 该行用于检查系统安全性
# todo:这部分的控件都没有绑定具体的内容
resource_check_frame = tkinter.Frame(root_window)
resource_check_frame.grid(row=2, column=0, sticky=tkinter.N)
check_static_button = tkinter.Button(resource_check_frame, text="静态安全性检查"). \
    grid(row=0, column=0, sticky=tkinter.N)
check_dynamic_entry = tkinter.Entry(resource_check_frame, width=20, justify=tkinter.LEFT). \
    grid(row=0, column=1, sticky=tkinter.N)
check_dynamic_button = tkinter.Button(resource_check_frame, text="动态安全性检查"). \
    grid(row=0, column=2, sticky=tkinter.N)
# 该行用于提示用户的操作信息
help_info_frame = tkinter.LabelFrame(root_window, text="使用提示", labelanchor='n')
help_info_frame.grid(row=3, column=0)
help_info_label = tkinter.Label(help_info_frame, text=help_info_string)  # todo:这边的用户提示信息有待完善
help_info_label.grid(row=0, column=0, sticky=tkinter.N)
main_frame.mainloop()
