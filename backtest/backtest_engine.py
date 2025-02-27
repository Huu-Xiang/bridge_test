# backtest/backtest_engine.py
import backtrader as bt
from .data_fetcher import TushareDataFetcher
from .strategy import DoubleMAStrategy

class BacktestEngine:
    def __init__(self, token):
        self.fetcher = TushareDataFetcher(token)
        
    def run_backtest(self, params):
        cerebro = bt.Cerebro()
        
        # 动态获取数据
        data_df = self.fetcher.get_daily_data(
            ts_code=params['ts_code'],
            start_date=params['start_date'],
            end_date=params['end_date']
        )
        
        # 添加数据
        #data_df.set_index('date', inplace=True)
        data = bt.feeds.PandasData(dataname=data_df)
        cerebro.adddata(data)
        
        # 策略参数
        cerebro.addstrategy(
            DoubleMAStrategy,
            order_percentage=params.get('order_percentage', 0.2)
        )
        
        # 资金设置
        cerebro.broker.setcash(params.get('initial_cash', 1000000))
        cerebro.broker.set_slippage_perc(params.get('slippage', 0.0001))
        
        # 运行回测
        cerebro.run()
        
        # 获取结果
        final_value = cerebro.broker.getvalue()
        returns = (final_value - params['initial_cash']) / params['initial_cash']
        
        return {
            'returns': round(returns, 4),
            'final_value': round(final_value, 2)
        }
