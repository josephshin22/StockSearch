import streamlit as st


def main():
    st.markdown(
        """
        <h3>View saved stocks here!</h3>
        """,
        unsafe_allow_html=True
    )

    if 'watchlist' in st.session_state and st.session_state.watchlist:
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
          
            </style>
            """,
            unsafe_allow_html=True
        )

        for ticker in st.session_state.watchlist:
            st.markdown(
                f"""
                <div class="rounded-box">
                    <span><h4>{ticker}</h4></span>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:
        st.write("Your watchlist is empty.")


if __name__ == "__main__":
    main()
