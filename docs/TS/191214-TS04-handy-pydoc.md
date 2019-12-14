# 远山近水 pydoc

## 手边的 pydoc

- 蟒营的预备练习是 Learn Python the Hard Way.
- 有学员发现,在 ex12 练习的附加题里面有这样一个题目：


> 使用 `pydoc` 再看一下 `open`, `file`, `os`, 和 `sys` 的含义。看不懂没关系，只要通读一下，记下你觉得有意思的点就行了。


- 学员尝试 `$ pydoc os` , 居然发掘出意想不到的帮助文档.

```
Help on module os:

NAME
    os - OS routines for NT or Posix depending on what system we're on.

FILE
    /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/os.py

MODULE DOCS
    http://docs.python.org/library/os
```

- 原来 pydoc 就是 python 内置的帮助文档模块.
- 其可爱之处在于,不仅能够直接在终端以文本形式查看,且组织方式简洁语言风格浅显.
- 是小白最爱的内容少深度浅的好文档,手边拿起就能用.


## pydoc 如何用?

- 只需告诉 pydoc 你想查点啥 `pydoc <name> ...`,比如想知道转换日期的好东西有哪些,直接输入 `$pydoc datetime`.
- 终端便会返回与日期相关的模块/函数,以及简要解释,类似常见的 cheatsheet.
- 比如,仅通过肉眼浏览,就可以快速分辨出,转换日期有把周一设定为第 1 天的,也有把周日设定为第 1 天的.

```
$ pydoc datetime
Help on module datetime:

NAME
    datetime - Fast implementation of the datetime type.
...    
     |  isoweekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |  weekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
...    

```

- 是不是一目了然?是不是下班就想试一试?

## 远山近水

- 学习时,探索往往是漫长而枯燥的.
- 有一种流行看法是,只要使用了 5W1H 即可有效管理探索过程.
- 认为将如下问题提前想清楚,就能心中有数避免时间的虚耗.
- 但也有学员补充道,「只是心中有数显然是不够的。人的注意力是非常涣散的，有点什么事情就会被牵扯着找不到方向.」
- 简单说, 搜索最好的结果始终是解决的问题.那么,有没有什么方法能够助力解决问题呢?
- 当然,及时记录形成笔记,固然是个好习惯.还有呢?
- 此处推荐,`在官方文档搜索有效答案` .比如,pydoc 的结构简洁论述完备,比某问答论坛可是方便太多.
- 比起漫无边际的互联网,把时间用在技术人员精心准备的官方档案上,可能更加聪明.
- 也许解决问题的开关,往往藏在脚下的水流,而非远处的群山.

## refer
- [[FAQ] 好奇心的边界~试论学习时值得挖掘的边界在哪儿? (#13) · Issues · 101Camp / 4py / tasks · GitLab](https://gitlab.com/101camp/4py/tasks/issues/13)
- [[LPTHW]e12->No Python documentation found for 'file'. (#10) · Issues · 101Camp / 4py / tasks · GitLab](https://gitlab.com/101camp/4py/tasks/issues/10)
- [LPTHW/e15.md · liliang_89 · 101Camp / 4py / tasks · GitLab](https://gitlab.com/101camp/4py/tasks/blob/liliang_89/LPTHW/e15.md#2019-11-23-211729-study-drills)

