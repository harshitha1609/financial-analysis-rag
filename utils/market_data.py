import yfinance as yf
import plotly.graph_objects as go

def get_stock_data(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    return df

def plot_stock_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], mode="lines", name="Close Price"))
    fig.update_layout(title="Stock Price Trend", xaxis_title="Date", yaxis_title="Price")
    return fig
