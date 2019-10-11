# SEU_Auto_Reconnection-for-PC

# 东南大学SEU-Wlan新版网页认证(2019-08-01后)<br/>
# 断网自动重连脚本(限PC)<br/>

## 运行环境
* 请优先选择Python 3.6 (已知3.7.4会存在问题，待解决)<br/>


## 基本思路
* 通过分析新版网页认证的登录方式，获取了其请求与认证方式<br/>
* 将请求的url按照其生成规则进行了拼接。<br/>
（与旧版不同，并不存在POST）


## 基本功能
* 网络状态的判断：通过网页访问与其返回状态码进行简单判断。<br/>
* 本地IP的获取：拼接url中所需要的本地地址。<br/>
* 登录请求的发送：向服务端进行认证请求（Request）。<br/>
* 恶趣味输出：如果你看到print的内容感到任何不适，请自行删除。<br/>


## 你所需要做的
在py文件的对应位置，填入你的一卡通号与密码，然后运行程序（So easy）


## 现存担忧
拼接的url中有如下参数：<br/>
![image](https://github.com/yyzhou94/SEU_Auto_Reconnection-for-PC/blob/master/parameter.png?raw=true)<br/>
测试时该参数可以正常使用，但由于所在测试环境为无线谷，该参数是否唯一确定尚不明确，若测试时出现问题，欢迎留言<br/>


## 关于转载
大家自行用用就好，喜欢的话记得素质三连(Watch,Star and Fork)，就别大张旗鼓地向国内论坛转载了~<br/>

## Produced by yyzhou from School of Cyber Science and Engineering


