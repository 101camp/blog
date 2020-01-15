# TS:7尝试小众模块 pysrc/fractal, 配置隔离环境

## 背景
- 因聚会主题演讲触发,希望试用小众画图模块 [pysrc/fractal: Draw fractal image by python.](https://github.com/pysrc/fractal).
- 此模块在 github 上,截止 2019 年也只有 17 个 stars,并非常规模块.
- 直觉上,尝试小众模块时,应该与系统环境隔离.
- 前置条件
    + 俺的配置,macOS Mojave/ 10.14.4.
    + 已成功安装 pyenv, 并检验过.

## 目标
- 配置 1 个专门用来尝试 fractal 的环境.

## 分解
- 查一下自己已经有的工程环境
    + 是否有 1 个纯净的版本环境可供复制?
- 查一下 pysrc/fractal 使用 python3 还是 2
- 创建适合 pysrc/fractal 的版本环境

## 记录
- 纯净的母环境
    + 首先,查看俺已有的虚拟环境们,并查看其中是否存在纯净的母环境?
        + 纯净母环境方便衍生新的虚拟环境.
    + 判断: 似乎有 1 个纯净环境 -> `3.7.4`,那么接下来就是复制该环境...

```
$ pyenv versions
* system (set by /Users/zsy/.pyenv/version)
  3.7.4
  3.7.4/envs/374blog
  374blog
```

- 复制
    + 从纯净的 3.7.4 母环境中复制出新的环境,并给其命名
    + `$ pyenv virtualenv 3.7.4 figure`
    + `3.7.4` 是纯净的母环境
    + `figure` 是俺想要创建的新环境,俺给其命名为 `figure` 
        * 即,在此环境下,俺一般喜欢干画图的事...
- 切换
    + 从母环境切换到刚刚创建的特殊环境 `figure` 里
    + `$pyenv local figure`
- 配置
    + 在 `figure` 环境下,安装俺常用的画图 module
    + `$ pip3 install fractal`
- 目录
    + 但是这过程里,俺十分迷惑的是, **pyenv 到底在哪个目录下有效?**
    + 俺这次是直接在画图的工作目录下,绑定 `figure` 环境;
    + 但是当切换到新的工作目录时,怎么复制 `figure` 环境呢?


```
$ cd zsy.fractal
(figure) zsydeMacBook-Air:zsy.fractal zsy$ python3
Python 3.7.4 (default, Nov 15 2019, 12:23:31) 
>>> from fractal import Pen
>>> 
```

## Refer
- [debuguself.github.io/2018-07-30-pyenv101.md at master · DebugUself/debuguself.github.io](https://github.com/DebugUself/debuguself.github.io/blob/master/_posts/scm4du/2018-07-30-pyenv101.md)
- [TS3: Pyenv 最终介绍 — Blogging 蟒营™ 博客](https://blog.101.camp/TS/190919-pyenv-finally-intro/)
- [191006_pyenv-usage_20-00-50_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili](https://www.bilibili.com/video/av77693412?from=search&seid=6335516483445440874)
- [pyenv/pyenv-virtualenv: a pyenv plugin to manage virtualenv (a.k.a. python-virtualenv)](https://github.com/pyenv/pyenv-virtualenv)
- [pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)
