import datetime
import os
import backtrader as bt


class MACDStrategy(bt.Strategy):
    params = (
        ('maperiod', 15),
    )

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.volume = self.datas[0].volume

        self.order = None
        self.buyprice = None
        self.buycomm = None

        # Compute MACD line and Signal line
        line1 = bt.indicators.EMA(self.datas[0], period=12)
        line2 = bt.indicators.EMA(self.datas[0], period=26)
        self.macd = line1 - line2
        self.signal = bt.indicators.EMA(self.macd, period=9)

        bt.indicators.MACDHisto(self.datas[0])

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm: %.2f' % (order.executed.price, order.executed.value, order.executed.comm))
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
                
            else:
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm: %.2f' % (order.executed.price, order.executed.value, order.executed.comm))
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order canceled/margin/rejected')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('Operation profit, Gross: %.2f, Net: %.2f' %
                 (trade.pnl, trade.pnlcomm))

    def next(self):
        '''
        Determine the strategy position:
        Buy the stock when the value of the MACD line < the value of the signal line indicates that a golden cross has occurred, at this time it is bullish.
        Sell in the opposite scenario.
        '''
        if self.order:
            return

        if not self.position:
            if self.macd[0] - self.signal[0] > 0:
                self.log('Buy create, %.2f' % self.dataclose[0])
                self.order = self.buy()

        else:
            if self.macd[0] - self.signal[0] < 0:
                self.log('Sell create, %.2f' % self.dataclose[0])
                self.order = self.sell()


if __name__ == '__main__':
    cerebro = bt.Cerebro()

    cerebro.addstrategy(MACDStrategy)
    cerebro.addsizer(bt.sizers.FixedSize, stake=100)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name = 'SharpeRatio')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name = 'DrawDown')

    cerebro.broker.setcash(10000)
    cerebro.broker.setcommission(commission=0.005)

    #! The data was retrieved from tushare
    #! Need to reindex the data in reverse order
    path = 'ENTER YOUR FILE PATH.'
    file_name = '002291.SZ.csv'
    datapath = os.path.join(path, file_name)
    data = bt.feeds.GenericCSVData(
        dataname=datapath,
        fromdate=datetime.datetime(2010, 1, 1),
        todate=datetime.datetime(2022, 6, 12),
        dtformat='%Y%m%d',
        datetime=2,
        open=3,
        high=4,
        low=5,
        close=6,
        volume=10,
        reverse=True
    )
    cerebro.adddata(data)

    start_balance = cerebro.broker.getvalue()
    results = cerebro.run()
    strategy_stats = results[0]
    end_balance = cerebro.broker.getvalue()

    print('---------------------------------------')
    print(f'Starting balance: {start_balance}')
    print(f'Ending balance: {end_balance}')
    print(f'Total return: {(end_balance-start_balance)/start_balance}')
    print('Sharpe Ratio: ', strategy_stats.analyzers.SharpeRatio.get_analysis())
    print('Drawdown: ', strategy_stats.analyzers.DrawDown.get_analysis())

    cerebro.plot(iplot=False)



## Another way to plot the result

# from backtrader_plotting import Bokeh
# from backtrader_plotting.schemes import Tradimo

# b = Bokeh(style='bar', plot_mode='single', scheme=Tradimo())
# cerebro.plot(b, iplot=False)