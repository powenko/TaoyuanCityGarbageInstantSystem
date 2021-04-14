#!/usr/bin/env python
# -*- coding=utf-8 -*-

#阿貝到此一遊20210414_

__author__ = "Powen Ko, www.powenko.com"
"""
Ivy
"""
"""
參考資料:
https://data.tycg.gov.tw/opendata/datalist/datasetMeta?oid=b3abedf0-aeae-4523-a804-6e807cbad589
https://data.gov.tw/dataset/43963
"""
# 取的

#　BusID(車號),DutyStatus(營運狀態[0=執勤,1=開始,2=結束,90=不明])
# ,RouteID(行駛路線),GoBack(去返程[1=去程,2=返程]),
# Longitude(所在位置緯度),Latitude(所在位置經度),Speed(車速)




"""
Mac 的使用者　如果出現　SSL Certificate Error
請執行以下的程式，HTTPS 就能工作
/Applications/python 3.6/Install Certificates.command
"""

import json
import sys 
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x

import ssl
context = ssl._create_unverified_context()


print("Version:3")




# dicDutyStatus={"0":"執勤","1":"開始","2":"結束","90":"=不明"}

#url="http://data.taipei/opendata/datalist/datasetMeta/download?id=ea732fb5-4bec-4be7-93f2-8ab91e74a6c6&rid=bf073841-c734-49bf-a97f-3757a6013812"
#url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
#url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=b3abedf0-aeae-4523-a804-6e807cbad589&rid=bf55b21a-2b7c-4ede-8048-f75420344aed"
url="http://data.tycg.gov.tw/api/v1/rest/datastore/0c7bcfbf-b151-4411-b888-9ff685ff7a75?format=json"
url="https://data.tycg.gov.tw/api/v1/rest/datastore/0c7bcfbf-b151-4411-b888-9ff685ff7a75?format=json&offset=100" # 由第幾筆開始
url="https://data.tycg.gov.tw/api/v1/rest/datastore/0c7bcfbf-b151-4411-b888-9ff685ff7a75?format=json&limit=800" # 最大資料量800筆
url="https://data.tycg.gov.tw/api/v1/rest/datastore/0c7bcfbf-b151-4411-b888-9ff685ff7a75?format=json&limit=6000" # 最大資料量6000筆
req=httplib.Request(url)
try:
    reponse = httplib.urlopen(req, context=context)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents = reponse.read()
        else:
            contents = reponse.read()
        data = json.loads(contents)
        print(data)


        """
        項次(項次)、清運序(清運序)、行政區(行政區)、清運路線名稱(清運路線名稱)、清運點名稱(清運點名稱)、一般垃圾清運時間(一般垃圾清運時間)、廚餘回收清運時間(廚餘回收清運時間)、資源回收清運時間(資源回收清運時間)
        '項次' = {str} '1'
'清運序' = {str} '1'
'行政區' = {str} '蘆竹區'
'清運路線名稱' = {str} '山腳區1線'
'清運點名稱' = {str} '山林路一段與山腳街口'
'一般垃圾清運時間' = {str} '星期一二四五六:16:55'
'廚餘回收清運時間' = {str} '星期一二四五六:16:55'
'資源回收清運時間' = {str} '星期一二四五六:16:55'

        """

        print("項次:",data["result"]["records"][0]["項次"],
              ",清運序:",data["result"]["records"][0]["清運序"],
              ",行政區",data["result"]["records"][0]["行政區"],
              ",清運路線名稱:",data["result"]["records"][0]["清運路線名稱"],
              ",清運點名稱:",data["result"]["records"][0]["清運點名稱"],
              ",一般垃圾清運時間:",data["result"]["records"][0]["一般垃圾清運時間"],
              ",廚餘回收清運時間:",data["result"]["records"][0]["廚餘回收清運時間"],
              ",資源回收清運時間:",data["result"]["records"][0]["資源回收清運時間"])


        ## 第二題：　顯示全部的
        print("=====第二題：　顯示全部的=======")
        length=len(data["result"]["records"])   # 有幾台的資料
        x=0
        while x<length:
            print("項次:", data["result"]["records"][x]["項次"],
                  ",清運序:", data["result"]["records"][x]["清運序"],
                  ",行政區", data["result"]["records"][x]["行政區"],
                  ",清運路線名稱:", data["result"]["records"][x]["清運路線名稱"],
                  ",清運點名稱:", data["result"]["records"][x]["清運點名稱"],
                  ",一般垃圾清運時間:", data["result"]["records"][x]["一般垃圾清運時間"],
                  ",廚餘回收清運時間:", data["result"]["records"][x]["廚餘回收清運時間"],
                  ",資源回收清運時間:", data["result"]["records"][x]["資源回收清運時間"])
            x=x+1

        ## 第三題：　今天()可以到垃圾的地點

        print("=====第三題：　今天()可以到垃圾的地點=======")
        import time, datetime
        def get_week_day(date):
            week_day_dict = {
                0: '一',
                1: '二',
                2: '三',
                3: '四',
                4: '五',
                5: '六',
                6: '天',
            }
            day = date.weekday()
            return week_day_dict[day]
        from datetime import datetime
        now = datetime.now()    # 現在時間
        week = get_week_day(now)    # 找星期幾

        length=len(data["result"]["records"])   # 有幾台的資料
        x=0
        while x<length:
            txt = data["result"]["records"][x]["一般垃圾清運時間"]
            position = txt.find(week)
            # print(txt,week)
            # print("該字的位置:",x)
            if position>0 and data["result"]["records"][x]["行政區"]=="中壢區" :
                print("今天有垃圾出的地點有-項次:", data["result"]["records"][x]["項次"],
                      ",清運序:", data["result"]["records"][x]["清運序"],
                      ",行政區", data["result"]["records"][x]["行政區"],
                      ",清運路線名稱:", data["result"]["records"][x]["清運路線名稱"],
                      ",清運點名稱:", data["result"]["records"][x]["清運點名稱"],
                      ",一般垃圾清運時間:", data["result"]["records"][x]["一般垃圾清運時間"],
                      ",廚餘回收清運時間:", data["result"]["records"][x]["廚餘回收清運時間"],
                      ",資源回收清運時間:", data["result"]["records"][x]["資源回收清運時間"])

            x=x+1


        ## 第三題：　今天()可以到垃圾的地點

        print("=====第三題：　今天 本小時()可以到垃圾的地點=======")

        now = datetime.now()    # 現在時間
        week = get_week_day(now)    # 找星期幾
        current_H = now.strftime("%H")  # 印出時間的格式
        print("現在時間小時 =", current_H)

        length=len(data["result"]["records"])   # 有幾台的資料
        x=0
        while x<length:
            txt = data["result"]["records"][x]["一般垃圾清運時間"]
            position = txt.find(week)
            positionH = txt.find(":"+current_H+":")            # 星期一二四五六:10:18
            if position>0  and positionH>0 and data["result"]["records"][x]["行政區"]=="中壢區" :
                print("此時可倒垃圾的地點有-項次:", data["result"]["records"][x]["項次"],
                      ",清運序:", data["result"]["records"][x]["清運序"],
                      ",行政區", data["result"]["records"][x]["行政區"],
                      ",清運路線名稱:", data["result"]["records"][x]["清運路線名稱"],
                      ",清運點名稱:", data["result"]["records"][x]["清運點名稱"],
                      ",一般垃圾清運時間:", data["result"]["records"][x]["一般垃圾清運時間"],
                      ",廚餘回收清運時間:", data["result"]["records"][x]["廚餘回收清運時間"],
                      ",資源回收清運時間:", data["result"]["records"][x]["資源回收清運時間"])
            x=x+1







        """
        ## 第三題：　    公車715 RouteID=="715"





        # {
        #   "datas" : [ {
        #     "BusID" : "02760000",

        # print(data["retVal"]["2001"]["sna"])
        # for x in range(2001,2100):
        #    print(data["retVal"][str(x)]["sna"])
        """
except:                                                                 #  處理網路連線異常
    print("error")

