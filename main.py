import streamlit as st
from streamlit_option_menu import option_menu


def main():

    # Sidebar for navigation
    with st.sidebar:
        selected = option_menu(
            "Navigation",
            ["Home", "Sector Data", "Stock Information",
                "Economic Features", "DCF Analysis"],
            icons=["house", "bar-chart", "info-circle",
                   "graph-up", "calculator"],
            menu_icon="cast",
            default_index=0
        )

    # Display the selected page
    if selected == "Home":
        import Home
        Home.main()
    elif selected == "Stock Information":
        import StockInfo
        StockInfo.main()


if __name__ == "__main__":
    main()
