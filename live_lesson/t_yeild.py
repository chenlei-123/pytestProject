# 生成器

def provider():
    # 循环读取数据列表
    for i in range(10):
        print("开始操作")
        yield i  # 让步到next
        print("结束操作")


p = provider()
# print(p)
for i in p:
    print(i)
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
