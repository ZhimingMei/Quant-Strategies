The idea comes from the financial engineering research report *量稳换手率选股因子——量小、量缩，都不如量稳?* from SOOCHOW Securities.

## Content
### Traditional Turnover Factor
Turn20: Calculate the average daily turnover rate of each stock over the past 20 trading days at the end of each month and neutralize the market value.

The IC is negative, and the smaller the turnover rate of stocks in the past month, the more likely they are to rise in the coming month.

Among the groups with the largest turnover rates, the future earnings of the constituents in the group vary greatly.

### Percent Turnover Factor    
**STEP:**
1. At the end of each month, we will review the past 20 trading days of all stocks and calculate the change rate of turnover rate for each trading day 
$$ DailyPctTurn = DailyTurn / BenchmarkTurn - 1 $$

2. The calculation of the benchmark turnover rate requires taking X (X=40) trading days further and calculating the average of the turnover rate for these X trading days.
3. After each stock gets the 20-day turnover rate change rate, calculate their average value, and then do a cross-sectional market value neutralization treatment.

During the entire backtesting period, the overall effect of the turnover rate change rate factor was not as good as the traditional turnover rate factor

### STR Factor (The Stability of Turnover Rate)
**STEP:**
1. At the end of each month, look back at the past 20 trading days of each stock and calculate the standard deviation of its 20-day turnover rate
2. Neutralize the market value on the cross section, that is, get the factor value of all stocks in the current month, and record it as the factor of stable volume turnover
