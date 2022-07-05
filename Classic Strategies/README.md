# Classic Strategies

## Momentum Strategy

### Digest Summary
**Momentum strategies** exploit a tendency for a stock's prior returns and prior news about its earnings to predict future returns. The authors confirm momentum for subsequent six-month and one-year periods. Prior returns and prior earnings contribute to predicted future returns after controlling for the other.

### Idea
In a certain period of time, if a stock or a stock portfolio performed well (poorly) in the previous period, the stock or stock portfolio will still perform well (poorly) in the next period.

For coding and implementing details, please refer to the code file.             
> momentum.ipynb      
    
*Updates: Jun 10, 2022*


## MACD Strategy

### Digest Summary
The **MACD line and signal line** can be utilised in much the same manner as a stochastic oscillator, with the crossover between the two lines providing buy and sell signals. As with most crossover strategies, a buy signal comes when the shorter-term, more reactive line – in this case the MACD line – crosses above the slower line – the signal line. Conversely, when the MACD line crosses below the signal line it provides a bearish sell signal.

### Figure
![figure1](https://github.com/ZhimingMei/Quant-Strategies/blob/main/Classic%20Strategies/macd_bt.png)
### Reference
IG.com provides the digest summary of this strategy. Refer to https://www.ig.com/en/trading-strategies/macd-trading-strategy-190610 for more details.             
pythondict.com provides the idea and some recurrence details. Link: https://pythondict.com/quant/backtrader-easy-quant-macd-26profit/ 

### Files
> macd.ipynb         
> mack_bt.py

The second file use backtrader package to construct the backtesting framework.        
*Updates: Jul 4, 2022*
