# 目录
[廖雪峰Python3教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
## 1. 第一篇 Python基础

### 1.1 Python简介

>Life is short, use Python.     
>创始人：Guido van Rossum("龟叔",吉多范罗苏姆)，荷兰人。   
>实例：YouTube，Instagram，豆瓣等。  
>应用：网络应用(网站、后台服务)，日常工具(脚本任务、自动化)，爬虫、大数据(数据挖掘、数据清洗)。    
>优点：1.优雅，明确，简单。尽量写容易看明白的代码，尽量写少的代码；2.完善的基础代码库，大量的第三方库。    
>缺点：1.解释型语言运行速度慢；2.代码不能加密，发布的程序就是发布源代码。

### 1.2 安装Python

Windows平台安装注意勾选添加Python环境变量。

![运行Python](Run_python.png)

#### 1.2.1 Python解释器

1. CPython(广泛使用)
2. IPython
3. PyPy
4. Jython
5. IronPython

### 1.3 第一个Python程序

Python交换式IDE环境:
![Python交换式IDE环境](interactive_python.png)

>在Python交换式命令行下，可以直接输入代码，然后执行，并立刻得到结果。

#### 1.3.1 使用文本编辑器

文本编辑器(把IDE也写进去了)推荐：

1. Sublime Text 2/3 收费
2. Notepad++ 免费
3. Visual Studio Code(VS Cod大法好) 免费
4. PyCharm 收费
5. Atom(Github出品) 免费

[test.py](test.py)

```python
print(100+200)
```

执行python文件test.py，在命令行中，切换到该文件所在目录，然后输入`python test.py`即可执行。

#### 1.3.2 Python代码运行助手

Python代码运行助手可以让你在线输入Python代码，然后通过本机运行的一个Python脚本来执行代码。
这个有点酷炫啊，在本机开了一个http服务。

启动Python运行助手：
![启动Python运行助手](python_run_assistant.png)

运行结果：
![运行](run_python_assistant.png)
![运行](run_result.png)

#### 1.3.3 输入和输出

`print('The quick brown fox','jumps over','the lazy dog')`

The quick brown fox jumps over the lazy dog.
覆盖了英文的2个字母，通常这句话用来测试。中文对应的有永字八法，千字文等。

### 1.4 Python基础

Python使用缩进来组织代码块，遵守约定俗成的习惯，使用4个空格的缩进(Tab)。
在文本编辑器(IDE)中，设置Tab自动转换为4个空格，确保不混用Tab和空格。

以`#`开头的语句是注释，注释是给人看的，可以是任意内容，解释器会忽略掉注释。其他每一行都是一个语句，当语句以冒号`:`结尾时，缩进的语句视为代码块。

Python程序是大小写敏感的，如果写错了大小写，程序会报错。

#### 1.4.1 数据类型和变量

数值类型：整数、浮点数    
字符串类型：`"test"`, `'for'`,`'''多行内容'''`   
布尔类型：`True`, `False`   
布尔运算： `and`, `or`, `not`   
转义字符：`\`   
`r' '`表示不转义     
`=`表示赋值     

动态语言：变量本身类型不固定，比如Python     
`a = 123`   
`a = 'test'`    
静态语言：变量定义时必须指定变量类型，比如Java   
`int a = 123`   
`string a = "test"`


整数的地板除//永远是整数，即使除不尽。要做精确的除法，使用/就可以。

#### 1.4.2 字符串和编码

#### 1.4.3 使用list和tuple

#### 1.4.4 条件判断

#### 1.4.5 循环

#### 1.4.6 使用dict和set

### 1.5 函数

    调用函数
    定义函数
    函数的参数
    递归函数

## 2. 第二篇 Python高级

### 2.1 高级特性

    切片
    迭代
    列表生成式
    生成器
    迭代器

### 2.2 函数式编程

    高阶函数
    map/reduce
    filter
    sorted
    返回函数
    匿名函数
    装饰器
    偏函数

### 2.3 模块

    使用模块
    安装第三方模块

## 3. 第三篇 Python进阶

### 3.1 面向对象编程

    类和实例
    访问限制
    继承和多态
    获取对象信息
    实例属性和类属性

### 3.2 面向对象高级编程

    使用__slots__
    使用@property
    多重继承
    定制类
    使用枚举类
    使用元类

### 3.3 错误、调试和测试

    错误处理
    调试
    单元测试
    文档测试

### 3.4 IO编程

    文件读写
    StringIO和BytesIO
    操作文件和目录
    序列化

### 3.5 进程和线程

    多进程
    多线程
    ThreadLocal
    进程 vs. 线程
    分布式进程

### 3.6 正则表达式

### 3.7 常用内建模块

    datetime
    collections
    base64
    struct
    hashlib
    itertools
    contextlib
    XML
    HTMLParser
    urllib

### 3.8 常用第三方模块

    PIL

### 3.9 virtualenv

### 3.10 图形界面

## 4. 第四篇 Python网络编程

### 4.1 网络编程

    TCP/IP简介
    TCP编程
    UDP编程

### 4.2 电子邮件

    SMTP发送邮件
    POP3收取邮件

### 4.3 访问数据库

    使用SQLite
    使用MySQL
    使用SQLAlchemy

### 4.4 Web开发

    HTTP协议简介
    HTML简介
    WSGI接口
    使用Web框架
    使用模板

### 4.5 异步IO

    协程
    asyncio
    async/await
    aiohttp

## 5. 第五篇 Python实战

    Day 1 - 搭建开发环境
    Day 2 - 编写Web App骨架
    Day 3 - 编写ORM
    Day 4 - 编写Model
    Day 5 - 编写Web框架
    Day 6 - 编写配置文件
    Day 7 - 编写MVC
    Day 8 - 构建前端
    Day 9 - 编写API
    Day 10 - 用户注册和登录
    Day 11 - 编写日志创建页
    Day 12 - 编写日志列表页
    Day 13 - 提升开发效率
    Day 14 - 完成Web App
    Day 15 - 部署Web App
    Day 16 - 编写移动App

## 6. FAQ

    期末总结
