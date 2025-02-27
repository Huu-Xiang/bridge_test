# backtest/data_fetcher.py
import tushare as ts
import pandas as pd
from datetime import datetime

class TushareDataFetcher:
    def __init__(self, token):
        self.pro = ts.pro_api(token)
        
    def get_daily_data(self, ts_code, start_date, end_date):
        """获取日线数据并转换为Backtrader兼容格式"""
        df = self.pro.daily(
            ts_code=ts_code,
            start_date=start_date,
            end_date=end_date
        )
        
        # 格式转换
        df = df.sort_values('trade_date')
        df['trade_date'] = pd.to_datetime(df['trade_date'], format='%Y%m%d')
        df.rename(columns={
            'trade_date': 'date',
            'vol': 'volume'
        }, inplace=True)
        df.set_index('date', inplace=True)
        return df[['open', 'high', 'low', 'close', 'volume']]
