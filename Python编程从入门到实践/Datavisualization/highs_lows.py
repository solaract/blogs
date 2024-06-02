import csv,os
from matplotlib import pyplot as plt
from datetime import datetime

# 修改当前工作目录为指定目录
os.chdir('Python编程从入门到实践\\Datavisualization')
# # 打印修改后的当前工作目录
# print("修改后的工作目录:", os.getcwd())

# 从文件中获取日期、最高气温和最低气温
filename = "death_valley_2014.csv"
with open(filename) as f:
    # 调用csv.reader()，并将前面存储的文件对象作为实参传递给它，从而创建一个与该文件相关联的阅读器（reader）对象
    reader = csv.reader(f)
    # 模块csv包含函数next()，调用它并将阅读器对象传递给它时，它将返回文件中的下一行
    header_row = next(reader)
    # print(header_row)
    # 调用enumerate()来获取每个元素的索引及其值
    # for index, column_header in enumerate(header_row):
    #     print(index,column_header)
    
    dates,highs,lows = [],[],[]
    # 阅读器对象从其停留的地方继续往下读取CSV文件，每次都自动返回当前所处位置的下一行。由于我们已经读取了文件头行，这个循环将从第二行开始
    for row in reader:
        try:
            # 调用方法strptime()，并将包含所需日期的字符串作为第一个实参。第二个实参告诉Python如何设置日期的格式
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            # ：打印一条错误消息，指出缺失数据的日期。打印错误消息后，循环将接着处理下一行
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128,figsize=(10,6))
    # 实参alpha指定颜色的透明度。Alpha值为0表示完全透明，1（默认设置）表示完全不透明
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    # 方法fill_between()，它接受一个x值系列和两个y值系列，并填充两个y值系列之间的空间
    # 实参facecolor指定了填充区域的颜色
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

    # 设置图形的格式
    plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=24)
    plt.xlabel('',fontsize=16)
    # 调用fig.autofmt_xdate()来绘制斜的日期标签，以免它们彼此重叠
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()