import streamlit as st


def main():
    st.markdown(
        """
        <h3>View saved stocks here!</h3>
        """,
        unsafe_allow_html=True
    )

    if 'watchlist' not in st.session_state:
        st.session_state.watchlist = []

    if st.session_state.watchlist:
        st.markdown(
            """
            <style>
            .rounded-box {
                border: 2px solid #f8d7da;
                border-radius: 15px;
                padding: 15px;
                margin: 10px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: #f9e9e9;
            }
            .remove-button {
                background-color: #f5c6cb;
                border: none;
                padding: 5px 10px;
                color: #721c24;
                cursor: pointer;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
                margin-left: 10px;
                text-align: center;
            }
            .remove-button:hover {
                background-color: #f1b0b7;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        for ticker in st.session_state.watchlist:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(
                    f"""
                    <div class="rounded-box">
                        <span><h4>{ticker}</h4></span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col2:
                # Use st.button to create the button with the appropriate key
                if st.button('Remove', key=f'remove-{ticker}'):
                    st.session_state.watchlist.remove(ticker)
                    st.experimental_rerun()

    else:
        st.write("Your watchlist is empty.")


if __name__ == "__main__":
    main()
