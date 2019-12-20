# TS04:认证的真相

## 烦恼的认证
- 花花世界,数据繁多,小白们看到心水数据,往往相恨太晚不能自持,总希望能把这些可爱的数据搬回家.
- 直觉上,抓取数据不外乎三步,打开冰箱(输入),放进大象(处理),关上冰箱(输出).
- 小白却发现,打开冰箱的第一步已经需要学习大量知识点,比如,怎么认证登录?


> 明确团队希望掌握,模拟网站登录的功能区网页直接抓取数据,但需要学习的知识点太多...

> 经大妈提醒,可以通过 API 抓取.但因为第一次接触 API,资料中很多专有名词和概念,都要转去补充阅读资料才理解,进展很慢...


## 认证的真相
- 以 gitlab 为例,抓取数据的一种流行方法为,从 gitlab api 获取数据.
- 可以通过各式各样工具,向 gitlab 提出请求,比如 curl,requests,GraphQL 等.
- gitlab 给出的示例代码如下,但小白们大呼看不懂!不好用!

```
    curl --header "Private-Token: <your_access_token>" \
        https://gitlab.example.com/api/v4/projects
```

- 其实核心问题在于,示例代码并不是直接就能上手用的. 
- 类似这种示例,如何最终结合到 Python 代码中? 这才是小白们自己该动手的地方.
- 那么, 这里就涉及到一系列有严密逻辑关系的问题:
- curl?
    + 是什么?
    + 如何安装?
    + 如何使用?
- gitlab.example.com
    + 为什么不存在?
    + 应该是什么?
    + 为什么?
- --header "Private-Token: <your_access_token>"
    + --header 是什么意思?
    + "Private-Token: <your_access_token>" 怎么理解?
    + your_access_token 从哪儿获取?
    + 整个儿真实使用时, 应该长什么样?
        * `<`your_access_token`>` 这儿的尖括号要保留嘛?
        * 为什么? 这是什么格式?...
- curl 示例 Python 的行为以及代码实现?
    + 什么是 http ?
    + 什么是 header ?
    + Python 中有什么网络请求模块?
        * 哪个最好?
        * 如何安装
        * 基本使用?
        * ...

- 那么, 如果无法自动分析并规划出这种探索路径,当然真相永远无法抵达...

## 不可遗忘的隐藏
- 当理解了认证后,更加重要的来了.
- 代码中 <your_access_token> 涉及个人隐私和信息安全的情况.
- 软件工程师习惯将一个软件运行起来需要的参数放在INI格式的配置文件里.
- 通过 python 模块调用配置文件里的参数.
- 所以特别提醒正在认证的小白们, 一定要保护好自己的隐私.
- 同时,务必在README或文档醒目位置告知最终用户配置文件的预期位置和名称,否则参数不对软件甚至无法运行.

## 结语
- 这就是蟒营对小白们的挑战,给小白们提供的并不只是知识/技能/常识,更多的是逻辑的挑战...


## refer
- [如何用爬虫抓取需要登录的网站内容 (#50) · Issues · 101Camp / 4py / tasks · GitLab](https://gitlab.com/101camp/4py/tasks/issues/50#note_255534812)
- [[team] <TRI@flyme2333> 数据抓取/分析 (#47) · Issues · 101Camp / 4py / tasks · GitLab](https://gitlab.com/101camp/4py/tasks/issues/47)
- [[FAQ]在 python-gitlab 环境中使用配置文件 Configuration file 详细使用指南 (#63) · Issues · 101Camp / 3py / tasks · GitLab](https://gitlab.com/101camp/3py/tasks/issues/63)
- [[FAQ]用配置文件替换代码中敏感信息 (#60) · Issues · 101Camp / 3py / tasks · GitLab](https://gitlab.com/101camp/3py/tasks/issues/60)
- [Group and project access requests API | GitLab](https://docs.gitlab.com/ee/api/access_requests.html)
- [API Docs | GitLab | personal-access-tokens](https://docs.gitlab.com/ee/api/README.html#personal-access-tokens)
