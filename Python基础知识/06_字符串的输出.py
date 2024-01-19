name = "小华"

# 逗号隔开法
print("名字是",name) #貌似中间会自动添加个空格

# format函数格式化法
print("名字是{}".format(name))
print("名字是{0},{1}".format(name,"您好！")) # format函数格式化，并且指定参数位置
print("名字是{1},{0}".format(name,"您好！")) # 位置可以调换
print("名字是{n}".format(n = name)) # 位置可以是变量（但觉得没什么意义？）
print(f"名字是{name}") # f就是format（格式化）了，这个方式最常用

# 占位符法
print("名字是%s"%(name)) # 和C语言最相似的占位符方式

#print里的运算符
print(name+"很厉害") # 粘合两个字符串，中间无空格
print("="*10) # 连续输出字符串