#导入相关第三方Python库
import backtrader as bt
import pandas as pd
import datetime
import matplotlib.pyplot as plt
#解决中文乱码
plt.rcParams["font.sans-serif"] = [u"SimHei"]
plt.rcParams["axes.unicode_minus"] = False 

import sys
f = open('交易记录.txt','w',encoding = 'utf-8') # 先打开要输出的文件
sys.stdout = f # 重定向到f文件
import warnings
warnings.filterwarnings("ignore")

#新建策略
class AceStrategy(bt.Strategy):
    params = (
        ('maperiod_10', 10),  #设置移动平均线天数
        ('maperiod_30',30)  #设置移动平均线天数
    )#设置相关交易策略的参数

    def __init__(self):
        self.inds = dict()
        for i, d in enumerate(self.datas):
            self.inds[d] = dict()

            #制定价格序列（收盘价）
            self.inds[d]['dataclose'] = self.datas[0].close

            #添加移动平均线指标(10日线、30日线）
            self.inds[d]['sma_10'] = bt.indicators.SimpleMovingAverage(
                self.datas[0], period=self.params.maperiod_10)
            self.inds[d]['sma_30'] = bt.indicators.SimpleMovingAverage(
                self.datas[0], period=self.params.maperiod_30)

            #初始化交易指令为空（None)
            self.inds[d]['order'] = None

    def start(self):
        pass

    def prenext(self):
        pass

    def nextstart(self):
        pass

    def next(self):
        for i, d in enumerate(self.datas):
            dt, dn = self.datetime.date(), d._name
            pos = self.getposition(d).size
            #检查是否持仓
            if not pos:#在没有持仓的情况下
                if self.inds[d]['sma_10']>self.inds[d]['sma_30']:#执行条件：10日线上穿30日线
                    # 执行买入指令，买入规模为1000000
                    self.inds[d]['order'] = self.buy(data=d, size=1000000)
                    #打印相关指令信息，包含买入时间、买入股票代码、买入价格
                    print(f"{self.datas[0].datetime.date(0)},买入{dn}，价格为{self.datas[i].close[0]}元/股")
            else:#有持仓情况下
                if self.inds[d]['sma_10']<self.inds[d]['sma_30']:#执行条件，10日线下穿30日线
                    #执行卖出指令，卖出规模为1000000
                    self.inds[d]['order'] = self.sell(data=d, size=1000000)
                    #打印先关指令信息，包含卖出时间、卖出股票代码、卖出价格
                    print(f"{self.datas[0].datetime.date(0)},卖出{dn}，价格为{self.datas[i].close[0]}元/股")

    def stop(self):
        pass

if __name__ == '__main__':
    #初始化cerebro回测系统设置
    cerebro = bt.Cerebro(stdstats=False)    #关闭observers观察者功能
    #cerebro自动实例化三个标准观察者
    cerebro.addobserver(bt.observers.Broker)  #经纪人观察者：用来跟踪现金和投资组合的价值
    cerebro.addobserver(bt.observers.Trades)  #交易观察者：会显示每笔交易所产生的影响
    cerebro.addobserver(bt.observers.BuySell) # 买/卖观察者：主要对订单操作进行记录
    # 设置初始资金金额
    cerebro.broker.set_cash(100000000.00)
    #获取初始资金金额并打印显示
    初始资金 = cerebro.broker.getvalue()
    print(f'初始资金:{初始资金}')

    stk_pools = pd.read_csv('多因子量化交易/数据地址/stock_code_update.csv')
    stk_num = 31  # 设置组合数量
    for i in range(stk_num): #设置循环
        #按顺序读取代码
        stk_code = stk_pools['code'][stk_pools.index[i]]
        stk_code = '%06d' %stk_code #设置补全6位数代码
        #根据代码读取相关股票代码交易数据集
        data = '多因子量化交易/数据地址/' + stk_code + '.csv'
        #加载数据，并设置回测时间(fromdate开始时间，todate截止时间)
        日线 = bt.feeds.GenericCSVData(  dataname=data,
                                        fromdate=datetime.datetime(2021, 1, 1),
                                        todate=datetime.datetime(2021, 12, 31),
                                        nullvalue=0.0,
                                        dtformat=('%Y-%m-%d')
                                          )
        #添加数据至cerebro回测系统
        cerebro.adddata(日线, name = stk_code)

    #将交易策略加载到回测系统当中
    cerebro.addstrategy(AceStrategy)


    # 添加分析指标
    # 返回年初至年末的年化收益率
    cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name='_AnnualReturn')
    # 计算最大回撤相关指标
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='_DrawDown')
    # 计算年化收益：日度收益
    cerebro.addanalyzer(bt.analyzers.Returns, _name='_Returns', tann=252)
    # 计算年化夏普比率：日度收益
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='_SharpeRatio', timeframe=bt.TimeFrame.Days, annualize=True,
                        riskfreerate=0)  # 计算夏普比率
    cerebro.addanalyzer(bt.analyzers.SharpeRatio_A, _name='_SharpeRatio_A')
    # 返回收益率时序
    cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='_TimeReturn')
    # 运行回测系统
    result = cerebro.run()
    # 提取结果
    期末资金 = cerebro.broker.getvalue()  # 获取期末资金，打印期末资金及收益率
    print(f'期末资金:{期末资金}，收益率为{(100 * (期末资金 - 初始资金) // 初始资金)}%')

    # 回测可视化
    # 添加 TimeReturn 分析器
    cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='_TimeReturn')
    # 提取收益序列
    pnl = pd.Series(result[0].analyzers._TimeReturn.get_analysis())
    # 计算累计收益
    cumulative = (pnl + 1).cumprod()
    # 计算回撤序列
    max_return = cumulative.cummax()
    drawdown = (cumulative - max_return) / max_return

    # 计算收益评价指标
    import pyfolio as pf

    # 按年统计收益指标
    perf_stats_year = (pnl).groupby(pnl.index.to_period('y')).apply(lambda data: pf.timeseries.perf_stats(data)).unstack()
    # 统计所有时间段的收益指标
    perf_stats_all = pf.timeseries.perf_stats((pnl)).to_frame(name='all')
    perf_stats = pd.concat([perf_stats_year, perf_stats_all.T], axis=0)
    perf_stats_ = round(perf_stats, 4).reset_index()

    # 绘制图形
    import matplotlib.pyplot as plt
    plt.rcParams['axes.unicode_minus'] = False   # 用来正常显示负号
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文
    import matplotlib.ticker as ticker  # 导入设置坐标轴的模块

    plt.style.use('seaborn')#设置可视化样式

    fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1.5, 4]}, figsize=(20, 8))
    cols_names = ['date', 'Annual\nreturn', 'Cumulative\nreturns', 'Annual\nvolatility',
                  'Sharpe\nratio', 'Calmar\nratio', 'Stability', 'Max\ndrawdown',
                  'Omega\nratio', 'Sortino\nratio', 'Skew', 'Kurtosis', 'Tail\nratio',
                  'Daily value\nat risk']

    # 绘制表格
    ax0.set_axis_off()  # 除去坐标轴
    table = ax0.table(cellText=perf_stats_.values,
                      bbox=(0, 0, 1, 1),  # 设置表格位置， (x0, y0, width, height)
                      rowLoc='right',  # 行标题居中
                      cellLoc='right',
                      colLabels=cols_names,  # 设置列标题
                      colLoc='right',  # 列标题居中
                      edges='open'  # 不显示表格边框
                      )
    table.set_fontsize(13)

    # 绘制累计收益曲线
    ax2 = ax1.twinx()
    ax1.yaxis.set_ticks_position('right')  # 将回撤曲线的 y 轴移至右侧
    ax2.yaxis.set_ticks_position('left')  # 将累计收益曲线的 y 轴移至左侧
    # 绘制回撤曲线
    drawdown.plot.area(ax=ax1, label='drawdown (right)', rot=0, alpha=0.3, fontsize=13, grid=False)
    # 绘制累计收益曲线
    (cumulative).plot(ax=ax2, color='#F1C40F', lw=3.0, label='cumret (left)', rot=0, fontsize=13, grid=False)
    # 不然 x 轴留有空白
    ax2.set_xbound(lower=cumulative.index.min(), upper=cumulative.index.max())
    # 主轴定位器：每 5 个月显示一个日期：根据具体天数来做排版
    ax2.xaxis.set_major_locator(ticker.MultipleLocator(100))
    # 同时绘制双轴的图例
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    plt.legend(h1 + h2, l1 + l2, fontsize=12, loc='upper left', ncol=1)

    fig.tight_layout()  # 规整排版
    plt.savefig('回测结果.png')