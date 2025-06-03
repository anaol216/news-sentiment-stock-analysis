import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import talib

class StockAnalyzer:
    def __init__(self, ticker):
        self.ticker = ticker

    def get_stock_data(self, start_date, end_date):
        stock = yf.Ticker(self.ticker)
        df = stock.history(start=start_date, end=end_date)
        df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
        df.dropna(inplace=True)
        return df

    def calculate_technical_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
        df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
        df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
        df['MACD'], df['MACD_signal'], _ = talib.MACD(df['Close'])
        return df

    def add_performance_metrics(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df['Daily Return'] = df['Close'].pct_change()

        # Volatility (30-day rolling)
        df['Volatility'] = df['Daily Return'].rolling(window=30).std()

        # Sharpe Ratio (annualized)
        df['Sharpe_Ratio'] = (
            df['Daily Return'].rolling(window=30).mean() /
            df['Daily Return'].rolling(window=30).std()
        ) * np.sqrt(252)

        # Max Drawdown
        df['Cumulative_Return'] = (1 + df['Daily Return']).cumprod()
        df['Cumulative_Max'] = df['Cumulative_Return'].cummax()
        df['Drawdown'] = df['Cumulative_Return'] / df['Cumulative_Max'] - 1

        return df

    def plot_stock_data(self, df: pd.DataFrame):
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close'))
        fig.add_trace(go.Scatter(x=df.index, y=df['SMA_20'], mode='lines', name='SMA 20'))
        fig.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], mode='lines', name='SMA 50'))
        fig.add_trace(go.Scatter(x=df.index, y=df['MACD'], mode='lines', name='MACD'))
        fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], mode='lines', name='RSI'))

        fig.update_layout(title=f"{self.ticker} Stock Analysis",
                          xaxis_title='Date',
                          yaxis_title='Price & Indicators',
                          legend_title='Legend')
        fig.show()
