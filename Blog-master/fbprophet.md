# fbprophet --- facebook开源的时间序列预测工具

## 1、背景介绍
时间序列预测对大部分公司而言都存在必要的需求，prophet是一个工业级应用，并且使用起来比较简单，可以很快的搭载起来。
## 2、工具特点
1：工具支持R和python语言。
2：官方案例是使用日数据的序列，但对于更短时间频段，比如小时数据，也是支持的。
## 3、简单实践
官网上的一个数据案例是Peyton Manning的Wikipedia页面的日志每日页面浏览量的时间序列。这个数据可以说明了先知的一些特征，例如多个季节性，改变增长率，以及模拟特殊日子的能力（例如曼宁的季后赛和超级碗出场），具体数据在https://github.com/facebook/prophet下的examples目录。我们打开example_wp_log_peyton_manning.csv
如下所示：

Prophet的输入始终是一个包含两列的数据帧：ds和y。 ds（datestamp）列应为Pandas预期的格式，理想情况下为日期的YYYY-MM-DD或时间戳的YYYY-MM-DD HH：MM：SS。 y列必须是数字，表示我们希望预测的值。
下面我们通过实例化一个新的Prophet对象来拟合数据，因为fbprophet遵循sklearn模型API，使用fit和predict方法。 预测过程的任何设置都将传递到构造函数中。 然后调用其fit方法并传入历史数据帧。 Fit需要1-5秒。
```
	dataFrame = pd.read_csv('examples/example_wp_log_peyton_manning.csv')
	p = Prophet()
	p.fit(dataFrame)
```
然后在数据框上进行预测，其中列ds包含要进行预测的日期。 您可以使用辅助方法Prophet.make_future_dataframe，传入一个合适的数据帧，该数据帧将在未来延长指定的天数。
```
    future = p.make_future_dataframe(periods=365)
```
predict方法将在未来为每一行指定一个预测值，通过调用Prophet.plot方法绘制预测并传入预测数据帧。或者本文用的是Prophet.plot_components方法。 默认情况下，您将看到时间序列的趋势，年度季节性和每周季节性。 如果你包括假期，代码如下所示：

```
    forecast = p.predict(future)
    fig2 = p.plot_components(forecast)
    plt.show()
```
结果如下图：其中第一个图的2017年的部分，用灰色阴影标注的就是预测出来的值。
完整的Demo代码如下

```

    import pandas as pd
	import matplotlib.pyplot as plt
	from fbprophet import Prophet
	dataFrame = pd.read_csv('examples/example_wp_log_peyton_manning.csv')
	p = Prophet()
	p.fit(dataFrame)
	future = p.make_future_dataframe(periods=365)
	forecast = p.predict(future)
	fig2 = p.plot_components(forecast)
	plt.show()
```
## 4、模型介绍
Prophet的本质是一个可加模型，将时间序列中的几个线性函数和非线性函数拟合为组件。将时序预测问题看作一个曲线拟合问题。
基本形式如下：
y(t) = g(t) + s(t) + h(t) + εt
其中 g(t) 是趋势项，s(t) 是周期项， h(t) 是节假日项， 最后一项是误差项并且服从正态分布。

> g(t) 表示趋势函数，用来拟合时间序列中预测值的非周期性变化
>
>s(t) 用来表示周期性变化，比如说每周，每年中的季节等
>
>h(t) 表示时间序列中那些潜在的具有非固定周期的节假日对预测值造成的影响
>
>εt 为噪声项，表示模型未预测到的波动，这里假设它呈高斯正态分布

## 5、安装遇到的坑
win7系统安装用pip安装会失败，可以使用anaconda来安装。里面版本的坑也有不少，最后能成功运行的几个包的版本入下。
pystan (2.17.1.0)
fbprophet (0.3.post2）
matplotlib (2.0.2)
numpy (1.15.4)
pandas (0.23.4)
安装命令类似于conda install pystan==2.17.1.0
另外华为内网ananconda下载需要设置代理，可以自行去h3上查询。

ps：据说一些业务的交易数据跑了下预测，据说大部分都能work，诸如“春节效应”这种中国特色也能抓得比较准。
>参考资料：https://facebook.github.io/prophet/docs/quick_start.html#python-api

> https://facebook.github.io/prophet/docs/quick_start.html#python-api
