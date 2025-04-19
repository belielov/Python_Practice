""" format()函数基本用法
基本语法是通过 {} 和 : 来代替以前的 %
1、位置替换print('{0} {1}'.format('字符串1','字符串2'))格式，
      {}调用时，字符串编号顺序从0开始
2、可通过列表索引格式化字符串，{0[1]}中，‘0’ 是必须的
3、可以使用大括号 {} 来转义大括号，{{}}
4、数字和关键字段可以混合使用来传递参数，
5、关键字参数必须位于位置参数之后。
6、省略字段名{}不能和数字形式的字段名同时使用
7、format 函数可以接受不限个参数，位置可以不按顺序。
8、占位符使用大括号 {} 定义。
9、返 回 值，返回一个格式化的字符串
10、# {} 和参数的个数必须匹配，否则会报错。
"""
# ----------- 按照先后顺序位置替换 -----------
#不指定位置，按默认顺序
print('{} {}'.format('Adversity','Awake'))
print('{} {} {} '.format('逆境清醒：','不能如愿而行，', '也须尽力而为。'))
# empty 占位符
text = "我的名字叫{}，我已经{}岁了~".format("逆境清醒",100)
print(text)
#不指定位置，按默认顺序，{{}}仅代表{}，不占用字符串格式化位置顺序
print('{} {{}} {} {{}} {}'.format('逆境清醒：','不能如愿而行，', '也须尽力而为。'))

# ----------- 按照索引进行匹配替换 -----------
# 按索引编号来匹配
text2 = "我的名字是{0}，我已经{1}岁了~".format("TH", 100)
print(text2)
# 设置指定位置
print('{0} {1}'.format('逆境', '清醒'))
print('{1} {0}'.format('逆境', '清醒'))
print('{1} {0} {1}'.format('逆境', '清醒'))
print('{1}{3}:{0},{2}!{3}!'.format('不能如愿而行', '逆境', '也须尽力而为', '清醒'))
print('{0} {2} {1}'.format('菠萝', '雪梨', '苹果'))

# ----------- 按关键字索引进行匹配替换 -----------
print('ID:{id}, Name:{name}'.format(id='No008', name='逆境清醒'))
print('博客名：{name}, 地址：{url}'.format(name='逆境清醒', url='https://www.baidu.com/'))
# 关键字可以随便放置
print('我今年{age}岁，座右铭{motto}'.format(age=100, motto='要有勇气做真实的自己'))
print('我今年{age}岁，座右铭{motto}'.format(motto='要有勇气做真实的自己', age=100))

# ----------- 通过列表索引格式化字符串 -----------
list1 = ['No008', '逆境清醒']
print('ID:{List[0]}, Name:{List[1]}'.format(List=list1))
print('ID:{List[1]}, Name:{List[0]}'.format(List=list1))
print('ID:{0[0]}, Name:{0[1]}'.format(list1))
print('ID:{0[1]}, Name:{0[0]}'.format(list1))

info1 = ("草莓", "红色")
info2 = ("芒果", "黄色")
print('水果名：{0[0]}, 颜色：{0[1]}'.format(info1, info2))
print('水果名：{1[0]}, 颜色：{1[1]}'.format(info1, info2))

# 在format格式化时，可使用 * 或者 ** 对 list 拆分
foods = ['苹果', '雪梨', '草莓', '菠萝', '香蕉']
s = '小白兔喜欢吃 {2} and {0} and {4}'.format(*foods)
print(s)

# ----------- 通过字典设置格式化字符串 -----------
dict1 = {'id':'No008', 'name':'逆境清醒'}
print('ID:{0[id]}, Name:{0[name]}'.format(dict1))
# 在format格式化时，可使用 ** 进行对字典拆分
print('ID:{id}, Name:{name}'.format(**dict1))

info3 = {'名字':'逆境清醒', '性别':'女'}
info4 = {'名字':'蒲公英', '性别':'女'}
print('名字：{0[名字]}，性别：{0[性别]}；名字：{1[名字]}，性别：{1[性别]}'.format(info3, info4))

# 同时使用元组和字典传参
name1 =['紫悦', '魔法与友谊']
name2 ={'Myname':'云宝', 'skill':'飞行'}
print("我是{0}，我的绝招是{1}".format(*name1, **name2))
print("我是{0}，我的绝招是{skill}".format(*name1, **name2))
print("我是{Myname}，我的绝招是{skill}".format(*name1, **name2))
print("我是{Myname}，我的绝招是{1}".format(*name1, **name2))

# ----------- 通过类设置格式化字符串 -----------
class Value1:
    id = 'No008'
    name = '逆境清醒'
print("ID:{Value.id}, Name:{Value.name}".format(Value=Value1))

class TestValue:
    def __init__(self, value):
        self.value = value
ab = TestValue(8)
print("ab = ", ab)
print("TestValue(8)", TestValue(8))
print("ID:{Value}".format(Value=TestValue))
print("ID:{Value.value}".format(Value=ab))

class Names:
    name1 = '陌生但有缘的朋友'
    name2 = '逆境清醒'
print("你好！{names.name1}，我是{names.name2}".format(names=Names))

# ----------- 通过魔法函数、参数设置格式化字符串 -----------
class Magics:
    def __format__(self, format_spec):
        print("这个参数的类型是：", type(format_spec))
        print(f'你使用format()函数，叫醒了我 -> (逆境清醒留言内容：{format_spec})')
        return "@"
magic = Magics()
format(magic, "2025年，但行前路，不负韶华！")

class Date:
    # 私有字典
    __format_dic = {
        "1":"{obj.year}-{obj.month}-{obj.day}",
        "2":"{obj.year}:{obj.month}:{obj.day}",
        "3":"{obj.year}/{obj.month}/{obj.day}",
    }
    # 初始化方法 __init__
    # 接收 year、mon、day 参数，并将它们分别赋值给实例属性 self.year、self.month、self.day。
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    # __format__ 方法
    # 这是 Python 的魔法方法，用于定义对象在 format() 函数中的行为。
    def __format__(self, format_spec):
        if not format_spec or not format_spec in self.__format_dic:
            f = self.__format_dic["1"]
        else:
            f = self.__format_dic[format_spec]
        return f.format(obj=self)

date = Date(2025, 4, 18)
print("日期格式（选项为1）：", format(date, "1"))
print("日期格式（选项为2）：", format(date, "2"))
print("日期格式（选项为3）：", format(date, "3"))
print("日期格式（选项为空，则选择默认）：", format(date))
print("日期格式（选项不存在，则选择默认）：", format(date, "4"))

# 对上面定义的 Date 类进行改进
class Date:
    # 私有字典
    __format_dic = {
        "1":"{year}-{month:02d}-{day:02d}",  # 2025-04-18（默认补零）
        "2":"{year}:{month:02d}:{day:02d}",  # 2025:04:18
        "3":"{year}/{month:02d}/{day:02d}",  # 2025/04/18
        "4":"{day}-{month_abbr}-{year}",     # 18-Apr-2025
        "5":"{month_name} {day}, {year}"     # April 18, 2025
    }

    __month_names = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    __month_full_names = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September","October", "November", "December"
    ]

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self._is_valid_date()

    def _is_valid_date(self):
        """ 验证日期合法性 """
        if not isinstance(self.month, int) or not 1 <= self.month <= 12:
            raise ValueError(f'Invalid month: {self.month}')

        max_day = 31
        if self.month in [4, 6, 9, 11]:
            max_day = 30
        elif self.month == 2:
            # 润年判断
            if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
                max_day = 29
            else:
                max_day = 28

        if not isinstance(self.day, int) or not 1 <= self.day <= max_day:
            raise ValueError(f'Invalid day: {self.day} for {self.year}-{self.month}')

    # __format__ 方法
    # 这是 Python 的魔法方法，用于定义对象在 format() 函数中的行为。
    def __format__(self, format_spec):
        # 获取格式模版
        format_template = self.__format_dic.get(format_spec, self.__format_dic["1"])

        # 添加月份名称参数
        format_params = {
            "year": self.year,
            "month": self.month,
            "day": self.day,
            "month_abbr": self.__month_names[self.month - 1],
            "month_name": self.__month_full_names[self.month - 1]
        }

        return format_template.format(**format_params)

# 测试用例
try:
    date = Date(2025, 4, 18)

    print("默认格式（选项1）：", format(date, "1"))  # 2025-04-18
    print("冒号格式（选项2）：", format(date, "2"))  # 2025:04:18
    print("斜杠格式（选项3）：", format(date, "3"))  # 2025/04/18
    print("缩写格式（选项4）：", format(date, "4"))  # 18-Apr-2025
    print("全名格式（选项5）：", format(date, "5"))  # April 18, 2025
    print("无效格式回退（选项6）：", format(date, "6"))  # 使用默认格式

    # 测试非法日期
    Date(2025, 2, 30)

except ValueError as e:
    print(f'日期错误：{e}')

# ----------- 通过内嵌替换设置格式化字符串 -----------
"""
1. 外层模板 Hello {0:...}
    - {0} 表示第一个参数（索引为0），即 '逆境清醒'。
    - : 后的内容是格式说明符，定义如何格式化该参数。
    
2. 内层格式说明符 {1}>{2}
    - {1}：对应第二个参数（索引为1），即填充字符 '☆'。
    - > 表示右对齐，< 左对齐，^ 居中对齐。
    - 填充字符可以是任意符号（默认是空格）。
    - {2}：对应第三个参数（索引为2），即总宽度 15。
3. 组合后的格式规则
    将 '逆境清醒' 格式化为：右对齐，总宽度 15 字符，不足部分用 ☆ 填充。
"""
print('Hello {0:{1}>{2}}'.format('逆境清醒', '☆', 15))

# ----------- 其他混搭使用 -----------
fh = [' @ ', '。', '!']
key = {'id':'No008', 'name':'逆境清醒'}
print('ID:{id} {}Name:{name}{}{}'.format(*fh, **key))

# 关键字实参必须写在最后，否则会编译报错
s = "{}, {}, 说得对吗：{judge}".format('努力不一定成功', '但放弃一定会失败', judge='Y')
print(s)

# 可以通过索引对参数的部分进行取值
sentence = "这是一个{a}，{a[0]}是颜色".format(a='红苹果')
print(sentence)


"""
用对齐及填充的方式格式化
    :<    左对齐填充
    <是左对齐，后面带宽度，
    : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
    -表示左对齐
    %-30s: 左对齐，占位符30位
"""
# ----------- 左对齐及填充格式化字符串 -----------
# 15表示占15个字符，- 表示左对齐
print('%-15s' % '逆境清醒', end='@')
print()

# < 表示左对齐，☆ 表示用 ☆ 号进行填充，10表示共占10个字符
print('{:☆<10}'.format('逆境清醒'))
print('{:？<10}'.format('逆境清醒'), end='@')
print()

# 左对齐，取30位，以空格补充空位
print("%-30s" % "Adversity Awake", end='@')
print()

# 不设置，默认左对齐
print("{:20s} & {:20s}".format('珍惜每一次相识', '珍惜每一分温暖'))

# <表示左对齐,10表示共占10个字符
products = [["iphone",6888],["MacPro",1480],["coffee",32],["abc",2499],["Book",60],
            ["Nike",699],["MacPro",45600],["coffee",432],["abc",244499],["Book",6230],
            ["Nike",61299],["MacPro",14800],["coffee",32],["abc",2499],["Book",60],
            ["Nike",699]]
print('-' * 10 + ' 商品列表 ' + '-' * 10)
i = 0
for product in products:
    print('{:<6}\t{:<10}\t{:<10}'.format(i, product[0], product[1]))
    i += 1

# ----------- 右对齐及填充格式化字符串 -----------
print('@%15s' % '逆境清醒')
print('@{:>10}'.format('逆境清醒'))
print('@', '{:☆>10}'.format('逆境清醒'))

# 右对齐，取30位，以空格补充空位
print('@''%30s' % 'Adversity Awake')

print('{:<20} & {:>20}'.format('珍惜每一次相识', '珍惜每一分温暖'))
print('{:>20} & {:<20}'.format('珍惜每一次相识', '珍惜每一分温暖'))

print('{} is {:>10.2f}'.format(1.8321, 1.8321))

# ----------- 居中对齐及填充格式化字符串 -----------
print('@{:^10}@'.format('逆境清醒'))
print('@{:☆^10}@'.format('逆境清醒'))
print('{:^20} & {:^20}'.format('珍惜每一次相识', '珍惜每一分温暖'))
print('{:☆^30}'.format('逆境清醒'))

# ----------- 调用函数对齐及填充格式化字符串 -----------
# ljust()函数：左侧对齐
# rjust()函数：右侧对齐
# center()函数：字符串居中对齐
# zfill()函数：右侧对齐，左侧补0
# len(str1)>width时，输出全部字符串
str1 = "逆境清醒"
width = 20
# 字符串左侧对齐， 右侧补❄
print(str1.ljust(width, '※'))
print('{}'.format(str1.ljust(width, '※')))
# 字符串右侧对齐， 左侧补❄
print(str1.rjust(width, '※'))
print('{}'.format(str1.rjust(width, '※')))
# center字符串居中对齐， 两侧侧补❄
print(str1.center(width, '※'))
print('{}'.format(str1.center(width, '※')))
# 字符串右侧对齐， 左侧补0
print(str1.zfill(width))
print('{}'.format(str1.zfill(width)))


""" 
用format函数实现对齐打印
"""
# ----------- 打印左对齐图案 -----------
def show(n):
    num = "🌸"*(2*n-1)
    width = len(num)
    for i in range(1, 2*n, 2):
        print('{:<{}}'.format('🌸'*i, width))

show(8)

# ----------- 打印右对齐图案 -----------
def show(n):
    width = 20
    for i in range(1, 2*n, 2):
        print("{:>{}}".format('0'*i, width))

show(8)

# ----------- 打印居中对齐图案 -----------
def show(n):
    num = "❄"*(2*n-1)
    width = len(num)
    for i in range(1, 2*n, 2):
        print('{:^{}}'.format('❄'*i, width))

show(8)
