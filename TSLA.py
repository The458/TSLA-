# %%
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
from pandas_datareader import data as web
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from selenium import webdriver

# %%


log_file_path = "C:/print/print.log"
log_df = pd.read_csv(log_file_path, header=None)
log_df = log_df.drop_duplicates(ignore_index=True)
log_df = log_df.rename(columns={0: "Symbol"})
print(log_df)

# %%
yf.pdr_override()
currentday = datetime.today()
startdate = (currentday-timedelta(days=30)).strftime("%Y-%m-%d")
enddate = datetime.today().strftime("%Y-%m-%d")


# %%
df = pd.DataFrame()

for stock in log_df["Symbol"]:
    df[stock] = web.get_data_yahoo(stock, start=startdate,end=enddate)["Close"]
    

# %%
plt.figure(figsize=(40,20))
for c in df.columns.values:
    plt.plot(df[c], label=c)

plt.legend(df.columns.values, loc="upper left")
plt.ylabel("TWD")
plt.xlabel("Date")
plt.show()

# %%
returns = df.pct_change()
returns

# %%
#相關性
corration = returns.corr()


# %%
TSLA_corration = returns.corr()["TSLA"]
Top10_TSLA_corration = TSLA_corration.sort_values(ascending=False)[1:11]
Top10_TSLA_corration








