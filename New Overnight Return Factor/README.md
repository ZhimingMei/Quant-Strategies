The idea comes from the FE research report *如何将隔夜涨跌变为有效的选股因子？--基于对知情交易者信息优势的刻画* from GUOSHENG Securites.

## Previous Research

- The traditional return factor     **Ret20**          
- The traditional overnight return factor       **OvernightRet**       
  The cumulative overnight increase or decrease of the stock over the past 20 trading days (today's open/yesterday's close -1)         
- Absolute overnight factor（隔夜跳空因子）     **abs_OvernightRet**        
  Method: Take absolute value of the overnight return          
  **Logical: Stocks with a large overnight gap may have short-term trading overheating, but there is no clear explanation for why short-term trading overheating leads to poor future performance**         
  Further: Market capitalization neutralization of cross-sectional data     
 
**All existing factors lack stability, and the effect is average (not so good)**

## New Overnight Return Factor

### Ideas

To discuss the impact of short-term overheating on future performance, we need to add volume information based on previous ideas.

### Steps

> 中文步骤
>  1. 每月月底，每只股票回溯过去20个交易日，计算**每日隔夜涨跌幅绝对值与昨日换手率的相关系数**
>  2. 做横截面市值中性化处理

> English Version
>  1. At the end of each month, look back 20 trading days for each stock to calculate **the correlation coefficient between the absolute value of the daily overnight change and yesterday's turnover rate**
>  2. Conduct cross-sectional market value neutralization

Further, since we want to provide incremental information beyond the previous research, we will orthogonalize the new factor constructed above to ***OvernightRet_desize***, take the residual. 

Define the residual as the final factor ***New_OvernightRet***

## Logics

### What does the correlation coefficient reflect?

**This factor actually measures the market inefficiency, namely *MIF (Market Inefficiency Factor)***

In the absence of overnight information, today's opening price should be roughly equal to yesterday's closing price

So, if the stock price gaps sharply at today's open, then it can be inferred that there is a high probability of overnight information. Since the market is not completely efficient, some investors may have an information advantage.         
If yesterday's turnover rate is higher than other trading days, investors with an information advantage are more likely to obtain overnight information in advance.

The higher the factor value -- the higher the correlation between the overnight return and the turnover rate           

----> It indicates that in the past period of time, informed traders have a greater information advantage in this stock, and they are often able to obtain overnight information and act in advance.       
**The market efficiency of the stock will be weak** 
