import streamlit as st


def main():
    st.markdown(
        """
        <h3>Welcome to <span style='color:red;'>StockSearch</span>, the CCI's proprietary stock research tool!</h3>
        """,
        unsafe_allow_html=True
    )

    st.write("Use the navigation menu to explore different sections.")

    # Add a description of capabilities with rounded corner boxes
    st.markdown(
        """
        <style>
        .rounded-box {
            border: 2px solid #f8d7da;
            border-radius: 15px;
            padding: 15px;
            margin: 10px;
            background-color: #f9e9e9;
        }
        </style>
        <div class="rounded-box">
            <h4>Key Features:</h4>
            <ul>
                <li><strong>Stock Information:</strong> Get detailed information about stocks, including company name, sector, industry, market cap, and more.</li>
                <li><strong>Historical Price Graphs:</strong> Visualize one-year historical prices of stocks with interactive charts.</li>
                <li><strong>Financial Ratios:</strong> Analyze key financial ratios to assess the financial health of a company.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
