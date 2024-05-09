import os
import matplotlib.pyplot as plt

# 修改当前工作目录为指定目录
os.chdir('Python编程从入门到实践\\Datavisualization')
# # 打印修改后的当前工作目录
# print("修改后的工作目录:", os.getcwd())

# 折线图
# 默认第一个数据点对应的x坐标值为0
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
# 参数linewidth决定了plot()绘制的线条的粗细
plt.plot(squares,linewidth=5)

# 设置图表标题，并给坐标轴加上标签
# 函数title()给图表指定标题
# 参数fontsize指定了图表中文字的大小
plt.title("Square Numbers",fontsize=24)
# 函数xlabel()和ylabel()为每条轴设置标题
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
# 函数tick_params()设置刻度的样式，axis="both"表示同时影响x轴和y轴上的刻度
plt.tick_params(axis="both",labelsize=14)

# plt.show()打开matplotlib查看器，并显示绘制的图形
plt.show()