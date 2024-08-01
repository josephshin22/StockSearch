import streamlit as st
import yfinance as yf


def display_stock_info(ticker):
    ticker = ticker.upper()
    stock = yf.Ticker(ticker)
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Ticker:** {ticker}")
        st.write(f"**Company Name:** {stock.info['longName']}")
        st.write(f"**Sector:** {stock.info['sector']}")
        st.write(f"**Industry:** {stock.info['industry']}")
        st.write(f"**Country:** {stock.info['country']}")
        st.write(f"**Market Cap:** ${stock.info['marketCap']:,}")

    with col2:
        st.write(f"**Price:** ${stock.history(period='1d')['Close'][0]:.2f}")
        st.write(
            f"**Dividend Yield:** {stock.info.get('dividendYield', 'N/A')}")
        st.write(f"**52 Week High:** ${stock.info['fiftyTwoWeekHigh']}")
        st.write(f"**52 Week Low:** ${stock.info['fiftyTwoWeekLow']}")
        st.write(f"**P/E Ratio:** {stock.info.get('trailingPE', 'N/A')}")

    if st.button('Add to Watchlist'):
        if 'watchlist' not in st.session_state:
            st.session_state.watchlist = []
        if ticker not in st.session_state.watchlist:
            st.session_state.watchlist.append(ticker)
            st.success(f'{ticker} added to watchlist')
        else:
            st.info(f'{ticker} is already in the watchlist')


def main():
    st.title("Stock Information")
    ticker = st.text_input("Enter Stock Ticker")
    if ticker:
        display_stock_info(ticker)


if __name__ == "__main__":
    main()
