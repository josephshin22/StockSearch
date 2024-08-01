import streamlit as st
from streamlit_option_menu import option_menu
import yfinance as yf
import plotly.express as px

# Define a function to display stock information


def display_stock_info(ticker):
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

# Define a function to display historical price graph


def display_historical_graph(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    fig = px.line(hist, x=hist.index, y='Close',
                  title=f"{ticker} Historical Prices")
    st.plotly_chart(fig)

# Define a function to display financial ratios


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
            st.write(f"**PEG Ratio:** {stock.info.get('pegRatio', 'N/A')}")

    except KeyError as e:
        st.write(f"Could not fetch some of the financial ratios: {e}")

# Main function to render the page


def main():
    st.title("Stock Information")
    st.write(
        "Enter a stock ticker symbol to get some basic information about the stock.")

    ticker = st.text_input("Stock Ticker")

    if ticker:
        selected = option_menu(
            menu_title=None,
            options=["Stock Info", "Historical Graph", "Financial Ratios"],
            icons=["info-circle", "graph-up", "calculator"],
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
