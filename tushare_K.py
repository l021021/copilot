import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf

#从tushare获取数据,并画出K线图


df = ts.get_hist_data('600848',start='2018-01-05',end='2023-06-09')
#如何得到一份dataframe的index列
    

#date的数据类型是什么
#df.index   是什么?
#改df['date']为DatetimeIndex
df.index = pd.to_datetime(df.index)




#df的数据结构
#date	open	high	close	low	volume	price_change	p_change	ma5	ma10	ma20	v_ma5	v_ma10	v_ma20	turnover
#2018-01-09	22.00	22.00	21.00	20.55	1.00	-1.00	-4.55	21.00	21.00	21.00	1.00	1.00	1.00	0.00

#把df画成K线图
#利用mpf 绘制K线图
#mpf.plot(df,type='candle',mav=(5,10,20),volume=True)
#如何调用mpf.plot   


mpf.plot(df,type='candle',mav=(5,10,20),volume=True,show_nontrading=True)
#mpf.plot(df,type='candle',mav=(5,10,20),volume=True,show_nontrading=True,style='yahoo')

#绘制pe-band图
#从tushare获取财务数据




