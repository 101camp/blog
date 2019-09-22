# TS3: Pyenv 最终介绍
> Tech Soup ~ 技术鳮汤 ;-)

期望这篇解决所有 Pyenv 核心困惑.
## snip

Pyenv 是 `Python 项目环境隔离/控制器` , 最基本的使用:

- 基于官方仓库安装:
    + `$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv`
- 然后配置到环境中:
    + `$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile`
    + `$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile`
- 接着就可以自由控制运行时环境了:
    + 安装目标版本,比如: 
        * `pyenv install 2.4.2`
    + 复制一个项目环境:
        * `pyenv virtualenv 2.4.2 242proj`
    + 设定当前目录以内默认使用新环境:
        * `pyenv local 242proj`

就以上三个环节的配置, 就可以完成:

- 自由安全安装系统无关, 自用 Python 版本环境
- 根据不同项目, 自由安全绑定不同 Python 运行时
- 根据同类项目, 自由绑定含有相同 pip 模块依赖树的Python 运行时

## background
> 为什么有 Pyenv 等等环境控制工具?


大家开始学习 Python 时, 可能最惊讶/震惊/自豪 的发现就是

- 大部分操作系统, 都内置了 Python 运行环境
- 也就是说, 不用我们专门安装, 从买到电脑那一瞬间开始
- 其实, 我们都有一个完备的可用 Python 版本环境了


因为, Python 太好用, 无论哪个系统厂商, 都有大量的内置工具/软件依赖 Python

- 所以, 也都预先安装了...
- 那么, 这也就带来一个问题:
    + 系统 Python 环境, 是很多系统依赖软件需要的环境
    + 这一环境, 肯定不能轻易破坏, 否则, 引发系统崩溃
    + 那就等于我们自己杀死了自己的电脑...
- 这其实, 也是很多教程中涉及安装 Python 模块时
    + 有的, 不负责的提示使用 `sudo` 命令
    + 这是临时将用户权限提升到系统管理员的指令
    + 造成的后果, 是一般人难以控制的
    + 当然, windows 系统本身是单人系统,并没有严格区分系统和用户权限
    + 所以, 在 windows 中看起来可以自由使用系统 Python 环境来开发学习
    + 其实, 只是另外一种慢性自杀而已

## problems
![](https://ipic.zoomquiet.top/2019-09-22-xkcd-1987-pyenv.gif)

由于 Python 发展太久, 中间有太多意外决策, 同时开源项目又不禁止大家的探索...

所以, 现在任何系统中的 Python 运行时环境都可以混乱不堪...

正如 [xkcd: Python Environment](https://xkcd.com/1987/) 所描述的那样...


但是, 对于正常学习/使用者而言, 一般只想解决几个问题:

- 和系统环境隔离
    + 运行 Python 时, 不触及系统自身依赖的s
- Python 版本隔离
    + 想用哪个版本的 Python 不用担心干挠谁
- 项目模块依赖隔离
    + 不同项目之间用 pip 安装的模块相互独立
    + 可以分别自由升级/降级/删除/...
    + 而不干挠各自的开发/运行

那么, 在很多年探索后, Pyenv 正好是解决以上问题的那个工具

## Pyenv
正如项目名称一样:

- **Py**thon
- **env**ironment

`Python 环境` ~ 控制器, 控制了核心两种环境:

- Python 版本环境, 也就是说, Python 2.1/3.1 这种大版本
- Python 运行时模块依赖环境, 也就是说, 具体项目中依赖的第三方一大堆模块


那么, 如何最短手续就进入 Pyenv 的世界享受可控 Python 环境?


### pyenv-installer
[pyenv/pyenv-installer: This tool is used to install `pyenv` and friends.](https://github.com/pyenv/pyenv-installer)

首次安装, 建议使用官方提供的安装器

- 不用管 homebrew 哪什么其它东西, 那些和 Pyenv 并无直接关系
- 何况 brew 在中国, 还是很不受到待见的...那速度哭吧...

如何检验 pyenv 安装成功?


$ env | grep pyenv

    PYENV_ROOT=/指向/你/的/.pyenv
    PATH=...:/指向/你/的/.pyenv/shims:/指向/你/的/.pyenv/bin:...

> 用 env 检验系统环境变量中包含 pyenv 要求的两个关键性配置



$  pyenv

    pyenv 1.0.3-535-g17f44b7c
    Usage: pyenv <command> [<args>]

    Some useful pyenv commands are:
       commands    List all available pyenv commands
       local       Set or show the local application-specific Python version
       global      Set or show the global Python version
       shell       Set or show the shell-specific Python version
       install     Install a Python version using python-build
       uninstall   Uninstall a specific Python version
       rehash      Rehash pyenv shims (run this after installing executables)
       version     Show the current Python version and its origin
       versions    List all Python versions available to pyenv
       which       Display the full path to an executable
       whence      List all Python versions that contain the given executable

    See `pyenv help <command>' for information on a specific command.
    For full documentation, see: https://github.com/pyenv/pyenv#readme

> 运行 pyenv 给出标准使用帮助


这样, 就说明安装好了

### pyenv-virtualenvwrapper
[pyenv/pyenv-virtualenvwrapper: an alternative approach to manage virtualenvs from pyenv.](https://github.com/pyenv/pyenv-virtualenvwrapper)

安装 Pyenv 当前是想用多版本 Python 环境了,那么,一定要安装这个插件

安装非常简单:

    $ git clone https://github.com/pyenv/pyenv-virtualenvwrapper.git $(pyenv root)/plugins/pyenv-virtualenvwrapper

就一个 git clone 操作,然后也配置到系统环境中:

    export PATH="~/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

在原先 pyenv 之后追加一行, 启动 `virtualenv-init` 就好;

### 系统环境
已经见到这个词很多次了, 但是, 多数文档并不说明这是什么东西...
导致 Pyenv 一直没使用起来....

系统环境 -> System **env**ironment

- 是的, 就是刚刚用 `env` 指令汇报出来的, 当前系统运行时使用的所有 `全局配置`
- 因为是系统当前在用的, 所以, 一定是有一种仪式/指令来更新的
- 不可能我们自行修改/自动化变更了 `~/.bash_profile` 之类系统配置文件就能自动加载的

这个仪式指令就是:

    $ source ~/.bash_profile

`source` ~ 资源

- 是的, 这个资源指令, 就是加载系统所有资源的指令
- 如果安装 Pyenv 后, 从来没执行过这个指令,
- 那只有下次电脑重启时,才可能真正加载上 pyenv 


### Common build
> 最大的坑来了...

[Common build problems · pyenv/pyenv Wiki](https://github.com/pyenv/pyenv/wiki/Common-build-problems)

在官方wiki 第一条, 就是这篇文章, 为什么?

- 因为我们想 Python 版本环境自由, 又想和系统隔离
- 那么, 必然不可能简单复制系统即有环境来用
- 只能, 自行编译全新 Python 来给自己使用
- 问题来了: 现场编译一个 Python 版本出来, 依赖什么东西?
- 直觉上, 当然需要额外的支持了...
    + 毕竟 Python 是用 C 语言编写的
    + 而 C 软件的编译, 需要一堆相关依赖模块的源代码支持
    + 否则, 编译是无法开展的...
- 这也是为什么很多人安装 Pyenv 后却无法安装新 Python 版本的根本原因:
    + 巧妇难为无米之炊
    + Pyenv 再智能, 也不可能替 Python 无中生有出来系统关联的第3方模块源代码

好在, Python 编译时依赖的都是通用基础模块,
无论哪个系统, 都有对应开源仓库可以快速安装;

对于 macOS 只需要:

    $ brew install openssl readline sqlite3 xz zlib

只是, 前提是事先配置好 XCode Command Line Tools:

    $ xcode-select --install

因为, 所有编译工作, 其实是使用 XCode 来进行的, 否则,无法兼容 macOS 环境哪...


### usage
好了, 以上准备工作完成了, 其实就3步:

- 安装 pyenv, 以及 pyenv-virtualenvwrapper 插件
- 检验, 并激活 Pyenv
- 准备当前编译环境


那么接下来的使用就异常顺滑了;-)

安装新 Python 环境:

    $ pyenv install --list
    Available versions:
      2.1.3
      2.2.3
      2.3.7 

      ...
      
      stackless-3.4.7
      stackless-3.5.4

看看 pyenv 支持多少种版本环境的安装? 上百种了, 这是其它工具作不到的

安装 Python 3.7.4 环境:

    $ pyenv install 3.7.3
    python-build: use openssl@1.1 from homebrew
    python-build: use readline from homebrew
    Downloading Python-3.7.3.tar.xz...
    -> https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
    ....


检验安装结果:

    $ pyenv rehash
    $ pyenv versions
    * system
      3.7.3

> 注意:

`* system` 说明当前目录使用系统 Python 环境中...

复制一个项目环境:

    $ pyenv virtualenv 3.7.3 373camp
    Looking in links: /var/folders/pl/8rsjzmjn2ybgd71lwqf3lxw80000gn/T/tmp_qtmj124
    Requirement already satisfied: setuptools in /Users/zoomq/.pyenv/versions/3.7.3/envs/373camp/lib/python3.7/site-packages (40.8.0)
    Requirement already satisfied: pip in /Users/zoomq/.pyenv/versions/3.7.3/envs/373camp/lib/python3.7/site-packages (19.0.3)

因为, 这个 3.7.3 环境是干净的单纯 Python 自身, 作为母本,
来复制出其它项目中环境才是正确的思路;

> 同时, 也因为 pyenv 复制已经安装好的环境是不用编译的, 非常快.

检验复制结果:
    $ pyenv versions
    * system
      3.7.3
      3.7.3/envs/373camp

绑定到当前目录:

    ༼system༽~/mnt/_historic/101.camp/_video༽
    ༄  pyenv local camp373
    ༼camp373༽~/mnt/_historic/101.camp/_video༽
      system
      3.7.3
      3.7.3/envs/373camp
    * camp373 (set by /Users/zoomq/mnt/_historic/101.camp/_video/.python-version)

> 这里出现的奇怪提示, 是大妈本地 bash 配置的特殊命令行提示结构, 不必关心...

关键是 `* camp373` , 那个 `*` 从 system 移动到 `camp373` 之前,
说明当前运行时环境, 已经从系统默认, 变成刚刚复制出来的一个全新 Python 3.7.3 环境了,

而实际上这一环境编译安装在:

    /Users/zoomq/.pyenv/versions/camp373

和系统的以及 brew 安装的都不相同.


> 注意:

千万别轻易使用: `pyenv global 指定版本别名`

这是将 系统 Python 运行环境切换到 pyenv 安装的环境上...
太危险了...



## summary
以上, 简单说:

- Python 运行时环境是开始学习/开发/测试前一定要关注的
- 而 Pyenv 提供了统一简洁的指令工具, 可以快速任意:
    + 安全安装不同 Python 版本环境
    + 并基于 virtualenv 以 pyenv-virtualenvwrapper 形式提供了一系列包依赖控制
        * 支持我们快速对不同项目的不同模块依赖
        * 也可以友好/安全的完成隔离
    + 更加精彩的是, 完成配置后 pyenv 将自动切换对应环境
        * 这样, 我们进入对应项目目录时
        * 根本不用担心运行时环境没有绑定上
    + 这一切, 最终 pyenv 只非常自制的使用
        * 目录中 `.python-version` 文件来完成辅助识别并自动切换
        * 其内容也就是 `camp373` 这种我们自行拟定的环境别名而已


### TS;DL
> 那么 Pipenv/Anaconda/... 其它工具呢?

Python 生态最好也最纠结的一个状态就是:

- 任何一个问题都有很多优秀解决方案
- 而且, 每一个都看起来佷优秀
- 导致我们无论选择了哪一个都好象放弃了整个儿世界似的...

好在各个开源项目的文档/示例都很友好, 也有大量对比文章可以参考,

俺的私人偏见:

- virtualenv 最早完成环境虚拟化;
    + 但是, 运行环境和项目目录绑定, 并得用指令进入/退出
    + 整体上, 不够灵活
- Anacoda/Miniconda 是通用预部署环境工具
    + 如果我们需要快速获得上百个第三方大型模块已经有的环境
    + 那么, 使用 Anacoda
    + 否则, 不如用 Pyenv
    + 当然, 想节省 Python 版本环境的编译
        * 可以安装 Miniconda 来替代 Pyenv 的 install Python 过程
        * 然后, 在 conda 版本环境中, 用 Pyenv 来管理项目模块依赖环境
    + 问题是, conda 环境的进入/退出, 必须用指令来完成
    + 而且, 进入后, 运行 Python 也不是直接用
    + 而是必须 `conda run python 我的脚本.py` 这种
    + 比较傻....
- Pipenv 从名字上来看就知道专注 pip 的管理
    + 虽然, 对项目模块状态管理更加灵活
    + 但是, 进入/退出, 必须人工指令
    + 而且, 在环境中运行, 也必须用 `pipenv run python 我的脚本.py` 这种形式
    + 当然, 也有人反感 Pyenv 这种自动切换环境的行为, 认为不可控
- venv 这是 Python 3 only 的官方内建虚拟环境工具
    + 没人用...
- poetry 也是类似 pipenv 的包依赖控制工具, 不包含 Python 版本环境管理


## refer:

- [怎么才能放飞自我的玩儿Python · Yixuan](https://yixuan.li/geek/2018/07/31/pyenvVirtualenv/)
- [pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)
    + [pyenv/pyenv-installer: This tool is used to install `pyenv` and friends.](https://github.com/pyenv/pyenv-installer)
        * [Home · pyenv/pyenv Wiki](https://github.com/pyenv/pyenv/wiki)
        * [Common build problems · pyenv/pyenv Wiki](https://github.com/pyenv/pyenv/wiki/Common-build-problems)
    + [自分の為のpython環境設定まとめ\[mac\]\[ubuntu\] - Qiita](https://qiita.com/miyamotok0105/items/55a828070b6d6abc1a7c)
    + [pyenv と pyenv-virtualenv で環境構築 - Qiita](https://qiita.com/Kodaira_/items/feadfef9add468e3a85b)
    + [Plugins · pyenv/pyenv Wiki](https://github.com/pyenv/pyenv/wiki/Plugins)
        * [pyenv/pyenv-virtualenvwrapper: an alternative approach to manage virtualenvs from pyenv.](https://github.com/pyenv/pyenv-virtualenvwrapper)
    + [An Effective Python Environment: Making Yourself at Home – Real Python](https://realpython.com/effective-python-environment/)
- [python - What is the difference between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc? - Stack Overflow](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe/41573588#41573588)
- [Pocket: Simplify Your Python Developer Environment](http://scm.zoomquiet.top/data/20190323095254/index.html)
    + [My Python Development Environment, 2018 Edition | Jacob Kaplan-Moss](https://jacobian.org/2018/feb/21/python-environment-2018/)
    + [Pyenv+Virtualenv+Virtualenvwrapper轻量级python环境管理 - S.Mona](https://silbertmonaphia.github.io/pyenv+virtualenv+virtualenvwrapper%E8%BD%BB%E9%87%8F%E7%BA%A7python%E7%8E%AF%E5%A2%83%E7%AE%A1%E7%90%86.html)
 

### env

![](https://ipic.zoomquiet.top/2019-09-18-ScreenFetch-zq-mac-env.jpg)

俺用 Pyenv 控制的环境:


    ༄  pyenv versions
      system
      2.7.10
      2.7.10/envs/uC2710
      2.7.12
      2.7.12/envs/dama2712
      2.7.15
      2.7.15/envs/leo2715
      3.6.3
      3.6.3/envs/AI363
      3.6.3/envs/DU363
      3.6.3/envs/du4pos
      3.7.0
      3.7.0/envs/leo370
      3.7.3
      3.7.3/envs/373camp
      3.7.3/envs/Django373
      3.7.3/envs/camp373
      3.7.3/envs/pycon373
      373camp
      AI363
      DU363
      Django373
    * camp373 (set by /Users/zoomq/mnt/_historic/101.camp/_video/.python-version)
      dama2712
      du4pos
      leo2715
      leo370
      pycon373
      uC2710

## PS:
蟒营(101.camp): 

    伴你重享学习乐趣
    Reactivate Joy by Self-teach with You

- 所以, 不仅仅是 Python ,
- 马上将用蟒营形式发布写作课程,
- 欢迎大家参与体验,
- 用7+1周时间
    + 重新获得写作的乐趣
    + 以及一组高效出品习惯


## PPS:
> 当前课程对应公众号 蟒营101camp 暂定专栏有:

- DM 大妈嗯哼 ~ 文本快速呢喃点心境...
- NC 嗯哼蟒营 ~ 图文/图片有关课程信息
- SS 学员故事 ~ 各期课程中发生的真实"血案"
- TS 技术鳮汤 ~ 转载/原创自学技术/心法相关嗯哼


欢迎投稿, 邮件给课程组就好:

    guru101camp@googlegroups.com

>> NN 3740



