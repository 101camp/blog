# TS0: Python 初学者常见 5 种错误
> Tech Soup ~ 技术鳮汤 ;-)

## 不必要的 lambda
> 并不是一定要函式编程才优雅


    def request(self, method, **kwargs):
        # ...
        if method not in ("get", "post"):
            req.get_method = lambda: method.upper()
        # ...


比如上面这个例子中的 lambda: method.upper()

其实, 说人话就好:

    def request(self, method, **kwargs):
        # ...
        if method not in ("get", "post"):
            req.get_method = method.upper
        # ...

## 异常 NotImplemented
> 相近命名引发的误用

    class SitesManager(object):
        def get_image_tracking_code(self):
            raise NotImplemented

而其实应该是:

    class SitesManager(object):
        def get_image_tracking_code(self):
            raise NotImplementedError


- NotImplemented 是一个常量, 一般用以二元计算;
- NotImplementedError 才是一个异常类, 配合 raise 来检验子类中是否完成对应函式的实现.


## 可变默认参数

最常见的:

    def add_item(new_item, items=[]):
        items.append(new_item)

这样将出现不可预知的结果,
推荐声明应该是:

    def add_item(new_item, items=None):
        if items is None:
            items = []
        items.append(new_item)

因为, 执行函式时, 默认参数会尝试运行,
指定的值是类似 [] {} 等可变量,
将可能被意外修改/使用.

## 用 assert 语句作为保护条件

比如:

    assert re.match(VALID_ADDRESS_REGEXP, email) is not None

看起来, assert 是一种检查某些条件和执行失败的简便方法,
但是, 注意:

- 当使用 Python -O 优化形式运行脚本时
- 解释器会从代码树中抛弃断言语句,
- 导致类似代码根本不运行
- 所以, 建议 assert 只用在测试代码中

而, 正常的生产代码应该正常检验:


    if not re.match(VALID_ADDRESS_REGEXP, email):
        raise AssertionError


## 用 isinstance 替代 type

    def which_number_type(num):
        if isinstance(num, int):
            print('Integer')
        else:
            raise TypeError('Not an integer')

    which_number_type(False)  # prints 'Integer', which is incorrect

虽然, isinstance() 和 type() 都有数据类型检验的能力,

但是, 有个重要区别:

- isinstance 在解析对象时,能识别继承关系
    + 而 type 不管这事儿
- 因为 bool 是 int 的子类
    + 所以,上述代码, 将 False 意外识别为 数字




## PS:

事实上类似初学者常见问题列表, 有很多种...
只是并不是真正初学场景中会撞到的,
为什么?

对初学的定义不同;

在蟒营(101.camp) Python 入门班(py.101.camp),
针对的是无基础学习者,
想有效获得靠谱编程体验 -> 即, 能自如探索 Python 生态, 
识别靠谱方案, 并快速自行完成实验, 并入当前问题的解决代码中;


全程高度互动:

- 针对每一位学员, 每一个具体真实行为, 
    + 进行就地嗯哼,
- 力图在每一个感性体验现场, 
    + 注入理性思考过程,
- 从而, 进一步形成习惯,完成编程思维的再激发.


当前 蟒营 Python入门正式班(101camp2py) 第2期 正在报名:

- 截止 190725 0842 (最后不到 4.2小时)
- 课程时间: 190728~190908
- 报名入口: https://py.101.camp


## PPS:
> 当前课程对应公众号 蟒营101camp 暂定专栏有:

- DM 大妈嗯哼 ~ 文本快速呢喃点心境...
- NC 嗯哼蟒营 ~ 图文/图片有关课程信息
- SS 学员故事 ~ 各期课程中发生的真实"血案"
- TS 技术鳮汤 ~ 转载/原创自学技术/心法相关嗯哼

