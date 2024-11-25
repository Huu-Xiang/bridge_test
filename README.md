# easy_test
如果你不想按照我们的要求做而是想搭建一些更有趣的策略，我们十分欢迎！我们渴望看到你的创造力，你可以随时向我们的邮箱发送你的代码 litterpigger@gmail.com

如果你使用AI来帮助你完成答题，请你在该文件夹下新建一个名为prompt.txt的文件，并将你们的对话放入。如何正确的使用prompt与ai交互也是能力之一，使用ai不会对你的成绩有任何消极影响。

使用AI却不按上面这么做我们则会直接取消你的成绩。


[前置]

你需要库为backtrader,tushare以及pandas。你可以通过pip install进行安装。

backtrader的文档为：https://www.backtrader.com/docu/

tushare api的文档为：https://tushare.pro/document/2?doc_id=27


[要求]

你需要首先folk这个代码仓库到你的github,然后完成开发后提交到你的github上面，最后只需要发你的github代码仓库连接给我们就可以


1. 回测品类为平安银行，tushare中的代码为'000001.SZ'，回测周期为2023年1月1日到12月31日。 在api_manager.py中完成数据的抓取。

2. 在backtest的文件的signal的文件夹下的buy_signal中写入你的均线买入策略。策略为当12日的价格均线穿越26日的价格均线时买入。

3. 当价格跌破26日均线时候卖出，将其写在sell_signal中

4. 在strategy.py中调用buy_signal以及sell_signal完成策略的开发。

5. 对于backtrader中cerebro的参数你需要在config.py中设置，为全局调用。要求为初始金额1000万元，每次开仓50万元，滑点万分之一。

6.最后在__main__.py中完成组装。



