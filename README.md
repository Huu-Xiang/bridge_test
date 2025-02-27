# bridge_test
如果你不想按照我们的要求做而是想搭建一些更有趣的策略，我们十分欢迎！我们渴望看到你的创造力，你可以随时向我们的邮箱发送你的代码 litterpigger@gmail.com

如果你使用AI来帮助你完成答题，请你在该文件夹下新建一个名为prompt.txt的文件，并将你们的对话放入。如何正确的使用prompt与ai交互也是能力之一，使用ai不会对你的成绩有任何消极影响。

使用AI却不按上面这么做我们则会直接取消你的成绩。


[前置]

回测框架你可以自行搭建，也可以使用vnpy或backtrader等常用的回测框架

通过tushare sdk可以帮助你更方便的获取股票数据。你也可以自行下载数据。

https://tushare.pro/document/1?doc_id=7

https://tushare.pro/document/2

https://tushare.pro/document/1?doc_id=131

后端的框架请自行挑选，你可以自由的使用pip中所有的库


[要求]

你需要首先fork这个代码仓库到你的github,然后完成开发后提交到你的github上面，最后只需要发你的github代码仓库连接给我们就可以


1. 回测品类为平安银行，回测周期为2023年1月1日到12月31日。本金为1,000,000,每次买入为本金的百分之20.滑点为万分之一。 


2. 策略为当12日的价格均线穿越26日的价格均线时买入。当价格跌破26均线时卖出。你需要在backtest文件夹下完成策略的回测，并即将为后端提供结果


3. 你可以使用任意的python后端框架。你所需要实现的api: 第一个为post方法，为设置周期以及对应回测的股票。第二个为get方法，将该策略回测的结果的收益率,最后的总权益返回。


4.最后你需要在README.md中说明你的api使用方法，方便我们进行测试。




# backend/.env.example
TUSHARE_TOKEN="your_token_here"
FLASK_ENV=development