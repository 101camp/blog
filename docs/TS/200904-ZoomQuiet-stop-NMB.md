# 呢喃/ NMB无法终止
> 记一次失败的系统配置

这是大妈在 **ZoomQuiet** 的第**061**篇原创


-------------
## 背景
大妈虽然学的是计算系,
但是, 当年电脑非常贵,
大学期间到大三, 才和同舍合资买了电脑,
因为出次最少, 平时上机还是排队去机房为多.

真正有私人电脑是毕业3年后了.

所以, 对于自用电脑的系统是有洁癖的;

当年 Windows 系统, 无论 98/XP/NT/... 那都是一言不合立即重装的,
毕竟, 必要软件和数据, 早已习惯分布在其它专用分区中,
系统所在 C 盘, 每42天 重装就感觉已经在变慢.

进而后来使用 Ubuntu/macOS 也都有定期检查系统健康情况的习惯.

-------------
## 现象

11年开始, 终于日常环境切换到 macOS 了,
也将原先 Ubuntu 环境中积累的各种习惯配置迁移过来,
特别是 输入法/浏览器/定制 bash  三大日常操作, 都兼容了老习惯.

只是毕竟 macOS 是魔改 freeBSD, 
和 windows 类似, 还是有很多暗角, 在不知不觉中占用多余空间.

又不信任那些自动优化空间的收费软件,
所以, 一般是用 `OmniDiskSweeper` 免费空间统计工具:

![OmniDiskSweeper](http://ydlj.zoomquiet.top/ipic/2020-09-04-ScreenShot%202020-09-04%2011.22.12.jpg)

可以说就是一个 GUI 化的自动多层排序 **du - estimate file space usage** 工具.

结果发现:

    /opt/local/var/log.nmbd

竟然有8G 之巨.


-------------
## 问题

追查内容发现:

    ...
    [2020/09/04 11:06:04,  0] nmbd/nmbd.c:main(849)
      nmbd version 3.2.15 started.
      Copyright Andrew Tridgell and the Samba Team 1992-2009
    [2020/09/04 11:06:04,  0] nmbd/nmbd.c:main(879)
      standard input is not a socket, assuming -D option
    [2020/09/04 11:06:04,  0] lib/util_sock.c:open_socket_in(1336)
      bind failed on port 137 socket_addr = 0.0.0.0.
      Error = Address already in use
    [2020/09/04 11:06:14,  0] nmbd/nmbd.c:main(849)
      nmbd version 3.2.15 started.
    ...

都是相同的服务失效报告;

将日志文件删除, 不一会儿, 又自动生成, 稳定增长.



-------------
## 尝试

看意思只是 Smaba 启动时, 依赖的 nmbd 无法启动, 因为对应端口已经被占用了.

可是, 根据自己平时使用情况, 根本用不上 Smaba 这种东西,
有太多更加方便和安装的协议可以同 Windows 系统交换文件了.

那么, 解决这种无限增长的服务日志, 嘦停止不必要的服务就好.

参考了:

[macos - How to start SAMBA on MAC OS X from Terminal? - Super User](https://superuser.com/questions/349717/how-to-start-samba-on-mac-os-x-from-terminal ) 
 


[Restart Mac OS X smb service from terminal/cli](https://gist.github.com/TomCan/7182edff81937687432f )
 
[How do I restart samba on OSX 10.6.7? - Apple Community](https://discussions.apple.com/thread/3050861)

[Mac OS X and SMB HOWTO](http://mirror.informatimago.com/next/developer.apple.com/documentation/Darwin/Conceptual/howto/osx_smb/osx_smb.html) 


...

也通过相关指令, 明确的确是 Smanba 相关服务在运行:

```
༄  netstat -l -n | grep 137
udp4       0      0  *.137                  *.*

༄  sudo lsof -i:137
COMMAND    PID     USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
launchd      1     root   17u  IPv4 0x4f6330094fadbb51      0t0  UDP *:netbios-ns
netbiosd 75859 _netbios    3u  IPv4 0x4f6330094fadbb51      0t0  UDP *:netbios-ns
```


但是, 神奇的是:

无论俺如何在配置界面中关闭所有文件共享,
还是用指令关闭所有相关服务;

每隔10秒, 这个日志又开始增长了,而且报错信息不变...


-------------
## 结果
折腾了几个星期, 找到所有相关指令, 能作到用 sudo 身份关闭服务后,
日志的确不再增长.

可是休眠/重启/..等等系统相关操作后,
不知道为什么日志又开始增长.

也就是说, Samba 不知道被哪个软件又给启动了.

因为硬件关系, 又不想升级 macOS 到最新版本, 坚守在最兼容当前硬件的 **10.12.6 (16G2136)**;

平时, 也真的没有任何 Smaba 使用场景, 
这事儿如何解决呢?

突然想到, 既然 Samba 不必要, 但是, 又无法真正删除/停止;

那么对于俺的影响, 无非是额外硬盘空间被占用.

那么, 定期自动化清空无法阻止的日志文件不就好了?


```
42 * * * * echo '' > /opt/local/var/log.nmbd
```

追加一个定期任务到 `crontab` 中,
哗...世界清静了.



PS:

所以, 太多时候,
我们尝试解决的问题, 
其实只是真实问题的一个直觉方案,
而不是问题本身;

这在软件行业中叫 `X-Y 问题`;

如何从这种惯性思维中挣脱出来?

说不得, 当然: **蟒营®编程思维提高班 Python版/** 就是一个很好的训练和呢喃背景.





-------------
> 本人公号所刊载原创内容之知识产权为本人所有,
> 未经许可, 禁止进行转载/摘编/复制及建立镜像等任何使用.
> 欢迎读者沟通交流, 请留言, 或通过邮件交流->

投稿/反馈邮箱:

    askdama@googlegroups.com


(邮件列表地址, 
当成正常邮件发送邮件就好, 不用订阅, 不用翻越...)

-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):


```python

私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
原创课程: 蟒营 (订阅号: Mainium)
过往吐糟: Chaos42 (订阅号 PythoniCamp)

as 核心组织者:
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        TFUG珠海 (订阅号: ZH_TFUG)
```

-------------
好文笔,感叹号年度配额: **1/3**

> NN 4126



