**股票回测系统**

这是一个基于 Flask 框架的股票回测系统，使用均线交叉策略（12日均线和26日均线）进行回测。用户可以通过 API 提供股票代码、回测时间区间和初始资金来运行回测，获取回测结果（包括收益率和最终总资金）。

*环境要求*
Python 3.12
安装所需的 Python 包：Flask, backtrader, tushare 等

*安装步骤*
克隆项目到本地：
`git clone https://github.com/your-repository/bridge_test.git`
`cd bridge_test`
创建并激活虚拟环境：
`python -m venv backtest_venv`
`source backtest_venv/bin/activate  # 在 Windows 上使用 `backtest_venv\Scripts\activate` `

*安装依赖：*
`pip install -r requirements.txt`
配置 Tushare API token：
需要在 [Tushare](https://tushare.pro) 注册并获取 API token，放在环境变量 TUSHARE_TOKEN 中，或者在代码中手动配置。

*运行项目*
启动 Flask 应用：
flask run --port 5000 --reload
在 Git Bash 或命令行中，使用 curl 命令测试回测 API：
`
curl -X POST http://localhost:5000/api/set_parameters -H "Content-Type: application/json" -d '{
    "ts_code": "000001.SZ",
    "start_date": "20200101",
    "end_date": "20201231",
    "initial_cash": 1000000
}'
`

ts_code：股票代码（如 000001.SZ 为平安银行）
start_date：回测开始日期（格式：YYYYMMDD）
end_date：回测结束日期（格式：YYYYMMDD）
initial_cash：初始资金，默认为 1,000,000

*回测结果*
返回结果是 JSON 格式：
`
{
  "data": {
    "final_value": 997171.59,
    "returns": -0.0028
  },
  "status": "success"
}
`
final_value：回测结束时的总资金。
returns：回测期间的收益率。

*说明*
回测策略：12日均线穿越26日均线时买入，价格跌破26日均线时卖出。
当前实现仅支持单只股票回测，未来可扩展为多只股票或其他策略。
项目结构
bridge_test/
├── backtest/
│   ├── strategy.py          # 策略代码
│   ├── backtest_engine.py   # 回测引擎
│   └── data_fetcher.py      # 数据获取模块（Tushare）
├── backend/
│   ├── app.py               # Flask 应用入口
│   ├── routes.py            # API 路由
│   └── config.py            # 配置文件
├── requirements.txt         # 项目依赖
└── README.md                # 项目说明文件