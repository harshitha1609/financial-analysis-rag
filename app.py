import streamlit as st
openai_api_key = st.secrets["OPENAI_API_KEY"]
news_api_key = st.secrets["NEWS_API_KEY"]
from rag_pipeline import get_rag_response
from utils.market_data import get_stock_data, plot_stock_chart
from utils.risk_model import calculate_risk
from utils.news_fetcher import fetch_news

st.set_page_config(page_title="Financial Analysis RAG", layout="wide")

st.title("💹 Financial Analysis RAG with Time-Series Data")

ticker = st.sidebar.text_input("Enter Stock Ticker (e.g. AAPL, TCS)", "AAPL")
query = st.sidebar.text_input("Ask a financial question", "Should I invest in this stock?")
period = st.sidebar.selectbox("Select Period", ["1mo", "3mo", "6mo", "1y"])

if st.sidebar.button("Analyze"):
    st.subheader(f"Analysis for {ticker}")

    # Market Data
    df = get_stock_data(ticker, period)
    if df.empty:
        st.warning("No stock data found for this ticker.")
    else:
        fig = plot_stock_chart(df)
        st.plotly_chart(fig, use_container_width=True)

        # Risk Assessment
        risk = calculate_risk(df)
        st.markdown(f"### Risk Level: **{risk}**")

    # News
    st.subheader("📰 Latest News")
    news = fetch_news(ticker)
    for article in news:
        st.write(f"- [{article['title']}]({article['url']})")

    # RAG Insights
    st.subheader("🤖 RAG Insights")
    answer = get_rag_response(query)
    st.write(answer)
