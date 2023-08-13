# 微博超话自动签到
>通过微博三个接口分别获取用户超话列表，用户信息和超话签到
<p align="center">
    <a href="https://github.com/raindrop-hb"><img alt="Author" src="https://img.shields.io/badge/author-raindrop-blueviolet"/></a>
    <img alt="PHP" src="https://img.shields.io/badge/code-Python-success"/></a>
    <a href="https://jq.qq.com/?_wv=1027&k=fzhZMSbP"><img alt="QQ群" src="https://img.shields.io/badge/QQ-交流群-blackviolet"/></a>
</p>

------
目前已实现功能：

- [x] 自动签到
- [x] 自动推送
- [x] 多用户

如有其他好的建议请提交issues

## 1.抓包

### 工具

1. vmos（免root）
2. httpcanary(抓包工具)
3. 微博app
   
### 视频教程
>抓包搜索2/cardlist

视频教程链接：<https://v.douyin.com/iJffEopN/>

root机请直接看抓包
## 2.代码部署

### 青龙面板

### *1.订阅方式*
   
> 下面两种任选一种
- 定时任务
    - 脚本/命令
     ```
     ql repo https://github.com/raindrop-hb/zhihu.git
     ```
    - 定时规则（随便）
     ```
     00 00 01 01 ?
     ```
    - 运行，运行结束后删除多的定时任务
- 订阅管理
    - 链接
     ```
     https://github.com/raindrop-hb/wbchaohua.git
     ```
    - 定时规则（随便）
     ```
     00 00 01 01 ?
     ```
    - 自动添加任务取消
    - 自动删除任务确定

### *2.自动任务*
  
- 定时任务
    - 脚本/命令
     ```
     task raindrop-hb_wbchaohua/main.py
     ```
    - 定时规则
     ```
     00 00 00 * * ?
     ```

### 华为云函数工作流 FunctionGraph（免费）（推荐）
华为云主页链接：<https://www.huaweicloud.com/>

华为云函数链接：<https://console.huaweicloud.com/functiongraph/>
- 创建函数
    - 创建空白函数
    - 函数类型:事件函数
    - 区域自定
    - 运行时:python3.10
    - 创建函数
    - 上传自zip文件
    - 上传代码
- 设置
    - 函数执行入口
    ```
     main.handler
    ```
    - 触发器-创建触发器
    - 触发器类型:定时触发器
    - 触发规则:corn表达式
    ```
    00 00 00 * * ?
    ```
## 3.配置修改

修改config.py文件，具体看注释

## 运行截图
![image](https://github.com/raindrop-hb/wbchaohua/assets/72308008/1162f58d-9403-46f4-996c-737a1eb489f6)

![image](https://github.com/raindrop-hb/wbchaohua/assets/72308008/70655650-9e6b-4406-b9ed-8b8d00561279)


