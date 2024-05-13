import os
import matplotlib.pyplot as plt

# 修改当前工作目录为指定目录
os.chdir('Python编程从入门到实践\\Datavisualization')
# # 打印修改后的当前工作目录
# print("修改后的工作目录:", os.getcwd())

# plt.scatter(2,4,s=200)
# x_value = [1,2,3,4,5]
# y_value = [1,4,9,16,25]
x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

# 传递实参edgecolor='none'删除数据点的轮廓
# 传递实参c修改修改数据点颜色，可使用颜色的名称“red”或RGB值组成的元组“(0,0,0.8)”
# plt.scatter(x_value,y_value,s=40,edgecolors='none',c=(0,0,0.8))
# 颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色
# 参数c设置成一个y值列表
# 参数cmap设置使用哪个颜色映射
plt.scatter(x_value,y_value,s=40,edgecolors='none',c=y_value,cmap=plt.cm.Blues)


# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both",which="major",labelsize=14)

# plt.show()

# 实参bbox_inches='tight'表示将图表多余的空白区域裁剪掉
plt.savefig('square_plot.png',bbox_inches='tight')