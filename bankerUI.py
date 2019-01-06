#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
本程序是为银行家算法的核心代码提供一个图形化的操作界面,方便用户使用
todo:tkinter中文本还是字符串形式,但是传入核心代码或从文件中读的时候都是List格式这个地方需要转换函数
"""

import tkinter

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

# 第一行的内容,系统资源总数相关
total_var = tkinter.StringVar()
total_var.set("[ 1 , 2 , 3 , 4 ]")

tkinter.Label(main_frame, text="当前系统总资源向量").grid(row=0, column=0, sticky=tkinter.E + tkinter.W)
resource_total_frame = tkinter.Frame(main_frame)
resource_total_frame.columnconfigure(0, weight=1)
resource_total_frame.columnconfigure(1, weight=1)
resource_total_frame.rowconfigure(0, weight=1)
resource_total_frame.grid(row=0, column=1)

resource_total_entry = tkinter.Entry(resource_total_frame, width=20, justify=tkinter.LEFT, textvariable=total_var)
resource_total_entry.grid(row=0, column=0, sticky=tkinter.W)
resource_total_button = tkinter.Button(resource_total_frame, text="锁定系统总资源")
# todo: 锁定系统总资源的按钮对应一个事件,要求能够把结果写到一个文件中,然后将文本框的状态锁定
resource_total_button.grid(row=0, column=1, sticky=tkinter.W)

# 第二三行的内容,系统中已有进程的状态
claim_var = tkinter.StringVar()
own_var = tkinter.StringVar()
claim_var.set("[ 1 , 2 , 3 , 4 ]\n[ 4 , 5 , 6 , 7 ]\n[ 7 , 8 , 9 , 0 ]")
own_var.set("[ a , b , c , d ]\n[ b , c , d , a ]\n[ c , d , a , b ]")

tkinter.Label(main_frame, text="系统中进程最大需要资源").grid(row=1, column=0, sticky=tkinter.E + tkinter.W)
tkinter.Label(main_frame, text="系统中进程已经占用资源").grid(row=1, column=1, sticky=tkinter.E + tkinter.W)
tkinter.Label(main_frame, textvariable=claim_var).grid(row=2, column=0, sticky=tkinter.N)
tkinter.Label(main_frame, textvariable=own_var).grid(row=2, column=1, sticky=tkinter.N)
# todo:上面两个标签对应的文本显示需要注意后期关联过来
# 该行用于向系统中添加进程(无条件)
resource_append_frame = tkinter.Frame(root_window)
resource_append_frame.grid(row=1, column=0, sticky=tkinter.N)
append_claim_entry = tkinter.Entry(resource_append_frame).grid(row=0, column=0)
append_own_entry = tkinter.Entry(resource_append_frame).grid(row=0, column=1)
append_button = tkinter.Button(resource_append_frame, text="添加数据").grid(row=0, column=2)  # todo:按钮事件没有绑定
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
help_info_label = tkinter.Label(help_info_frame, text="这边是\n用户\n使用说明")  # todo:这边的用户提示信息有待完善
help_info_label.grid(row=0, column=0, sticky=tkinter.N)
main_frame.mainloop()
