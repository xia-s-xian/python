#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#--------------------------------------------------------------------------#
#定时执行任务
#参考：https://blog.csdn.net/liao392781/article/details/80521194
import datetime,os,platform
import schedule,time

def run_task():
    now = datetime.datetime.now()
    now_string=str(now)
    file_name=now_string[0:10]
    print(file_name)
    
'''
def timer_fun(schecd_timer):
    flag=0
    while True:
        now = datetime.datetime.now()
        if now == schecd_timer:
            run_task()
            flag=1
        else:
            if flag ==1:
                schecd_timer=schecd_timer+datetime.timedelta(seconds=4)
                flag=0
'''
    
def every_day(): 
    while True:
        schedule.run_pending()
        time.sleep(1)

#schedule.every().day.at("15:40").do(run_task)
schedule.every(4).seconds.do(run_task)

if __name__ == "__main__":
    every_day()