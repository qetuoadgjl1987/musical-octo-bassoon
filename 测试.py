import numpy as np


# 镜场函数（这里以二维的Rastrigin函数为例）
def mirror_field(x, y):
    return 20 + x ** 2 + y ** 2 - 10 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))


# 初始化鲸鱼种群
def initialize_population(num_whales, num_dimensions, boundary):
    whales = []
    for _ in range(num_whales):
        whale = np.random.uniform(boundary[0], boundary[1], num_dimensions)
        whales.append(whale)
    return whales


# 更新鲸鱼位置
def update_position(whale, leader, c, a):
    A = 2 * a * np.random.rand(len(whale)) - a
    C = 2 * np.random.rand(len(whale))
    D = np.abs(C * leader - whale)
    new_position = leader - A * D
    new_position = np.clip(new_position, -c, c)
    return new_position


# 鲸鱼优化算法
def whale_optimization_algorithm(num_iterations, num_dimensions, num_whales, boundary):
    # 初始化鲸鱼种群
    whales = initialize_population(num_whales, num_dimensions, boundary)

    # 迭代优化
    for iteration in range(num_iterations):
        a = 2 - iteration * (2 / num_iterations)  # 动态更新调整参数
        for i in range(num_whales):
            x, y = whales[i]

            # 计算镜场值
            mirror_value = mirror_field(x, y)

            # 寻找最优解（最小值）
            leader_index = np.argmin(mirror_value)
            leader = whales[leader_index]

            # 更新鲸鱼位置
            new_position = update_position(whales[i], leader, boundary[1], a)
            whales[i] = new_position

    return whales


# 使用示例
num_iterations = 100  # 迭代次数
num_dimensions = 2  # 优化问题维度数（这里为二维）
num_whales = 30  # 鲸鱼种群数量
boundary = (-5, 5)  # 搜索空间边界

# 运行鲸鱼优化算法
optimized_whales = whale_optimization_algorithm(num_iterations, num_dimensions, num_whales, boundary)

# 输出最优解（最优位置）
best_whale = min(optimized_whales, key=lambda whale: mirror_field(whale[0], whale[1]))
print("最优解：", best_whale)
print("最优解的镜场值：", mirror_field(best_whale[0], best_whale[1]))