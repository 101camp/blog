# SS4: 在Pyenv中从3.6.5升级至3.7.3时僵局
> 101camp1py 190409 触发

## 苦也:
> 为什么用代码总是获得意外的数据?

进行ch0的第一个开发任务安装python3.7.3时遇到问题:

- 已经安装python3.6.5版本,
- 执行 brew upgrade python3 时,
- 提示 python3 尚未安装,
- 但在执行python3 --version 时是能查到版本的

::

    $ brew upgrade python3
    Updating Homebrew...
    Error: python3 not installed

    $ python3 --version
    Python 3.6.5


请问我该如何操作,我的思路是---

- 是否是Homebrew在GFW内速度感人,所以需要让终端也翻墙再操作. 
- 是否能不霸王硬上弓,使用版本控制方法,比如pyenv或者virtualenv来搞?
- 我猜测第1个思路应该是不对的,第二个应该是OK的. 


## 触发:
> 是也乎,(￣▽￣)

高兴你的高兴

- 作为 17+年 Python 用户, 也深深感 Python 运行时环境是个灵巧又任性的大坑
- 作为初学者, 竟然这么快就独立解决了, 实在太惊人了...
- 也恭喜激发本周最后一个 SM(隐藏任务):
    + 结合自己的体验
    + 试发表一则 Issue:
        * [SM] Python 运行时环境管理小雾
- 用自己的理解给大家分享
    + 什么是 Python?
    + 什么是 Python 运行时?
    + 什么是 系统 Python 环境?
    + 什么是 用户 Python 环境?
    + 在你的桌面系统中, 有多少种 Python 运行环境可以部署?
    + 用哪种来管理最省必? 为什么?
    + 为什么 Python 有这么多运行时环境关系?
- 对于初学者, 最重要的 Pyton 多版本环境控制概念是什么?
- 给出最小 Python 运行时管理工具/概念检查单?
    + 如何检验当前有什么 Python 版本/环境?
    + 当前代码运行时调用的是哪个?
    + 如何切换?
    + ...
- 以及查阅过哪些资料? 哪些最推荐?

## 嗯哼?
> 我去,这个仿佛是不可能完成的任务啊,完全没概念. 

助教来嗯哼:

- 大妈的问题一般都比较完备, 虽然乍一看吓尿指数也很高.
- 冷静下来, 看一道题解决一道. 你没问题的.
- 不过这么快就跑通了虚拟环境, 已经非常非常非常有灵性了.
- But! 这里留个线索... 其实你并没有完全的跑通虚拟环境 嗷!
    + pyenv versions这个命令你已经懂了.
    + 需要实际的了解, 如何切换到自己想要的环境.
    + 并且要明白, 为什么需要切换?
- 以上的思考方向, 可以帮助你了解大妈的提问.


## 解决的解决:
> 问题已解决!思路如下---

我选择第二条路,使用 pyenv 来实现安装 python3.7.3,所以我执行了如下命令:

```
    $ brew install pyenv
    $ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
    $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
    $ source ~/.zshrc
```

但是在进行最后一行命令source ~/.zshrc时,提示错误为:

```
    pyenv: no such command `virtualenv-init'
```

在google上查阅后发现是pyenv-virtualenv没有安装,所以需要执行如下命令:

```
    $ brew upgrade --HEAD pyenv-virtualenv
```

先用上面这个命令更新一下,如果提示没有安装就换下面这个命令
```
    $ brew install --HEAD pyenv-virtualenv
```

之后再进行source ~/.zshrc顺利完成. pyenv安装好后,接下来就是使用它来安装最新python 3.7.3,所以执行下列命令

```
    $ pyenv install 3.7.3
```

,发现3.7.3的安装包在国外,下载十分缓慢,至少等待了30分钟(我洗了个澡),我决定让终端也能翻墙,去墙外下载. 
我使用的是socks5代理,所以终端翻墙较为复杂,先下载最新版本的 Shadowsocks-NG,配置好服务器后,之后在终端执行:

```
     $ export http_proxy=http://127.0.0.1:1087
     $ export https_proxy=http://127.0.0.1:1087
```

然后继续使用pyenv来下载python 3.7.3,又遇到了问题:
```
    $ pyenv install 3.7.3
    BUILD FAILED (OS X 10.14.2 using python-build 20180424)
    Inspect or clean up the working tree at /var/folders/gf/_4hphmvs5lnfz7_sg4l1d3y00000gn/T/python-build.20190410094358.7234
    Results logged to /var/folders/gf/_4hphmvs5lnfz7_sg4l1d3y00000gn/T/python-build.20190410094358.7234.log
    ...
```

查阅后,需要进行如下配置,(It works for me but I don't know why)

```
    $ sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
```

具体内容来源为

> macOS Mojave Pyenv install multi-version build failed solution
> 
> http://www.blog.howechen.com/macos-mojave-pyenv-install-multi-version-build-failed-solution/


操作之后,再执行如下命令,完成!

```

    $ pyenv install 3.7.3
    $ pyenv versions
    * system (set by /Users/Cheyer/.pyenv/version)
      3.7.3

```

到此,就完成配置了!


## 是也乎:
这就是蟒营哪, 正如隔壁队长说的:

> 一个十分开放的课程,开放到他只给你一个框架,内容完全由自己来填写,任何形式任何方法都可以得到包容,也没有人说[哎呀这个应该这样做],他完全靠自己实际操作来触发一系列隐藏任务,而大妈则是"和蔼"的站在背后不时的看看你,指引你,帮助你把这个发现的问题狠狠的踩下去,推动你去弄个明白. 




## PS:
> 当前课程对应公众号 蟒营101camp 暂定专栏有:

- DM 大妈嗯哼 ~ 文本快速呢喃点心境...
- NC 嗯哼蟒营 ~ 图文/图片有关课程信息
- SS 学员故事 ~ 各期课程中发生的真实"血案"
- TS 技术鳮汤 ~ 转载/原创自学技术/心法相关嗯哼

欢迎投稿, 邮件给课程组就好:

    guru101camp@googlegroups.com


## PPS:
蟒营(101.camp): 

    伴你重新享受自学乐趣
    Reactivate Joy by Self-teach with You

- 所以, 不仅仅是 Python ,
- 马上将用蟒营形式发布写作课程,
- 欢迎大家参与体验,
- 用7+1周时间
    + 重新获得写作的乐趣
    + 以及一组高效出品习惯


>> NN 3740








