#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# Copyright (C) 2023 , Inc. All Rights Reserved 
# @Time    : 2023/8/10 16:17
# @Author  : raindrop
# @Email   : 1580925557@qq.com
# @File    : main.py

import requests,json,config,push,time,re,random


class Main(object):
    def __init__(self,user):
        self.headers = {
            "Host": "api.weibo.cn",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip",
            "content-type": "application/json;charset=utf-8",
            "user-agent":"Redmi Note 10 Pro_12_weibo_13.7.0_android"
        }
        self.params = {
            "gsid": user["url"]["gsid"],
            "c": "android",  # 客户端校验
            "from": user["url"]["from"],
            "s": user["url"]["s"],
            "lang": "zh_CN",
            "networktype": "wifi",
            "uid": user["url"]["uid"]
        }
        self.name=user["tag"]

    def get_user_name(self):
        try:
            url=config.main("info_url")
            resp = requests.get(url, params=self.params, headers=self.headers).text.encode('gbk',errors='ignore').decode('gbk')
            resp=json.loads(resp)
            if "errno" in resp:
                raise Exception(resp["errmsg"])
            else:
                self.name = resp["userInfo"]["name"]
        except Exception as e:
            print(f"获取用户名时出错, 原因: {e}")
            self.name = "获取失败"

    def item_list(self,list):
        super_List=[]
        for card in list:
            if card["card_type"] == "8":
                scheme = card["scheme"]
                cid = re.findall("(?<=containerid=).*?(?=&)|(?<=containerid=).*",scheme,)
                if len(cid) > 0:
                    super_item = {
                        "level": re.findall(r"LV.\d", card["desc1"])[0],
                        "title": card["title_sub"],
                        "id": cid[0],
                        "status": card["buttons"][0]["name"],  # "已签" or "签到"
                    }
                    super_List.append(super_item)
                    print(f"[{super_item['id']}]: {super_item['title']}")
        return super_List

    def cardlist(self):
        since_id=""
        super_list=[]
        while True:
            url=config.main("haohua_url")
            params = {
                "containerid": "100803_-_followsuper",
                "fid": "100803_-_followsuper",
                "since_id": since_id,
                "cout": 20,
            }
            params.update(self.params)
            resp=requests.get(url,params=params,headers=self.headers).text.encode('gbk',errors='ignore').decode('gbk')
            resp=json.loads(resp)
            if "errno" not in resp:
                for card in resp["cards"]:
                    list_ = self.item_list(card["card_group"])
                    super_list.extend(list_)
            if resp["cardlistInfo"]["since_id"]!="":
                since_id=resp["cardlistInfo"]["since_id"]
            else:
                break
        return super_list

    def checkin(self, item: dict):
        try:
            if item["status"] == "签到":
                params = {
                    "request_url": f"http://i.huati.weibo.com/mobile/super/active_checkin?pageid={item['id']}&in_page=1"
                }
                params.update(self.params)
                url=config.main("check_url")
                resp = requests.get(url,headers=self.headers,params=params,).text.encode('gbk',errors='ignore').decode('gbk')
                resp=json.loads(resp)
                if "errno" in resp:
                    raise Exception(resp["errmsg"])
                else:
                    msg = {
                        "超话": item["title"],
                        "status": True,
                        "msg": "签到成功",
                        "签到排名": resp["fun_data"]["check_count"],  # 第几个签到
                        "积分": resp["fun_data"]["score"],  # 积分
                        "经验": resp["fun_data"]["int_ins"],  # 经验
                        "连续签到": resp["fun_data"]["check_int"],  # 连续签到
                    }
                    #print(f"[success] {item['title']}")
            else:
                msg = {
                    "超话": item["title"],
                    "status": True,
                    "msg": "已签到",
                    "exp": "",
                    "score": "",
                    "continute": "",
                    "rank": "",
                }
                #print(f"[success] {item['title']}")
        except Exception as e:
            msg = {
                "status": False,
                "msg": e,
                "title": item["title"],
                "exp": "",
                "score": "",
                "continute": "",
                "rank": "",
            }
        return msg


    def run(self):
        cardlist=self.cardlist()
        self.get_user_name()
        msg_list=[]
        for item in cardlist:
            msg = self.checkin(item)
            for i in msg:
                if msg[i]!="":
                    print(i+":"+str(msg[i]))
            msg_list.append(msg)
            time.sleep(random.randint(10, 15))
        return {
            "name": self.name,
            "result": msg_list,
        }

def main():
    print("微博自动任务执行开始")
    for i in config.main("user"):
        if i["enable"]:
            a=Main(i)
            b=a.run()
            push_list = []
            push_msg="raindrop微博超话自动任务\n\n当前用户:{}".format(str(b["name"]))
            for msg in b["result"]:
                push_msg += "\n"
                for ss in msg:
                    if msg[ss] != "" and ss!="status":
                        push_msg=push_msg+"\n"+ss + ":" + str(msg[ss])
                        if len(push_msg) > 550:
                            push_list.append(push_msg)
                            push_msg="接上:"
            push_list.append(push_msg)
            for i in push_list:
                push.main(i)
                time.sleep(3)



if __name__ == '__main__':
    main()

