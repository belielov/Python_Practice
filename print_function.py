""" print()打印输出文本
打印文本时需要使用引号将文本内容引起来，
引号可以是单引号('  ')，双引号(" ")，三引号("""  """)
"""
# Single quotes
print('有生命便有希望')
print('"有生命便有希望"')

# Double quotes
print("永不气馁！")
print("'永不气馁！'")

# Triple quotes
Multilinetext = """
They who cannot do as they would,
must do as they can.
不能如愿而行，
也须尽力而为。
"""
print(Multilinetext)


""" 
print()中空格的使用方法
"""
# 直接在引号中打空格，空格数不限
print("谋事在人  成事在天  有生命便有希望")

# 相邻的两项用逗号间隔
print("谋事在人","成事在天","有生命便有希望")

# 相邻的两项打印时没有用逗号间隔
print("谋事在人""成事在天")

# 字符串间不要空格
print ("谋事在人" + "成事在天")


""" print()换行 
print()函数的“end”参数指定了print()函数在打印完内容之后，用什么符号来表示结尾，
默认值是“\n”，表示换行，即print()函数在打印完指定内容之后，就会自动换行。
我们可以通过“end”参数的定义，用其他符号来表示print()输出打印完成。
例如：print()函数的“end”参数指定为“|”，即print()函数每次输出完成之后，都输出“|”。
"""
# 强制换行
print("有生命\n便有希望")

# 打印后不换行，用end参数来设置你想要的结束符号
print("谋事在人", end=" ")
print("成事在天", end=" ")
print("有生命便有希望")

print("谋事在人", end="|")
print("成事在天", end="|")
print("有生命便有希望", end="|\n")

for i in range(5):
    print(i, end=" ")
for i in range(5):
    print(i, end=",")
print()

for i in range(1, 6):
    print(i, end=" ")
print()
for i in range(1, 6):
    print(i, end=",")
print()


""" 区隔符sep
用sep参数来约束print括号里多项内容之间的区隔符
"""
print("谋事在人","成事在天","有生命便有希望", sep="&")
print("www","csdn","net", sep=".")
print()


""" 制表符\t
制表符\t控制水平间隔，作用如tab键，在打印输出时控制间隔距离
\t表示空8个字符，
如果元素占位小于8，各列能实现完美对齐，皆大欢喜；
如果字符元素占位大于或等于8个字符，对齐会出现偏差，可以再在其中插入N个\t拼起来，这样就能使元素对齐
"""
print("不能如愿而行\t也须尽力而为")
print()

for i in range(1, 11):
    print(i, '\t\t', i*2, '\t\t', i*3, '\t\t', i*4)
print()

name = 'Adversity awake'
saying = "Man proposes, god disposes 谋事在人,成事在天"
print(name.title() + " once said" + ": " + '\n\t"' + saying + '"')  # title()会强制每个单词的首字母大写
print()

# 错误print()效果距离：对齐出现偏差
print("学生号\t姓名\t科目\t分数")
print("100000101\t阿凡达\t语文\t80")
print("100000102\t卡梅隆卡梅隆\t语文\t85")
print("100000103\t莫妮卡·贝鲁卡梅隆\t语文\t85")
print()

# 用多个制表符，对齐完好
print("学生号\t\t姓名\t\t\t\t\t科目\t\t分数")
print("100000101\t阿凡达\t\t\t\t语文\t\t80")
print("100000102\t卡梅隆卡梅隆\t\t\t语文\t\t85")
print("100000103\t莫妮卡·贝鲁卡梅隆\t\t语文\t\t85")
print()

print("%-10s %-17s %-6s %-10s" % ("学生号", "姓名", "科目", "分数"))
print("%-10s\t %-16s %-3s\t %-12s" % ("100000101", "阿凡达", "语文", "80"))
print("%-10s\t %-14s %-3s\t %-12s" % ("100000102", "卡梅隆卡梅隆", "语文", "82"))
print("%-10s\t %-13s %-3s\t %-12s" % ("100000103", "莫妮卡·贝鲁卡梅隆", "语文", "85"))
print()

# 对齐输出，还可以使用format()来实现
products = [["iphone", 6888], ["MacPro", 14800], ["coffee", 32], ["abc", 2499], ["Book", 60], ["Nike", 699],
            ["MacPro", 45600], ["coffee", 432], ["abc", 244499], ["Book", 6230], ["Nike", 61299], ["MacPro", 14800],
            ["coffee", 32], ["abc", 2499], ["Book", 60], ["Nike", 699]]
print("-" * 10 + " 商品列表 " + "-" * 10)
i = 0
for product in products:
    print('{:<6}\t{:<10}\t{:<10}'.format(i, product[0], product[1]))  # {:<6} 表示左对齐，占 6 个字符宽度。
    i += 1
print()


""" 输出数学表达式
print后的括号中如果是数学表达式，则打印结果为表达式最终运算的结果
"""
print(1+2+3+4+5)
print(8/1)
print(2*4)
print()


""" 打印输出反斜杠 \
\\ 第一个 \ 为转义符
"""
print("不能如愿而行\\也须尽力而为")
print()


""" print()变量的输出
无论什么类型的数据，包括但不局限于：数值型，布尔型，列表变量，字典变量……都可以通过print()直接输出。
"""
# 输出数值型变量
num = 91682
print(num)
print()

# 输出字符串变量
name = '逆境清醒'
print(name)
print()

# 输出列表变量
List = [1,2,3,4,5,'a','b','c']
print(List)
print()

# 输出元组变量
Tuple = (1,2,3,4,5,'a','b','c')
print(Tuple)
print()

# 输出字典变量
Dict ={'a':1, 'b':2,'c':3}
print(Dict)
print()


""" 
print()数据的格式化输出
"""
# ------------ 在字符串中插入 ------------
# 字符串变量
name = "逆境清醒"
print("我的名字是%s " % name)
print("my name is", name)
print()

# 整数变量
age = 100
print("我的年龄是%d" % age + "岁了")
print()

# 小数变量
i = 2670.5
print("数字是 %.2f" % i)
print()

# %号点(.)前跟字段宽度；
# %号点(.)后跟精度值；字段宽度中，小数点也占一位
i = 2.67145573
print("8位保留字段宽度%8f" % i)
print("保留两位小数输出的是%.2f" % i)
print("a"+'%10.3f' % i)
print("a"+'%f' % i)
print()

# '%' 字符，用于标记转换符的起始, 后面可以跟各种格式符
print('%s有 %d 个中文字。' % ('逆境清醒', 4))  # 元组
print('%(名字)s有 %(个数)03d 个中文字。' %
      {'名字': "逆境清醒", "个数": 4})  # 字典
print()

s='逆境清醒'
x=len(s)
print('%s名字的长度是 %d' %(s,x))
print()

# ------------ 格式输出 ------------
# %s：输出一个字符串，字符串采用str()的显示
i= 2.6714563467
print('%s' %i)
print()

# %r：字符串(repr())的显示
print('%r' % repr({1, 1, 2, 3}))
print()

# %c：输出一个单一的字符
print('%c' %90)
print()

# %e, %E：指数（基底写e）
k = 2671.4563467284
print('%e' %k)
print('%E' %k)
print()

# %b：二进制整数
print(bin(50))  # 0b 是二进制字符串的前缀，表示后续数字是二进制格式
print(bin(50)[2:])  # 如果不需要 0b 前缀，可以用切片操作
print()

# %hd、%d、%ld：以十进制、有符号的形式输出 short、int、long 类型的整数
print('%d' %50)
print()

# %hu、%u、%lu：以十进制、无符号的形式输出 short、int、long 类型的整数
print('%u'%50)
print()

# %ho、%o、%lo：以八进制、不带前缀、无符号的形式输出 short、int、long 类型的整数
print('%o' %50)
print()

# %#ho、%#o、%#lo：以八进制、带前缀、无符号的形式输出 short、int、long 类型的整数
print('%#o' %50)
print()

# %hx、%x、%lx、%hX、%X、%lX：以十六进制、不带前缀、无符号的形式输出 short、int、long 类型的整数。
# 如果 x 小写，那么输出的十六进制数字也小写；如果 X 大写，那么输出的十六进制数字也大写。
print('%x' %50)
print()

# %#hx、%#x、%#lx、%#hX、%#X、%#lX：以十六进制、带前缀、无符号的形式输出 short、int、long 类型的整数。
# 如果 x 小写，那么输出的十六进制数字和前缀都小写；如果 X 大写，那么输出的十六进制数字和前缀都大写。
print('%#x' %50)
print('%#X' %50)
print()

# %f、%lf 、%F：以十进制的形式输出 float、double 类型的浮点数
i = 2.6714563467
print('%f' %i)
print()

# 说明：%(n)f，是小数点后面只保留6位，小数点代表一位，小数点前面的位数全保留
i = 12345.123456789123456789
print("%8f结果是:", "%8f" %i)
print("%9f结果是:", "%9f" %i)
print("%10f结果是:", "%10f" %i)
print("%.8f结果是:", "%.8f" %i)
print("%.10f结果是:", "%.10f" %i)
print()

# %g、%lg、%G、%lG：以十进制和指数中较短的形式输出 float、double 类型的小数，并且小数部分的最后不会添加多余的 0。
# 如果 g 小写，那么当以指数形式输出时 e 也小写；如果 G 大写，那么当以指数形式输出时 E 也大写。
i = 3.2141234567890000e03
print('%G' %i)
print()

# ------------ 其他一些格式输出方法 ------------
k= 2671.4563467284
print('二进制形式{1:b}'.format(int(k), 100))  # 表示引用 format() 方法中的第2个参数
print('十进制形式{:d}'.format(int(k)))
print('八进制形式{:o}'.format(int(k)))
print('十六进制形式{:x}'.format(int(k)))
print('数字形式{:n}'.format(k))
print('百分数形式{:%}'.format(k))
print('幂指数形式{:e}'.format(k))
print('十进制较短的形式输出{:g}'.format(k))
print('十进制浮点数{:f}'.format(k))
print()

print(bin(int(k)))  # 输出二进制数
print(oct(int(k)))  # 输出八进制数
print(hex(int(k)))  # 输出十六进制数
print()


"""
英文大小写转换（title()首字母大写，upper()全大写，lower()全小写）
"""
name = 'Adversity awake'
print(name.title())
print(name.upper())
print(name.lower())
print()


"""
print()小例子
"""
# ------------ 打印字符 ------------
for u in range(1, 100):
    print('{:c}'.format(u), end='|')
print()

# ------------ 九九乘法表 ------------
print()
for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={}".format(j, i, i*j), end='|')
    print()

# ------------ 打印实心菱形 ------------
print()
n = 5
for i in range(1, n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(1,n):
    print(" "*i+"*"*(2*(n-i)-1))

# ------------ 打印空心菱形 ------------
print()
n = 5
print(" " * (n - 1) + "*")
for i in range(1, n):
    print(" " * (n - 1 - i) + "*" + " " * (2 * i - 1) + "*")
for i in range(1, n - 1):
    print(" " * i + "*" + " " * ((n - 1 - i) * 2 - 1) + "*")
print(" " * (n - 1) + "*")

# ------------ 打印空心三角形 ------------
print()
n = 5
print(" " * (n - 1) + "*")
for i in range(2, n):
    print(" " * (n - i) + "*" + " " * (2 * (i - 1) - 1) + "*")
print("* " * n)

# ------------ 打印实心三角形 ------------
print()
n = 5  # 控制层数
m = 4  # 控制位置
for i in range(0, n):
    for j in range(0, m):
        print(end=" ")
    m -= 1
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

# ------------ 打印侧三角形 ------------
# 方式1
print()
i = 5
while 0 < i <= 5:
    j = 1
    while j <= i:
        print("* ", end = '')
        j += 1
    print(" ")
    i -= 1

# 方式2
for i in range(0,5):
    tx="◆"
    print()
    for k in range(0,5):
        if i>k:
            continue
        print(tx,end=" ")
print()

# 方式3
print()
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("* ", end = '')
        j += 1
    print(" ")
    i += 1

# 方式4
print()
n = 5
# join()函数：将可迭代对象（如列表、生成器）中的多个字符串元素，按指定的分隔符拼接成一个新字符串
print('\n'.join('◆ ' * i for i in range(1, n + 1)))

# 方式5
print()
for i in range(0,5):
    tx='◆'
    tx1=''
    print()
    for j in range(0,5):
        print(tx if i<=j else tx1,end=" ")
print()

# 方式6
print()
l=5
for i in range(l):
    for j in range(i):
        print(end='　')
    for k in range(2*(l-i)-1):
        print(end='◆ ')
    print()

# 方式7
print()
i = 1
while i <= 9:
    if i <= 5:
        print('◆ '*i)
    else:
        print('◆ '*(10 - i))
    i += 1

# ------------ 打印平行四边形 ------------
print()
l = 5
for i in range(l):
    for j in range(l-i):
        print(end=' ')
    for k in range(l):
        print(end='◆')
    print()

# ------------ 用字母单词 love 打印心形 ------------
# 核心逻辑是通过双循环遍历坐标点，判断每个点是否在心形曲线范围内
# (x*0.05)**2 + (y*0.13)**2 -1 是心形曲线的简化公式，通过调整 0.05 和 0.13 控制图形横向和纵向的缩放比例。
print()
print('\n'.join([''.join([('Love'[(x - y) % len('Love')] if ((x * 0.05) ** 2 + (y * 0.13) ** 2 - 1) ** 3 - (
            x * 0.05) ** 2 * (y * 0.13) ** 3 <= 0 else ' ') for x in range(-25, 25)]) for y in range(25, -25, -1)]))


# ------------ 用字符输出 I ❤ U ------------
# 方式1
# 主心形公式：(x² + y² - 1)³ ≤ 3.6x²y³，这是笛卡尔心形方程的变形，用于生成心形轮廓
# 标准心形方程为 (x² + y² - 1)³ - x²y³ ≤ 0，代码中通过调整系数（3.6）优化显示比例
import time
y = 2.5
while y >= -1.6:
    x = -3.0
    while x <= 4.0:
        if (x * x + y * y - 1) ** 3 <= 3.6 * x * x * y * y * y or (-2.4 < x < -2.1 and 1.5 > y > -1) or (
                ((2.5 > x > 2.2) or (3.4 < x < 3.7)) and -1 < y < 1.5) or (
                -1 < y < -0.6 and 3.7 > x > 2.2):
            print(' ', end="")
        else:
            print('*', end="")
        x += 0.1
    print()
    time.sleep(0.15)  # 每行打印间隔 0.25 秒
    y -= 0.2

# 方式2
import time
y = 2.5
while y >= -1.6:
    x = -3.0
    while x <= 4.0:
        if (x * x + y * y - 1) ** 3 <= 5 * x * x * y * y * y or (-2.4 < x < -2.1 and 1.5 > y > -1) or (
                ((2.5 > x > 2.2) or (3.4 < x < 3.7)) and -1 < y < 1.5) or (
                -1 < y < -0.6 and 3.7 > x > 2.2):
            print('*', end="")
        else:
            print(' ', end="")
        x += 0.1
    print()
    time.sleep(0.15)
    y -= 0.2

# ------------ 由Dear,I love you forever! 五个单词输出五个爱心 ------------
import time  # # 导入时间模块，用于控制动画间隔
sentence = "Dear, I love you forever!"  # # 要显示的句子，按空格分隔为多个单词
# 外层循环：逐个处理句子中的每个单词
for char in sentence.split():
    allChar = []  # 存储当前单词生成的所有行图形
    # 纵向循环：y从12到-12，步长-1（控制心形高度，共24行）
    for y in range(12, -12, -1):
        lst = []  # 存储单行字符的列表
        lst_con = ''  # 单行字符串
        # 横向循环：x从-30到29（控制心形宽度，共60列）
        for x in range(-30, 30):
            # 心形数学公式：判断当前坐标是否在心形区域内
            formula = ((x * 0.05) ** 2 + (y * 0.13) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.13) ** 3
            if formula <= 0:
                # 若在区域内，取当前单词的字符循环填充（如 "love" 循环取 l, o, v, e）
                lst_con += char[x % len(char)]  # x取模单词长度实现循环
            else:
                lst_con += ' '  # 区域外填充空格
        lst.append(lst_con)  # 将单行字符串加入列表
        allChar += lst  # 将单行加入总图形列表
    print('\n'.join(allChar))  # 打印当前单词的心形图案：将所有行用换行符连接后输出
    time.sleep(1)  # 暂停1秒，实现逐词显示的动画效果


"""
print()写入文件
"""
# 写入文件1
with open('file.txt', 'w') as f:
    print("Hello, World!", file=f)

# 写入文件2
header = "原始值\t2倍\t\t3倍\t\t4倍"
with open(file='file1.txt', mode='a', encoding='utf-8') as f:  # mode='a'：以追加模式打开文件，保留原有内容
    print(header, file=f)
    for i in range(1, 11):
        print(f"{i}\t\t{i*2}\t\t{i*3}\t\t{i*4}", file=f)


"""
print()在终端输出彩色字体
    语法：\033[显示方式;前景色;背景色m彩色字体显示内容\033[0m
    
    开头部分的三个参数：显示方式，前景色，背景色。
    这三个参数是可选参数，可以只写其中的某一个，
    另外由于表示三个参数不同含义的数值都是唯一的没有重复的，
    所以三个单数的书写顺序没有固定的要求，但建议按照默认的格式规范书写。
"""
print('\033[0;30m逆境清醒虽然已经很笨，但仍希望坚持保持善良\033[0m')
print('\033[1;31m逆境清醒虽然已经很笨，但仍希望坚持保持善良\033[0m')
print('\033[4;32m逆境清醒虽然已经很笨，但仍希望坚持保持善良\033[0m')
print('\033[5;33m逆境清醒虽然已经很笨，但仍希望坚持保持善良\033[0m')
print('\033[7;34m逆境清醒虽然已经很笨，但仍希望坚持保持善良\033[0m')
print('\033[8;35m逆境清醒虽然已经很笨，但仍希望坚持保持善良\033[0m')
print('\033[1;36m逆境清醒虽然已经很笨，但仍希望坚持保持善良\033[0m')
print('\033[1;37m逆境清醒虽然已经很笨，但仍希望坚持保持善良\033[0m')
print()

print('\033[0m显示方式0\033[0m')
print('\033[1m显示方式1\033[0m')
print('\033[4m显示方式4\033[0m')
print('\033[5m显示方式5\033[0m')
print('\033[7m显示方式7\033[0m')
print('\033[8m显示方式8\033[0m')
print('\033[30m前景色0\033[0m')
print('\033[31m前景色1\033[0m')
print('\033[32m前景色2\033[0m')
print('\033[33m前景色3\033[0m')
print('\033[34m前景色4\033[0m')
print('\033[35m前景色5\033[0m')
print('\033[36m前景色6\033[0m')
print('\033[37m前景色7\033[0m')
print('\033[40m背景色0\033[0m')
print('\033[41m背景色1\033[0m')
print('\033[42m背景色2\033[0m')
print('\033[43m背景色3\033[0m')
print('\033[44m背景色4\033[0m')
print('\033[45m背景色5\033[0m')
print('\033[46m背景色6\033[0m')
print('\033[47m背景色7\033[0m')
print()

print('\033[0;36m Adversity awake \033[0m')

# 若打印的不是字符串，而是变量值，则需要将变量值转为字符类型
# Python中加号+是字符串连接符，但要求操作数必须是字符串类型：
# 第一个加号连接\033[0;36m abc=与转换后的字符串str(a)
# 第二个加号将前两者的拼接结果与终端颜色重置符\033[0m连接
a = 7472
print('\033[0;36m abc = ' + str(a) + '\033[0m')
# -------------- 替代实现方案 --------------
# 方案1：f-string格式化（Python 3.6+）
print(f'\033[0;36m abc = {a}\033[0m')
# 方案2：format函数
print('\033[0;36m abc = {}\033[0m'.format(a))
# 方案3：多参数打印（自动加空格分隔）
print('\033[0;36m abc = ', a, '\033[0m', sep='')
print()

# 多行输出彩色字
# 对于结尾部分，其实也可以省略，只用开头部分+输入文字
# 执行效果（没有结束符号，整行都会有背景色）
# 建议语句最后还是加上\033[0m为恢复默认，否则下面的其他输出字体都会被影响
print('\033[7;34m ')
print('工作认真对待，')
print('困难勇敢面对，')
print('生活细细品味，')
print('真情慢慢体会，')
print('珍惜人生中每一次相识，')
print('珍惜天地间每一分温暖，')
print('珍惜每一个无声的默契，')
print('不枉此生。')
print(' \033[0m')
print()
