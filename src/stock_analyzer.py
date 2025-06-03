import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Optional, Dict
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import talib
from pynance import Stock

class StockAnalyzer:
    def __init__(self, ticker: str):
        self.ticker = ticker.upper()
        self.stock = yf.Ticker(self.ticker)
        self._info = None

    @property
    def info(self) -> Dict:
        if self._info is None:
            self._info = self.stock.info
        return self._info

    def get_historical_data(
        self,
        period: str = "1y",
        interval: str = "1d",
        start: Optional[str] = None,
        end: Optional[str] = None
    ) -> pd.DataFrame:
        if start and end:
            data = self.stock.history(start=start, end=end, interval=interval)
        else:
            data = self.stock.history(period=period, interval=interval)
        return data

    def calculate_manual_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        # Simple Moving Averages
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['SMA_50'] = df['Close'].rolling(window=50).mean()

        # RSI
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))

        # MACD
        exp1 = df['Close'].ewm(span=12, adjust=False).mean()
        exp2 = df['Close'].ewm(span=26, adjust=False).mean()
        df['MACD'] = exp1 - exp2
        df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()

        return df

    def calculate_talib_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df['SMA_20_talib'] = talib.SMA(df['Close'], timeperiod=20)
        df['RSI_talib'] = talib.RSI(df['Close'], timeperiod=14)
        macd, macdsignal, _ = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        df['MACD_talib'] = macd
        df['Signal_Line_talib'] = macdsignal
        return df

    def add_pynance_metrics(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        stock = Stock(self.ticker)
        stock.load_data(df)
        df['Volatility'] = stock.volatility()
        df['Sharpe_Ratio'] = stock.sharpe_ratio()
        df['Drawdown'] = stock.drawdown()
        return df

    def plot_stock_data(
        self,
        df: pd.DataFrame,
        indicators: bool = True,
        volume: bool = True
    ):
        fig = make_subplots(
            rows=2 if volume else 1,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.03,
            row_heights=[0.7, 0.3] if volume else [1]
        )

        fig.add_trace(
            go.Candlestick(
                x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                name='OHLC'
            ),
            row=1, col=1
        )

        if indicators:
            for col_name, color in [('SMA_20', 'blue'), ('SMA_50', 'red')]:
                if col_name in df.columns:
                    fig.add_trace(
                        go.Scatter(x=df.index, y=df[col_name], mode='lines', name=col_name, line=dict(color=color)),
                        row=1, col=1
                    )

        if volume:
            fig.add_trace(
                go.Bar(x=df.index, y=df['Volume'], name='Volume'),
                row=2, col=1
            )

        fig.update_layout(
            title=f'{self.ticker} Stock Price',
            yaxis_title='Price',
            xaxis_title='Date',
            template='plotly_white'
        )

        fig.show()


