info = "人生苦短我学Python"

# 单个参数：一个字符
print(info[4])   # 取一个字符
print(info[-1])  # 负索引取导数第一个字符

"""
两个参数
开始下标:结束下标
注意不包括结束下标的数据
"""
print(info[0:4])
print(info[:4])  # 省略开头，默认从头
print(info[4:])  # 省略结尾，默认到尾
print(info[-8:]) # 可以与负索引结合使用

"""
三个参数
开始下标:结束下表:步长
注意结合使用
"""
print(info[::-1]) # 倒序输出
print(info[::2])  # 跳着输出