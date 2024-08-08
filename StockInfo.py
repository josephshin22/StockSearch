import streamlit as st
import yfinance as yf
from streamlit_option_menu import option_menu
import plotly.express as px


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


def get_historical_data(ticker, period):
    stock = yf.Ticker(ticker)
    return stock.history(period=period)


def display_historical_graph(ticker):
    # Add a horizontal bar of buttons for time period selection without icons
    period = option_menu(
        menu_title=None,  # No menu title, just options
        options=["1mo", "3mo", "6mo", "ytd", "1y", "5y", "max"],
        menu_icon="calendar",  # Icon shown for the menu
        default_index=3,  # Default to "1y"
        orientation="horizontal",
        styles={
            "container": {"padding": "0", "margin": "0"},
            "nav-link": {"font-size": "14px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#06c1a4"},
        },
    )

    hist = get_historical_data(ticker, period)
    fig = px.line(hist, x=hist.index, y='Close', title=f"{
                  ticker} Historical Prices ({period})")
    st.plotly_chart(fig)


def display_financial_ratios(ticker):
    stock = yf.Ticker(ticker)
    try:
        st.write("### Financial Ratios")
        col1, col2 = st.columns(2)

        with col1:
            st.write(
                f"**Current Ratio:** {stock.info.get('currentRatio', 'N/A')}")
            st.write(f"**Quick Ratio:** {stock.info.get('quickRatio', 'N/A')}")
            st.write(
                f"**Debt to Equity Ratio:** {stock.info.get('debtToEquity', 'N/A')}")
            st.write(
                f"**Return on Equity (ROE):** {stock.info.get('returnOnEquity', 'N/A')}")
            st.write(
                f"**Return on Assets (ROA):** {stock.info.get('returnOnAssets', 'N/A')}")
            st.write(
                f"**Return on Investment (ROI):** {stock.info.get('returnOnInvestment', 'N/A')}")
            st.write(
                f"**Gross Margin:** {stock.info.get('grossMargins', 'N/A')}")
            st.write(
                f"**Operating Margin:** {stock.info.get('operatingMargins', 'N/A')}")
            st.write(
                f"**Net Profit Margin:** {stock.info.get('profitMargins', 'N/A')}")

        with col2:
            st.write(f"**P/S Ratio:** {stock.info.get('priceToSales', 'N/A')}")
            st.write(f"**P/E Ratio:** {stock.info.get('trailingPE', 'N/A')}")
            st.write(f"**P/B Ratio:** {stock.info.get('priceToBook', 'N/A')}")
            st.write(f"**PEG Ratio:** {stock.info.get('trailingPegRatio', 'N/A')}")

    except KeyError as e:
        st.write(f"Could not fetch some of the financial ratios: {e}")


def main():
    st.title("Stock Information")
    st.write(
        "Enter a stock ticker symbol to get some basic information about the stock.")

    ticker = st.text_input("Stock Ticker")

    if ticker:
        selected = option_menu(
            menu_title=None,
            options=["Stock Info", "Historical Graph", "Financial Ratios"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )

        if selected == "Stock Info":
            display_stock_info(ticker)
        elif selected == "Historical Graph":
            display_historical_graph(ticker)
        elif selected == "Financial Ratios":
            display_financial_ratios(ticker)
    else:
        st.write("Please enter a stock ticker symbol.")


if __name__ == "__main__":
    main()
