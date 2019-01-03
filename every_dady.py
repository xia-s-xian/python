#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#参考：https://blog.csdn.net/liao392781/article/details/80521194

import datetime,os,platform
import schedule,time

def run_task():
    now = datetime.datetime.now()
    print(now)

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

schedule.every().day.at("13:12").do(run_task)
schedule.every(4).seconds.do(run_task)
    
if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
    
