# 拙见/ 远程"办公"的正确姿势
> 普通老程序猿叕一则思考痕迹...

这是大妈在 **ZoomQuiet** 的第**003**篇原创


-------------
## 背景
新冠肺炎(2019-nCoV/NCP/SARS-CoV-2->COVID-19) 被爆发;
而且正式名称也随着分析的深入而变来变去,
唯一不变的, 只是生活, 我们还得继续.

-------------
## 现象
那么, 既然去公共场合就有被传染或是被感染的可能,

所以, 大家不得被根据国家要求, 推迟复工;

而有条件的高科技企业, 自然全体进入`SOHO`(Small Office Home Office)远程办公状态;

而学校的办公后果是, 小学生们创造性的发明了:

    五星好评
    分期付款

竟然令若大一家企业头痛不已, 不得不想尽办法求饶, 以免相关应用在市场排名跳崖.


-------------
## 问题
俺的直觉, 其实这个方向的问题, 也可以化为灵魂三问:

- 远程办公是什么?
- 远程办公想解决什么问题?
- 远程办公能解决这些问题嘛?


-------------
## 分析

> 远程办公:

- 望文生义: 
    + 双方不在同一个物理空间中
    + 通过远程进行办公
- 其它问题都是在这个形式上引发的

> 远程办公可以解决的问题:

- 昂贵的办公空间成本
- 昂贵的通勤时间成本
- 痛苦的分居/迁移等适应成本
- ...


互联网/移动互联网/物联网/... 现在网络技术/工具/硬件/服务/...如此发达,
优秀的远程协作软件这么多,

为什么, 被迫大规模进入远程办公时爆发出这么多不适应?

-------------
## 思索
> 先限定讨论范畴: IT 行业, 软件开发为核心的企业; 其它行业/形态的企业没深入过, 也就没发言权.

首先, 远程协作这事儿, 原本就存在, 甚至于是主流:

- 在 `FLOSS(自由开源软件)` 创始时, 互联网早期, 就已经是常态了
- 那时的网络只能通过电话线拨号进入, 速度只有 56k/s 
    + 即便没有任何干扰, 永远以最高速度下载
    + 我们现在通过云盘10分钟下载到的蓝光电影文件
    + 当年就算整整两天都不一定下载的到(8G左右 .mkv)
- 而技术社区已经形成了成熟的远程协作流程:
    + 通过邮件发布代码的补丁文件
    + 协作者通过邮件下载到补丁
    + 然后和本地代码合并, 解决冲突, 然后继续开发
- 这种基于文件 diff 记录进行的远程同步操作非常稳定
    + 只是比较繁琐 -> 几个文件还好,要是成千上万, 一次几千个文件发生了变化时...
    + 所以, 人们设计开发了 cvs 工具
    + 并维护社区的中央代码版本仓库, 帮助大家快速从主版本仓库进行自动化版本合并
- 之后的 SVN 等版本管理系统都根据这种 `先提交再合并` 的思路来完成协作流程的
    + 但是, 这样一来造成大家所有对版本相关的操作
    + 都要远程访问中央仓库, 这给主仓库告成了很大压力
    + 也无形中降低了协同效率
- 所以 Darcs/Bazaar/Mercurial 等等分布式版本管理系统(DVCS)
    + 将所有历史版本分散保存在所有工作复本所在的开发者本地
    + 只是, 虽然一些版本操行就可以在本地完成了
    + 可惜, 进行协同时, 还是习惯的进行  `先提交再合并` 
- 直到伟大的 GitHub 创造性的发明了 `Pull-Request` 模式
    + 即,  `先合并再提交` 流程
    + 这才极大的降低了一个开源项目的管理成本
    + 令每一位有想法, 有能力的开发者, 可以不用和项目管理团队先打好交道, 才能获得提交权
    + 而是, 随时可以提交合并请求
    + 将一个项目的协作大规模的扩大了
- 然后, 围绕 GitHub 从发布之初就公开出来的, 设计非常合理, 功能非常友好的接口
    + 产生越来越多的协作支持工具/扩展/服务/思路/...
    + 甚至于专业服务公司, 提供对应产品来帮助大家更好的使用 GutHub 生态
- 而这一演化进程, 至少有37年了...
    + 也就是说, 对于开发者, 在 `FLOSS(自由开源软件)` 社区中
    + 天然的一直就在基于远程协作来推进社区项目的开发
    + 而且, 围绕这一现实形成的文化/工具/流程/...早已完备/稳定/高效


那么, 一样是以软件开发为核心行为的 IT 企业为什么并不都能很好的适应远程办公?

### 什么是办公?
> 答案很明显了...问题在办公, 而不是远程


远程协作的一系列工具, 多数是基于协作开发而形成的;

- 可惜, 办公并不等于开发;
- 一个健康的企业, 也不可能只由开发人员组织
    + 嗯哼? 还真不一定, 有大量只有开发者形成的小微企业
    + 多数也都算健康...
    + 好吧, 这个话题不展开
- 而且, 中国的 IT 企业, 无论创始人是否技术出身
    + 能生存至今的, 现在也都不约而同的不以技术为驱动了
    + 多数以销售/产品/服务/... 或是宣传的, 以用户为核心来驱动

那么, 当公司内部管理职级是以非技术/开发为核心组建起来时
,沟通就变成了一种很魔幻的行为:

- 高层的多数沟通习惯:
    + 我知道你不知道我不知道
    + 但是, 我知道如何令你以为我知道
- 中层的多数沟通习惯:
    + 我知道我不知道你知道的
    + 但是, 我知道令你以为我知道是我的使命
- 一线开发者就只能:
    + 我知道你不知道我知道的
    + 而且, 我知道你也不想知道我知道的
    + 但是, 我知道我必须实现你以为你知道的


因为, 这时所有环节上的交流, 基于的不是可运行/可调试/可比较/可追溯/...确定意义的代码;
而是各个方向涌过来的不确定性/可能性/猜想/...纠缠而成的决策;

而且, 大家出于自我保护心理, 也都下意识的尽可能将阐述模糊化,
这样无论结果如何, 自己都有推脱的操作空间.

所以, 这时的沟通, 只能通过当面进行:

- 用表情/用手势/用姿态/用语调/... 用各种表演艺术功力来传递压力
- 同时, 无法产生合理的共识和方案
- 因为, 多数会议时, 没有人知道真正发生了什么, 什么问题引发的, 以及对应解决方法
- 也就是大妈经常说的断言:
    + 如果一件事儿, 用文字无法描述清晰
    + 那么, 只能说明这事儿, 还没想明白
- 因为, 文字不过是线性/结构化的思想, 或是语言
    + 没理由, 这事儿只能通过当面口头完成传达
    + 其它隔了网络, 通过文字/图形就无法传达
    + 这又不是咒语, 必须通过有灵力的人当面用语言从背景能量中激发


### 远程办公之殇
> 如果从这个偏见出发, 就大体能明白现在 IT 企业远程办公的困难了

- 远程办公流畅, 将发现自组织起来的工程师们, 其实用不上中层
- 远程办公困难, 则证明现在的中层, 难以适应未来的办公模式
- 这简直就是 `22条军规` 哪...

好在, 经过和产品经理 PK 这么多年, 
技术人员们也都发现了这个世界的规则:

- 必须有能说人话的人, 去和开发之外的各种角色协调, 作为防波堤
    + 否则, 将永远无法开发真正有用的功能, 
    + 只能, 永远在没有逻辑依据的妄想式功能上想办法来自我证明技术实力
- 所以, 被远程办公时, 技术人员需要加强的并不是远程协作能力
- 而是远程表演能力
    + 通过语言/文字, 也能令经理们感受的到我们顺从的态度
    + 以免会议时间无端延长, 以便经理们展示压力
    + 自己又得在家中加班漏夜调试代码才能赶上进度...


嗯哼, 将将 4200 字了,
先将企业被远程办公时俺的偏见说完;

而其它远程办公的有关话题, 比如:

- 开源技术社区中的大规模远程协作,
- Indie Hacker 们长期 SOHO 时的心法修炼...

再找机会聊了, 或是看转载/引用/在看数量是否能超过42, 俺就先续上大家更加有兴趣的部分.


-------------
## refer.

- [FLOSS , Free and open\-source software \- Wikipedia](https://en.wikipedia.org/wiki/FLOSS)


文中链接感谢["文章助手"的助手](https://linux.cn/static/tools/a.html) 的支持,
(来自 [LINUX中国]((https://linux.cn/article-11850-1.html)) 的小应用)

- 可以点击, 将自动复制对应链接到剪贴板
- 然后打开浏览器, 复制到地址栏访问


JD 下单链接 -> 点击后再打开浏览器复制到地址栏访问 -> 俺能获得少许佣金:

有关软件工程中管理和被管理者的关系, 推荐几本好书:

- [人月神话(40周年中文纪念版)](https://union-click.jd.com/jdc?e=&p=AyIGZRhaFgsaB1MfXRAyEgRQGlsTBxo3EUQDS10iXhBeGlcJDBkNXg9JHU4YDk5ER1xOGRNLGEEcVV8BXURFUFdfC0RVU1JRUy1OVxUBFwZVHV4dMlJdDEAOFEdxZQlLL0N6TkUeYzBtcGILWStaJQITBlYZWBYAEABlK1sSMkBpja3tzaejG4Gx1MCKhTdUK1sRCxEBVBlaFwMQD1ErXBULImwLRQd1RkpTECtrJQEiN2UbaxYyUGlSGA5AURpQAkwJQlcXBlFPC0AHRgAAGQ5FAkVXXExYHDIQBlQfUg%3D%3D)
    + 如果能看原文还是看原著->[人月神话(英文版)](https://union-click.jd.com/jdc?e=&p=AyIGZRhaFgsaB1MfXRAyEgZXH14QBRc3EUQDS10iXhBeGlcJDBkNXg9JHU4YDk5ER1xOGRNLGEEcVV8BXURFUFdfC0RVU1JRUy1OVxUDEANQHlwQMk8OJ3sdXANPZShLGUBRUmAdUw5AcUQLWStaJQITBlYZWBYAEABlK1sSMkBpja3tzaejG4Gx1MCKhTdUK1sRCxEBVBlaEQATBVwrXBULImwLRQd1RkpTECtrJQEiN2UbaxYyUGlSGA5AURpQAkwJQlcXBlFPC0AHRgAAGQ5FAkVXXExYHDIQBlQfUg%3D%3D)
- [软件随想录:程序员部落酋长Joel谈软件](https://union-click.jd.com/jdc?e=&p=AyIGZRhaFgsaB1MfXRAyEgZUHFkdBBM3EUQDS10iXhBeGlcJDBkNXg9JHU4YDk5ER1xOGRNLGEEcVV8BXURFUFdfC0RVU1JRUy1OVxUDEwBXE10UMhEdEn4SVnZhZRRtDQ8AEFsrQj5OXEQLWStaJQITBlYZWBYAEABlK1sSMkBpja3tzaejG4Gx1MCKhTdUK1sRCxEBVBlbEwQSAl0rXBULImwLRQd1RkpTECtrJQEiN2UbaxYyUGldSw4QUBMEVUhTEwIXAQZPUhVWFQZQGg4dVhEFB0lSRzIQBlQfUg%3D%3D) ~ 真正的一线软件工程师的内心...
- [重构－改善既有代码的设计(中文版)](https://union-click.jd.com/jdc?e=&p=AyIGZRtSFQASAVIfXxIyFQJXHFkTBhUBUBNrUV1KWQorAlBHU0VeBUVNR0ZbSkdETlcNVQtHRVNSUVNLXANBRA1XB14DS10cQQVYD21XHgBQGVwXBBYAUx5TJQpncjNZQWVEcQIrGyxTBGoEHB0aD0QeC2UaaxUDEwRXGFgXABU3ZRtcJUN8B1QaXxMLEwRlGmsVBhsEUxpZFwEWDlQfaxICGzc%2BRQVJYlZfAV5rJTIRN2UrWyUBIkU7TwkTV0IGVU9ZEQYTAgBIUkUGEQAGEl0XAxFSB05cFVUiBVQaXxw%3D) ~ 熊节老师翻译的精品
    + 如果能看原文还是看->[重构 改善既有代码的设计 英文版](https://union-click.jd.com/jdc?e=&p=AyIGZRhaFgsaB1MfXRAyEgdcGF4QChY3EUQDS10iXhBeGlcJDBkNXg9JHU4YDk5ER1xOGRNLGEEcVV8BXURFUFdfC0RVU1JRUy1OVxUCGwRQHlMRMltDCH8ZFkBXYj1lCX5hUgRQZRx%2BXEQLWStaJQITBlYZWBYAEABlK1sSMkBpja3tzaejG4Gx1MCKhTdUK1sRCxEBVBlZEgESB1UrXBULImwLRQd1RkpTECtrJQEiN2UbaxYyUGkBSV1AUhMHARlfEQMXUgYSCxEBFVRcHVkUAUdVABxbQjIQBlQfUg%3D%3D)


-------------
## PS:
`新冠肺炎(NCP)正确应对姿势` 系列之后被读者触发的两个系列:

- 为什么就是不愿意上班?
- 科学'摸鱼'指北

都已完结,虽然分散在各个公众号中...

接下来将尝试什么, 俺也没计划, 想哪儿怼哪儿了;

欢迎大家留言触发其它 `有用/有趣/有种` 的系列话题.

-------------
>> NN 3934

好文笔,感叹号年度配额: **1/3**

-------------

ZoomQuiet/**大妈**

就是四处 `是也乎,(￣▽￣)` 的那个大妈:


- 私自嗯哼: ZoomQuiet (订阅号 **ZoomQuiet42**)
- 公开课程: **蟒营** (订阅号: Mainium)
- 全国大会: PyChina (订阅号: PyChinaOrg)
- 本地社区: 
    + GDG珠海 (订阅号: GDG-ZhuHai)
    + TFUG珠海 (订阅号: ZH_TFUG)
- 历史吐糟: Chaos42 (订阅号 PythoniCamp)

-------------



