info = "hello world and python and me"

# 查找

# find
print("="*10,"find","="*10)
print(info.find('and')) # 返回第一个的首下标
print(info.find('and',15,30)) # 给定查找范围
print(info.find('apple')) # 未找到返回-1

# index 与find类似，未找到会报错
print("="*10,"index","="*10)
print(info.index('and')) # 返回第一个的首下标
print(info.index('and',15,30)) # 给定查找范围
#print(info.index('apple')) # 未找到则报错

# count 返回找到的元素的个数
print("="*10,"count","="*10)
print(info.count('and')) # 两个and
print(info.count('and',15,30)) # 区间内一个and
print(info.count('apple')) # 没有apple

# 修改

# 大小写转换方法
print("="*10,"大小写转换","="*10)
print(info.upper()) # 全部大写
print(info.lower()) # 全部小写
print(info.title()) # 每个单词首字母大写
print(info.capitalize()) # 句子首字母大写

# replace 字符串修改与替换方法
print("="*10,"replace","="*10)
print(info.replace("and","or")) # 将and全部替换为or
print(info.replace("and","or",1)) # 将一个and替换为or

# split 字符串分割方法
print("="*10,"split","="*10)
print(info.split())      # 默认使用空格分割
print(info.split("and")) # 使用and分割

# join 字符串拼接方法
print("="*10,"join","="*10)
temp = info.split()   # 按照空格分隔
print("".join(temp))  # 默认直接拼接不留空格
print(",".join(temp)) #选择使用","拼接

# strip 去除左右无关信息方法'
print("="*10,"strip","="*10)
info2 = "    哈哈我就打空格    "
print(info2.strip())
print(info2.lstrip()) # 删除左边（left）的空格
print(info2.rstrip()) # 删除右边（right）的空格

# 判断

# startswith endswith 判断是否以指定字符串开头（结尾）
print("="*10,"startswith endswith","="*10)
print(info.startswith("hello"))
print(info.startswith("python"))

# is... 和C语言相似的字符判断方法
# startswith endswith 判断是否以指定字符串开头（结尾）
print("="*10,"is...","="*10)
info3 ='123'
info4 ='abc'
info5 ='abc123'
print(info3.isdigit()) # 数字
print(info4.isalpha()) # 字母
print(info5.isalnum()) # 数字和字母（is a number）