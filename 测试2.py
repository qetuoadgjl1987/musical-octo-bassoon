import numpy as np
# 目标函数：计算镜面位置的适应度
def fitness_function(position):
    # 这里使用一个简单的示例函数作为目标函数，根据实际情况进行修改
    x = position[0]
    y = position[1]
    fitness = x ** 2 + y ** 2
    return fitness

# 初始化鲸群
def initialize_population(population_size, num_dimensions, search_range):
    population = []
    for _ in range(population_size):
        individual = search_range[0] + np.random.rand(num_dimensions) * (search_range[1] - search_range[0])
        population.append(individual)
    return population

# 镜场优化算法
def mirror_placement_optimization(num_iterations, population_size, num_dimensions, search_range):
    population = initialize_population(population_size, num_dimensions, search_range)
    best_fitness = float('inf')
    best_solution = None

    for iteration in range(num_iterations):
        a = 2 - iteration * ((2) / num_iterations) # 参数a控制步长
        for i, position in enumerate(population):
            rand_leader_index = np.random.randint(0, population_size)
            rand_leader = population[rand_leader_index]

            r1 = np.random.random()
            r2 = np.random.random()
            A = 2 * a * r1 - a
            C = 2 * r2

            # 更新位置
            D = np.abs(C * rand_leader - position)
            new_position = rand_leader - A * D
            new_position = np.clip(new_position, search_range[0], search_range[1])

            # 更新适应度
            fitness = fitness_function(new_position)
            if fitness < best_fitness:
                best_fitness = fitness
                best_solution = new_position

            population[i] = new_position

        print(f"Iteration {iteration+1} Best Fitness: {best_fitness}")

    return best_solution

# 使用示例
num_iterations = 100
population_size = 50
num_dimensions = 2
search_range = [-10, 10]

best_solution = mirror_placement_optimization(num_iterations, population_size, num_dimensions, search_range)
print("Best Solution:", best_solution)
print("Best Fitness:", fitness_function(best_solution))