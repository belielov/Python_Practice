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


""" 输出数学表达式
print后的括号中如果是数学表达式，则打印结果为表达式最终运算的结果
"""
