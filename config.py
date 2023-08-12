#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# Copyright (C) 2023 , Inc. All Rights Reserved
# @Time    : 2023/8/10 19:04
# @Author  : raindrop
# @Email   : 1580925557@qq.com
# @File    : config.py.py

def main(key):
    user = [
        # user1
        {
            # 开关True开False关
            "enable": False,
            # 给该用户一个备注
            "tag": "",
            "url": {
                "wb_version": "6279",
                "c": "android",
                "s": "f93b",
                "from": "110",
                "gsid": "_2A25J0mIdubB0",
                "uid":"749338"
            }
        },
        #user2
        {
            # 开关True开False关
            "enable": False,
            # 给该用户一个备注
            "tag": "",
            "url": {
                "wb_version": "6279",
                "c": "android",
                "s": "3769",
                "from": "10D010",
                "uid":"62012",
                "gsid": "_2A25J0MIHXvgHyxYlu",
            }
        },
        {
            # 开关True开False关
            "enable": False,
            # 给该用户一个备注
            "tag": "",
            "url": {
                "wb_version": "6279",
                "c": "android",
                "s": "3a64",
                "from": "10010",
                "uid":"775034",
                "gsid": "_2sqUbQ3j",
            }
        },
    ]
    push={
        "WeCom": {
            # 是否企业微信推送True或False
            "push": "False",
            # 企业ID
            "corpid": "ww226a",
            # 应用的凭证密钥
            "secret": "CB",
            # 应用id
            "agentid": "1000003",
            #推送userid，@all为全员
            "touser":"@all"
        },
        "Ding": {
            # 是否钉钉推送
            "push": "False",
            # 应用凭证
            "appkey": "dingoqw",
            # 应用凭证
            "appsecret": "UptFE0xc4nsCpDRa",
            # 钉钉app-部门群-设置-机器人-webhook
            "webhook": "https://oapi.dingtalk.com/robot/send?access_token="
        },
        "pushplus": {
            # 是否pushplus推送
            "push": "False",
            # pushplus  token
            "token": "be3423bfe"
        }
    }
    haohua_url="https://api.weibo.cn/2/cardlist"
    check_url="https://api.weibo.cn/2/page/button"
    info_url = "https://api.weibo.cn/2/profile"
    return eval(key)

