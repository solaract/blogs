import os
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 修改当前工作目录为指定目录
os.chdir('Python编程从入门到实践\\Datavisualization')
# # 打印修改后的当前工作目录
# print("修改后的工作目录:", os.getcwd())


# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()
    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))
    # plt.scatter(rw.x_values,rw.y_values,s=15)
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,s=1,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none')

    # 突出起点和终点
    plt.scatter(0,0,c='green',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)


    # 隐藏坐标轴
    # plt.axis('off')
    # 获取当前图形的坐标轴对象
    ax = plt.gca()
    # 隐藏 x 轴
    ax.get_xaxis().set_visible(False)
    # 隐藏 y 轴
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break