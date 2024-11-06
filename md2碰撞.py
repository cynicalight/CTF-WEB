import hashlib
from Crypto.Hash import MD2


def find_md2_collision():
    # 尝试不同的输入字符串，直到找到符合要求的哈希值
    i = 0
    while True:
        # 将整数 i 转换为字符串作为输入
        input_str = str(i)

        # 使用 MD2 进行哈希计算
        md2_hash = MD2.new(input_str.encode()).hexdigest()

        # 检查哈希值是否以 '332' 开头
        if md2_hash.startswith('332a'):
            print(f"找到碰撞！输入字符串: {input_str}, MD2 哈希值: {md2_hash}")
            break

        # 打印进度以避免长时间无反馈
        if i % 100000 == 0:
            print(f"尝试次数: {i}, 当前哈希值: {md2_hash}")

        i += 1


# 调用函数
find_md2_collision()
