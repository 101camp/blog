# blog
blogging all kinds of 101.camp

## 综述
> 改进 Mkdocs 工具, 利用 github-pages 完成免费发布

- 蟒营™基于 Python 工具链
    + github 基于 RoR 工具链
    + 所以, github-pages 并不支持 Python 完成的各种 SSG 工具
- 进一步的, 以往各种 Jekyll SSG 引擎, 都依赖在头部有一堆非内容的 meta 信息行
    + 这令撰写的 .md 无法简单的直接复制, 应用到其它场景中, 很烦
- 所以, 基于 MkDocs, 用 invoke 编写对应小工具, 完成自动化:
    + 目录生成
    + 索引注入
    + 编译为 html 网站
    + 自动 push 到 github 发布


## 配置
> 基于 gh-pages 分支

- 主仓库: https://github.com/101camp/blog
- 发布分支: https://github.com/101camp/blog/tree/gh-pages

先在本地合适目录中, 分别 clone 两次:

- blog <- https://github.com/101camp/blog
- blog_ghp <- https://github.com/101camp/blog
    + 然后, 进入切换到 `gh-pages` 分支 

最后, 将两个仓库用目录软链接关联起来:

```
$ cd path/2/blog
$ ln -s ../blog_ghp/ site
$ ls -la
total 32
-rw-r--r--  1 zoomq staff   13  9 10 10:01 CNAME
-rw-r--r--  1 zoomq staff 1318  9 10 10:01 LICENSE
-rw-r--r--  1 zoomq staff 1666 10  9 17:24 README.md
drwxr-xr-x  2 zoomq staff   68  9 15 19:43 _draft
drwxr-xr-x  3 zoomq staff  102  9 22 18:21 _trigger
drwxr-xr-x 10 zoomq staff  340  9 10 10:25 docs
-rw-r--r--  1 zoomq staff  460  9 10 17:29 mkdocs.yml
drwxr-xr-x 12 zoomq staff  408  9 10 10:01 mkdocs_alabaster
lrwxr-xr-x  1 zoomq staff   12  9 10 10:03 site -> ../blog_ghp/
-rw-r--r--  1 zoomq staff 8826  9 16 08:46 tasks.py

```

这样 `tasks.py` 才能自动完成一系列行为.


## 使用
> Python 3, 依赖 invoke


    ༄  inv -l
    Available tasks:

      bu      usgae MkDocs build AIM site
      pub     $ inv pub [101|py] <- auto deploy new site version base multi-repo.
      reidx   re-build _index auto.
      ver     echo crt. verions

一般使用:

- 在 `docs` 对应目录中撰写 .md
- 然后, 回到根目录执行:
    + `$ echo '' > _trigger/deploy.md` 放置部署标记文件
    + `$ inv pub` 自动进行目录生成/编译/发布


## 课程
> 蟒营™组织发布各种线上/下课程以及社区来共同嗯哼

### 101camp3py 进行中

- 190919 截止
- 190922 开课
- 191103 结束

