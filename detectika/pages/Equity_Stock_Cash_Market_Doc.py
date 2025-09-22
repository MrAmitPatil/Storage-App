import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title('Equity Stock Cash Market')

st.header("What is Cash Market?")
st.markdown("""            
A cash market is a marketplace in which securities purchased are paid for and received at the point of sale. 
Each trade in the stock market has to be settled once the trading session ends. Indian markets now follow the T+1 (Trade + 1) settlement cycle, which means that the trades are settled a day after they are executed.
What our data contains?
The data in the table primarily represents cash market orders. In the cash market, securities like stocks are bought and sold for immediate delivery and payment, facilitating direct exchange between buyers and sellers. Unlike futures or options markets, transactions in the cash market involve the physical transfer of assets and immediate settlement in cash. It represents the real-time, spot trading of financial instruments at prevailing market prices. Cash market trades are straightforward, with ownership transferred upon completion, making it distinct from derivative markets.
""")


st.header("What our data contains?")
st.markdown("""The data in the table primarily represents cash market orders. In the cash market, securities like stocks are bought and sold for immediate delivery and payment, facilitating direct exchange between buyers and sellers. Unlike futures or options markets, transactions in the cash market involve the physical transfer of assets and immediate settlement in cash. It represents the real-time, spot trading of financial instruments at prevailing market prices. Cash market trades are straightforward, with ownership transferred upon completion, making it distinct from derivative markets.""")


column_descriptions = [
    {"Column": "UserID", "Description" : " This field should contain the ID of the user."},
    {"Column": "TokenNo", "Description" : " It is a unique number given to a particular symbol-series combination."},
    {"Column": "Symbol", "Description" : " This field contains the Symbol of the security."},
    {"Column": "Series", "Description" : " This field contains the series of a security."},
    {"Column": "Buy/Sell Indicator", "Description" : " This field should contain one of the following values to specify whether the order is a buy or sell order \n1 denotes Buy order \n2 denotes Sell order"},
    {"Column": "Volume", "Description" : " This field should contain the order quantity."},
    {"Column": "Price", "Description" : " This field should contain the price at which the order is placed."},
    {"Column": "Branch Id", "Description" : " This field should contain the branch number to which the broker belongs."},
    {"Column": "Trader Id", "Description" : " It could be the identifier of the trader responsible for executing the transaction."},
    {"Column": "Broker Id", "Description" : " This column likely represents the identifier of the broker associated with the transaction. The broker is an intermediary facilitating the buying or selling of stocks."},
    {"Column": "Pro/Client Indicator", "Description" : " This field should contain one of the following values to specify whether the order is entered on behalf of a broker or a trader. \n1 represents the client's order. \n2 represents a broker's order."}
]
df = pd.DataFrame.from_dict(data=column_descriptions)

st.header("Significance and use of each column")
st.dataframe(df, hide_index=True, use_container_width=True)


sample_data = [{
    "user_id" : "5063634",
    "token_no" : "12706",
    "symbol" : "ACC",
    "series" : "EQ",
    "buy_sell_indicator" : "1 (Buy)",
    "volume" : "38",
    "price" : "1807",
    "branch_id" : "1",
    "trader_id" : "5063634",
    "broker_id" : "34",
    "pro_client_indicator" : "1 (Client)"
}]
sample_data_df = pd.DataFrame.from_dict(sample_data)

st.header("Sample Data with Explanation")
st.markdown("""The below data indicates that the user with ID 5063634, is a client, who has placed buy order of 38 shares of the stock with symbol ACC in the equity series at a price of 1807 per share, and the transaction is associated with branch 1 and broker 34.""")
st.dataframe(sample_data_df, hide_index=True, use_container_width=True)


st.header("Usage Examples")
st.text("Basic query on the Cash Market data")
st.code("""
SELECT 
    CM.USER_ID, 
    CM.TOKEN_NO, 
    CM.SYMBOL, 
    CM.SERIES, 
    CM.BUY_SELL_INDICATOR, 
    CM.VOLUME, 
    CM.PRICE, 
    CM.BRANCH_ID, 
    CM.TRADER_ID, 
    T.TRADER_NAME,
    CM.BROKER_ID, 
    B.BROKER_NAME,
    CM.PRO_CLIENT_INDICATOR
FROM
    MARKET_DATA.CASH_MARKET_TRADE CM
LEFT JOIN
    MARKET_DATA.BROKERS B
ON
    B.BROKER_ID = CM.BROKER_ID
LEFT JOIN
    MARKET_DATA.TRADERS T
ON 
    T.TRADER_ID = CM.TRADER_ID;
""", language='sql', line_numbers=True)

st.text("Query the market data for a specific trader")
st.code("""
SELECT 
    CM.USER_ID, 
    CM.TOKEN_NO, 
    CM.SYMBOL, 
    CM.SERIES, 
    CM.BUY_SELL_INDICATOR, 
    CM.VOLUME, 
    CM.PRICE, 
    CM.BRANCH_ID, 
    CM.TRADER_ID, 
    T.TRADER_NAME,
    CM.BROKER_ID, 
    B.BROKER_NAME,
    CM.PRO_CLIENT_INDICATOR
FROM
    MARKET_DATA.CASH_MARKET_TRADE CM
LEFT JOIN
    MARKET_DATA.BROKERS B
ON
    B.BROKER_ID = CM.BROKER_ID
LEFT JOIN
    MARKET_DATA.TRADERS T
ON 
    T.TRADER_ID = CM.TRADER_ID
WHERE 
    CM.TRADER_ID=5002335;
""", language='sql')

st.text("Query the market data for a specific Broker")
st.code("""
SELECT 
    CM.USER_ID, 
    CM.TOKEN_NO, 
    CM.SYMBOL, 
    CM.SERIES, 
    CM.BUY_SELL_INDICATOR, 
    CM.VOLUME, 
    CM.PRICE, 
    CM.BRANCH_ID, 
    CM.TRADER_ID, 
    T.TRADER_NAME,
    CM.BROKER_ID, 
    B.BROKER_NAME,
    CM.PRO_CLIENT_INDICATOR
FROM
    MARKET_DATA.CASH_MARKET_TRADE CM
LEFT JOIN
    MARKET_DATA.BROKERS B
ON
    B.BROKER_ID = CM.BROKER_ID
LEFT JOIN
    MARKET_DATA.TRADERS T
ON 
    T.TRADER_ID = CM.TRADER_ID
WHERE 
    CM.BROKER_ID=1;
""", language='sql')

st.text("Query the market data for a specific symbol")
st.code("""
SELECT 
    CM.USER_ID, 
    CM.TOKEN_NO, 
    CM.SYMBOL, 
    CM.SERIES, 
    CM.BUY_SELL_INDICATOR, 
    CM.VOLUME, 
    CM.PRICE, 
    CM.BRANCH_ID, 
    CM.TRADER_ID, 
    T.TRADER_NAME,
    CM.BROKER_ID, 
    B.BROKER_NAME,
    CM.PRO_CLIENT_INDICATOR
FROM
    MARKET_DATA.CASH_MARKET_TRADE CM
LEFT JOIN
    MARKET_DATA.BROKERS B
ON
    B.BROKER_ID = CM.BROKER_ID
LEFT JOIN
    MARKET_DATA.TRADERS T
ON 
    T.TRADER_ID = CM.TRADER_ID
WHERE 
    CM.SYMBOL='ITC';
""", language='sql')