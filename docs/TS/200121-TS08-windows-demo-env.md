# TS:08 为了部落,再搞 Windows
> 重新体验 windows 环境中的无奈...

## 背景
> 主力桌面系统私人历史

- 半年 -> win3.2 
- 4年 -> win95 
- 2年 -> XP 
- 5年 -> NT server 
- 6年 -> Ubuntu 
- 至今 -> macOS

所以, 运营
[蟒营™ Python 入门班](https://py.101.camp/)
时对所有日常系统中学员的反应都是有自信的...

> 但是, 没想到...

## 目标
> 需要一个基本可用的 windows 环境来截屏录像, 比对演示很多日常常识性操作

- 嘦 windows , 哪个版本都可以
- 有 git
- 有 类似 Notepad++ 那种反应快速稳定的编辑器
- 有 ssh 支持, 以便无口令访问 gitlab 仓库


## 折腾
> 看起来目标很少吧? 但是, 没想到...

### 设想

日常是 macOS, 硬盘不大, 不想寄生一个 windows 浪费空间;
也不愿专门为临时演示浪费一台硬件, 只安装 windows;

所以, 理想状态:

- 内网一台 miniPC , Ubuntu 18.04 系统,作为宿主机
    + 通过 VirtualBox 来安装 Windows 子系统
    + macOS 通过 VNC 访问远程桌面中 VirtualBox 拉起的 Windows
- 这样, macOS 桌面本地不消耗任何资源
    + 可以随时调用
    + 也可以随时挂起
    + 同时, 也不消耗内网服务器的过多资源


### 环境

$ screenfetch

                              ./+o+-       zoomq@i3SPAM
                      yyyyy- -yyyyyy+      OS: Ubuntu 18.04 bionic
                   ://+//////-yyyyyyo      Kernel: x86_64 Linux 4.15.0-74-generic
               .++ .:/++++++/-.+sss/`      Uptime: 1d 7h 39m
             .:++o:  /++++++++/:--:/-      Packages: 2204
            o:+o+:++.`..```.-/oo+++++/     Shell: bash 4.4.20
           .:+o:+o/.          `+sssoo+/    CPU: Intel Core i3-7100U @ 4x 2.4GHz [27.8°C]
      .++/+:+oo+o:`             /sssooo.   GPU: intel
     /+++//+:`oo+o               /::--:.   RAM: 2431MiB / 7848MiB
     \+/+o+++`o++o               ++////.
      .++.o+++oo+:`             /dddhhh.
           .+.o+oo:.          `oddhhhh+
            \+.++o+o``-````.:ohdhhhhh+
             `:o+++ `ohhhhhhhhyo++os:
               .o:`.syhhhhhhh/.oo++o`
                   /osyyyyyyo++ooo+++/
                       ````` +oo+++o\:
                              `oo++.

$ apt show virtualbox

    Package: virtualbox
    Version: 5.2.34-dfsg-0~ubuntu18.04.1
    Priority: optional
    Section: multiverse/misc
    Origin: Ubuntu
    Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
    Original-Maintainer: Debian Virtualbox Team <team+debian-virtualbox@tracker.debian.org>
    Bugs: https://bugs.launchpad.net/ubuntu/+filebug
    
    ...

    Homepage: https://www.virtualbox.org
    Download-Size: 17.3 MB
    APT-Manual-Installed: yes
    APT-Sources: http://mirrors.cn99.com/ubuntu bionic-updates/multiverse amd64 Packages
    Description: x86 virtualization solution - base binaries
     VirtualBox is a free x86 virtualization solution allowing a wide range
     of x86 operating systems such as Windows, DOS, BSD or Linux to run on a
     Linux system.
     .
     This package provides the binaries for VirtualBox. Either the virtualbox-dkms
     or the virtualbox-source package is also required in order to compile the
     kernel modules needed for virtualbox. A graphical user interface for
     VirtualBox is provided by the package virtualbox-qt.


### 记要
原先就有一个 XP 虚拟机, 但是:

- 无论 git 哪个版本, 都无法安装
- 又尝试了 cmder 集成终端加强工具, 也无法安装
    + 各种 dll 找不到...
- 想想, 2020年了, 除了 ATM 机, 没个人平时在用 XP 来当桌面环境的了
    + 除了 DOS 仿真游戏, 其它什么游戏也玩不了哪...  


然后, 开始搜索如何能快速构建一个 windows 环境, 到 VirtualBox 中:

- 首先感动俺的就是: [下载 Windows 10 虚拟机 - Windows 应用开发](https://developer.microsoft.com/zh-cn/windows/downloads/virtual-machines)
    + 虽然有 17Gb 大小
    + 但是, 好歹是官方的哪...
    + 然而, 好容易下载下来, 发现 VirtualBox 无法加载 .ova 镜像
    + 想想, 可能是版本问题
    + 强行升级到 virtualbox-6.1
    + 果然可以加载了, 但是, 无法运行, 根本进入不了系统
- 这才发觉, 当初选购 miniPC 时, 为了一些老模块兼容性, 专门选择 32位兼容的
    + 安装的 Ubuntu 也是 32位的
    + 而 M$ 官方提供的没特殊说明, 早已统一是 64 位的了...
- 那么回到老思路, 从各种花园中下载对应精简`优化`过的 ghost 光盘
    + 然后, 在 VirtualBox 中创建虚拟机
    + 加载 .ios 镜像
    + 通过虚拟光盘启动 Windows 2003 PE 工具系统
    + 使用内置 Ghost 工具, 将目标系统恢复到虚拟机硬盘中
- 可惜:
    + win7/8/10 各种优化方案的 ghost 镜像
    + 从 2.7G~4.7G 各种体积的都有
    + 全部一个样:
        * win7 好歹能进入系统,但是, 什么也不动, 就自动兰屏屎机,无法恢复
        * win8/10 启动时就报各种硬件加速不兼容, 强行完成恢复后
            - 都只能停在启动屏幕
            - 屎也无法进入系统
- 好吧...再退一步
    + 老老实实从历史中, 挖出官方 win7 安装光盘
    + 在 VirtualBox 中从头安装
    + 还好, 也就20分钟,毕竟是 SSD 时代了...
    + 安装好, 也顺利进入系统, 然后撞到正版系统激活问题...
    + ...猜, 怎么解决的?

总算用了大半天, 有了一个干净的"正版" win7 32位系统环境, 

>> 但是, 没想到...

32位 win7 旗舰版, 竟然是如此个性的系统:

- 先解决 SSH 的问题:
    + putty 官方下载 32位全功能包
    + macOS 下载, SCP 推到 Ubuntu 宿主机
    + 通过 VirtualBox 和子系统的共享目录
    + 在 win7 中正常安装(提取)
    + 使用 puttygen.exe 生成私匙对
    + 启动 pageant.exe 加载密钥, 发布 SSH 服务
- 再解决编辑器的问题:
    + VSCode 包含所有主要功能,首先尝试:
        * 官方版本可以安装, 但是无法运行
        * 卡屎在启动页面...
    + [Notepad++](https://notepad-plus-plus.org/) 官网下载
        * [zip package](https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.8.3/npp.7.8.3.bin.zip)
        * 可以直接运行, 不用安装
        * 丢个快捷方式到桌面也就完成了部署
- 真正的挑战爆发在 [Git](https://git-scm.com/download/win)
    + 官方无论哪个形式的 32-bit 版本
    + 都无法安装, 或是解开后, 无法运行
- git-bash 屎了...那么其它 windows 环境兼容的呢?
    + [TortoiseGit – Windows Shell Interface to Git](https://tortoisegit.org/download/) 和 windows 资源管理器自然结合的形式是最自然的
        * 可惜安装/运行都正常
        * 却依赖外部 git 指令, 自身没有 git 能力
        * 强行指向几种版本的 git-bash 中的 git 
        * 都无法通过自检
    + [Fork - a fast and friendly git client for Mac and Windows](https://git-fork.com/)
        * 地球最强免费可视化 git 客户端
        * 无法安装, 没有 32-bit 版本
    + 从官方挖其它客户端, 希望有内置 git 的:
        * [SourceTree](https://www.sourcetreeapp.com/)
        * [GitHub Desktop](https://desktop.github.com/)
        * [ungit](https://github.com/FredrikNoren/ungit)
        * [RepoZ](https://github.com/awaescher/RepoZ/)
        * [Cong](http://cong.tools/)
        * ...免费的基本都无法安装, 报各种 .NET 依赖丢失
        * [GitKraken](https://www.gitkraken.com/) 倒是可安装, 可运行
            - 但是,收费
            - 而且本身就是类似 Atom 一样一个内部网站的壳
            - 非常慢不说, 帐号注册, 还依赖 github ....
                + 那俺为了使用 gitlab 还得先专门注册 github  ?

> 怎么办?

- 按照以往的经验, cmder 是最好的选择, [Cygwin](https://www.cygwin.com/) 是最后最完备, 也最没 windows 体验的选择...
- 好在, 从官方下载的 [Cygwin](https://www.cygwin.com/) 安装器根本无法运行
- 那就只能硬怼 [Cmder | Console Emulator](https://cmder.net/) 了
- 从官方仓库 [27 releases](https://github.com/cmderdev/cmder/releases) 中一个个尝试
- 发现 [v1.2.9 - The Anti-PowerShell Pre-Release](https://github.com/cmderdev/cmder/releases/tag/v1.2.9)
- 这个名称好屌...
    + 一试, 果断可用


## 成果

![比对实景](http://ydlj.zoomquiet.top/ipic/2020-01-21-py0.5demo-case.jpg)

- macOS 本地使用:
    + iterm2 作为终端
        * 包含 OpenSSH/git/vim
            - git version 2.14.3 (Apple Git-98)
        * 通过 Homebrew 统一管理
    + Sublime Text3 作为编辑器
        * 正版, 个人终身授权
- 透过 VNC view 访问内网远程 Ubuntu GNOME 桌面
    + 运行 VirtualBox
    + 拉起 win7 桌面
        * Notepad++ 7.8.3 作为编辑器
        * Cmder 1.2.9 作为终端
            - 包含一系列预编译实用工具
            - 从 ls 到 vim...
            - 当然, 也包含 git 
                + git version 2.6.1.windows.1

至此, 基本完成可以客观演示/对比 windows 环境中 
[蟒营™ Python 入门班](https://py.101.camp/)
所需要的各种基本操作实景.

> 是也乎,(￣▽￣)

- 还没开始优化系统呢
- 各种注册表, path 环境加强...
- 回想当年自己为了在 windows 环境中, 有各种 Linux/mac 中的开发体验,
    + 折腾了多少东西哪...


## Changelog

- 200121 1h 成文
- 200120 6.5h 确认最终组合
- 200119 5.5h 试安装各种嗯哼
- 200118 1h 规划
- 191225 .5h 起意