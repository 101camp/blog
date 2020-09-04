# 蟒营®/ 怎么把大象🐘放进冰箱?
> 7py:学员故事...

-------------
## 背景
参考: [蟒营®101.camp 开源网络课程框架](https://doc.101.camp/)...

大妈从99年开始自学各种技术,
到05年开始主动参与技术社区筹备,
已经隐隐发现自学的重要性;
再到09年开始尝试培训,
又9年各种尝试, 才敢在18年圣诞节正式上线 `蟒营®Python入门班` ,
准备应该算是充分的...


-------------
## 现象
但是, 绞尽脑汁儿设计的口号:

```
蟒营® 101.camp: 
    伴你重享自学乐趣
    Reactivate Joy by Self-teching with You

```

却反复被指看不懂;
毕竟, 这是门网络课程, 强调自学, 不就等于说明, 课程本身没用?


-------------
## 分析
> 可是为什么呢?

其实, 就是大妈所有的解说, 都是从课程设计者角度来陈述的, 当然令学习者触动不能.

所以, 看看学员的感受?


-------------
## 怎么把大象🐘放进冰箱?
> 乐豆派@sunnyseed: CI续集...



上集讲到,CI太高冷,只对commit事件才有反应,不如Webhook平易近人,于是乐豆派@葵花籽先生追求Webhook去了. 回头一看,发现团队笔记网站的自动发布,还得靠CI. 

- Webhook触发后,想用脚本自动git push到gitlab,失败概率好高,10个try也架不住,遂放弃
- 研究CI : 代码变更后 -> 触发 -> 自动启动一个管道,去完成某些任务
  - 在这里 = 手工push上传md文件 ->触发-> 
    1. 把md  Build成 gitbook
    2. 再发布到public目录

> 看着就是真命天子😍


-------------
### 1. CI 的 MVP

> 过程看[[Ask\] CI 的第一次尝试:成功,但public里没有文件<解决了,网站缓存问题😭>]
> ,简单说就是在master根目录下加入一个**.gitlab-ci.yml**

```yaml
#使用的docker镜像
image: alpine:latest

pages:
  stage: deploy
  script:
  # 命令
  - cp ./sunnyseed/web/*.html ./public/
  artifacts:
    paths:
    - public
  only:
  - master

```

关键有两句

1. `cp ./sunnyseed/web/*.html ./public/`,这句就是命令行,把html文件拷贝进发布目录

2. `image: alpine:latest`,用这个docker镜像,来运行上面这句语句. 

> 什么?可以直接用docker运行cli,甚至能运行python?这跨度太大,我跟不上

-------------
### 2. Gitbook 的 MVP

> 这个更简单粗暴,但真好用
>
> 2个文件 + 2句命令搞定,具体看网上的介绍吧

```
gitbook init
gitbook build
```

-------------
### 3. 拼装
> 这个逻辑看着挺简单的,就是👇


没用CI前

![CI前](http://ydlj.zoomquiet.top/ipic/2020-05-28-7py-sunnyseed-cd-0.jpg)

使用CI后

![CI后](http://ydlj.zoomquiet.top/ipic/2020-05-28-7py-sunnyseed-cd-1.jpg)


> 可以看出就是用CI,做了手工做的事情

- 1. build
- 2. copy

但要把写完的脚本用上却不容易,总是遇到cancel或者pending,不起作业,也没有报错信息

-------------
### 报错信息在哪里?

> 遍寻网络,尝试修改了五六种不同脚本,包括官网的例子之后. 终于遇到一个正确能用的:

```yaml
# requiring the environment of NodeJS 10
image: node:10

# add 'node_modules' to cache for speeding up builds
cache:
  paths:
    - node_modules/ # Node modules and dependencies

before_script:
  - npm install gitbook-cli -g # install gitbook
  - gitbook fetch 3.2.3 # fetch final stable version
  - gitbook install # add any requested plugins in book.json


# the 'pages' job will deploy and build your site to the 'public' path
pages:
  stage: deploy
  script:
    - gitbook build ./sunnyseed/book public # build to public path
  artifacts:
    paths:
      - public
    expire_in: 1 week
  only:
    - master # this job will affect only the 'master' branch

```

> 终于看到 passed ,激动. 



![passed](http://ydlj.zoomquiet.top/ipic/2020-05-28-7py-sunnyseed-cd-2.jpg)



-------------
### 使用手册
> 怎么把大象放进冰箱?

- 1. 知道大象能放进冰箱
- 2. 找到冰箱
- 3. 学会开门的方法
- 4. 实践它

- Playground, master分支,sunnyseed/book目录,按照gitbook格式放入md文件,修改目录
    + git push
- 就可以看到结果 ～ [乐豆派主页](https://101camp.gitlab.io/7py/playground/)

  
-------------
### refer
> 过程中参考过的重要文章/图书/模块/代码/...

1.  [什么是持续集成(CI)/持续部署(CD)? - 知乎](https://zhuanlan.zhihu.com/p/42286143) 
2.  [Gitlab-CI使用教程 - 掘金](https://juejin.im/post/5e1965375188252695366f8b) 
3.  [GitLab CI: Deployment & Environments | GitLab](https://about.gitlab.com/blog/2016/08/26/ci-deployment-and-environments/) 
4.  [Webhooks | GitLab](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html) 
5.  [Python3.6创建虚拟环境并安装Flask框架 - 简书](https://www.jianshu.com/p/0b909759ccb3)
6.  [利用 GitHook 构建持续交付和部署 - CODING 博客](https://blog.coding.net/blog/GitHook-for-delivery-and-deployment) 
7.   [Python Pandas Cannot import QUOTE_MINIMAL - Stack Overflow](https://stackoverflow.com/questions/60912657/python-pandas-cannot-import-quote-minimal) 



永远的: [提问的智慧](https://github.com/DebugUself/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)


-------------
### 结语
学员@sunnyseed, 算是0基础进入蟒营®的,

但是, 经过4周报名期间预习,4次周任务驱动自学,
自然进入最后两周小组原创作品自组织开发;

过程中, 没有出现拐点, 平滑完成了入门,
而且写出这么有趣的记要来.

实在超乎大妈想象;
毕竟当初撞见 CI/CD 概念时,自己也纠结了几个月,
才慢慢上手的.

可见, 蟒营®Python 入门班本质上并不是单纯的 Python 编程知识入门,
而是更加高阶的编程思维入门班了.


-------------
## 所以

```
蟒营®:

知道你认为自己不NB,
但蟒营®认定你其实非常NB,
  只是习惯了不NB而已,
蟒营®愿带你遇见NB的那个你.

```



-------------
>> NN 4027

好文笔,感叹号年度配额: **1/3**

投稿/反馈邮箱:

    askdama@googlegroups.com


(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)

-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):


```python

私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开课程: 蟒营 (订阅号: Mainium)
历史吐糟: Chaos42 (订阅号 PythoniCamp)

as 核心组织者:
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        TFUG珠海 (订阅号: ZH_TFUG)
```

-------------



