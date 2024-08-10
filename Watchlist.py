import streamlit as st


def main():
    st.markdown(
        """
        <h3 style='text-align: center;'>📈 Your Watchlist</h3>
        <p style='text-align: center;'>Keep track of your favorite stocks!</p>
        """,
        unsafe_allow_html=True
    )

    if 'watchlist' not in st.session_state:
        st.session_state.watchlist = []

    if st.session_state.watchlist:
        for ticker in st.session_state.watchlist:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"**{ticker}**")
            with col2:
                st.button(
                    'Remove', key=f'remove-{ticker}', on_click=lambda t=ticker: remove_stock(t))
    else:
        st.markdown(
            """
            **Your watchlist is empty.**
            Add some stocks to get started!
            """,
        )


def remove_stock(ticker):
    st.session_state.watchlist.remove(ticker)
    st.experimental_rerun()


if __name__ == "__main__":
    main()
