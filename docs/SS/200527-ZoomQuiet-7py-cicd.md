# 蟒营™/ CI/CD 像是在读侦探小说
> 7py 学员故事...

-------------
## 背景
参考: [蟒营™101.camp 开源网络课程框架](https://doc.101.camp/)...

大妈从99年开始自学各种技术,
到05年开始主动参与技术社区筹备,
已经隐隐发现自学的重要性;
再到09年开始尝试培训,
又9年各种尝试, 才敢在18年圣诞节正式上线 `蟒营™Python入门班` ,
准备应该算是充分的...


-------------
## 现象
但是, 绞尽脑汁儿设计的口号:

```
蟒营™ 101.camp: 
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
## CI/CD 像是在读侦探小说
> 乐豆派@sunnyseed 蟒营™Python 入门班第7期团队队长


-------------
### 背景

> 额外任务, 若有余力, 也请完成

- 如何通过 CI/CD (持续集成/部署) 功能,令 gitlab 可以感知到小队分支变化
  - 统计数据
  - 数据可视化
  - 团队笔记网站更新发布
- **简单说**, 是否可以将以往人工指令方式完成的一系列行为,变成可以通过某种仓库行为触发自动化过程?


-------------
### 进展

> 就好像是侦探小说,开头说这里有个现场:gitlab有变化时,网站被自动更新了,**犯人**怎么做到的?
>

⚠️: 大量术语,扑面而来. . . 

-------------
#### 1. 怎么知道git-lab出现了变化?

> 查来查去,发现两种方法:

1. 持续集成(CI):代码变更后,gitlab自动启动一个管道,去完成某些任务
   - 管道,pipeline:多个不同的 *任务(task)*和 *作业(job)*,串联成的一个流程. 完成一个自动启动下一个.  
2. Web hook :在gitlab订阅一个事件,比如发了一个issue之后,webhook会向你指定的服务器,发送事件的提醒

> CI太高冷,只对commit事件有反应,不如Webhook平易近人,先追求Webhook看看,,,

-------------
#### 2. Webhook跑起来
> webhook入门,要趟过6个坑:

1. 权限?playground有webhook权限,tasks没有,先上playground

2. 设计?就是附加题,**提示**,中的这一句:

>> 但是, 不依赖任何服务,只通过一个长期运行的主机也一样可以完成低配版 CI/CD 响应

3. 主机?就是一个能够接受 webhook post 来的消息的,web应用. 查webhook例子时,找了一个叫 flask:

```python
# 请求处理
from flask import Flask, request

app = Flask(__name__)

# WebHooks 使用 POST 请求
@app.route('/', methods=['POST'])
def git_hook():
   # 这就是收到的 json 本体
   receive = request.data.decode('utf-8')
   if request.json['object_kind'] == 'push':
       # 对commits进行处理
            ...
   return 'success'

if __name__ == "__main__":
   app.run(debug=True, port=5050, host='0.0.0.0')

```

惊不惊喜?意不意外?😀

> 这段话是几个帖子凑成的,跑通,2小时过去了. 但回头看,真的简单. 

4. 外网?怎么让gitlab找到我的电脑?突然想起ch4题目中,提到ch3的坑:
   - 为什么不能将内网应用直接发布到外网?

我们组因为直接发布在gitlab page上,ch3没有使用自己的服务器. 但6py结业bp上,erica组用过一个内网穿透工具,记忆犹新,小本子翻出来,叫做ngrok ~  [ngrok - secure introspectable tunnels to localhost](https://ngrok.com/) 又是一个神奇小子. 安装,运行,又是只要一句:

```
$ ngrok http 5050

```

   

5. 组装?配上webhook`http://sunnyseed.ngrok.io/hook`,之后网络结构是下面这样的


![结构](http://ydlj.zoomquiet.top/ipic/2020-05-28-7py-sunnyseed-ci-0.jpg)


6. 自动?进一步修改 flask 的响应语句,获取三种不同的时间:commit\issue\note,存放在csv中,再用小组此前设计的,pandas语句统计,输出成html,就ok啦.  

```python
# comments
if request.json['object_kind'] == 'note':
   c0 = 'comment'
   c1 = time.strftime("%Y%m%d%H%M%S", time.localtime())
   c2 = request.json['user']['username']
   c3 = "1" #都是一次
   c = f"{c0},{c1},{c2},{c3}"

# 写入csv
f = open("ci.csv", 'a')
f.write(f"{c}\n")
f.close()

# csv -> html
columns = ['Type', 'Datetime', 'Username', 'Count']
df = pd.read_csv('ci.csv', names=columns, engine = 'python')
# group(分组字段)[统计字段1][统计字段2].sum, 之后的部分用于怎加列名
df_1 = df.groupby(['Type','Username'])['Count'].sum().to_frame('Count').reset_index()
df_2 = df_1.sort_values(by='Count',ascending=False)

# 保存为 html "网站主目录"
df_2.to_html('ci.html')
   

```


![](http://ydlj.zoomquiet.top/ipic/2020-05-28-7py-sunnyseed-ci-1.jpg)

写到这里主体就完成了


-------------
#### 3. 使用手册

- 在playground 任意发帖,或者git push之后,访问 [排名展示页](http://101camp.applinzi.com) 就可以实时看到排名变化啦(测试用,历史数据不准确,新增是对的啦🎭,,,应该)
  


-------------
### 问题
> mvp完成,能不能更好

- 问题0 -> 我的mini可是要关机的,怎么7*24小时运行?
- 问题1 -> 如果使用原来的ssg 和 gitlab page,就要使用CI,但又是一堆坑,比如怎么控制git push?

  
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
学员@sunnyseed, 算是0基础进入蟒营™的,

但是, 经过4周报名期间预习,4次周任务驱动自学,
自然进入最后两周小组原创作品自组织开发;

过程中, 没有出现拐点, 平滑完成了入门,
而且写出这么有趣的记要来.

实在超乎大妈想象;
毕竟当初撞见 CI/CD 概念时,自己也纠结了几个月,
才慢慢上手的.

可见, 蟒营™Python 入门班本质上并不是单纯的 Python 编程知识入门,
而是更加高阶的编程思维入门班了.



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



