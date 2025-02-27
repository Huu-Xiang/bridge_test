# strategy.py
import backtrader as bt

class DoubleMAStrategy(bt.Strategy):
    params = (
        ('ma_fast', 12),
        ('ma_slow', 26),
        ('order_percentage', 0.2),
    )

    def __init__(self):
        self.ma_fast = bt.indicators.SMA(self.data.close, period=self.p.ma_fast)
        self.ma_slow = bt.indicators.SMA(self.data.close, period=self.p.ma_slow)
        self.crossover = bt.indicators.CrossOver(self.ma_fast, self.ma_slow)
        
    def next(self):
        if not self.position:
            if self.crossover > 0:  # 金叉
                amount = self.broker.getvalue() * self.p.order_percentage
                self.order_target_value(target=amount)
        else:
            if self.data.close < self.ma_slow:  # 跌破慢线
                self.close()
