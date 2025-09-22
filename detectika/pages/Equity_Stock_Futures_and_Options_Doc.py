import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title('Equity Stock Futures & Options')


st.header('What is Future and Option?')
st.markdown("""
Futures and Options (F&O) are derivative products in the stock market. Since they derive their values from an underlying asset, like shares or commodities, they are called derivatives.
""")


st.header('Types of Futures and Options')
st.markdown("""
**Futures:** Futures are contracts that have to be settled (paid for) once you enter into them. If you enter a futures contract, you are obligated to buy or sell the underlying asset at a pre-specified price on or prior to a certain date.
""")
st.markdown("""
**Options:** An options contract is the right, and not the obligation, for its buyer to buy or sell the underlying asset at a certain price on or prior to a fixed date. Options are a good way to trade in stocks without owning them. If the option buyer does not want to buy or sell the underlying asset, they can decide not to do so.
""")


st.header('Types of options')
st.markdown("""
- **Call Options:** A Call option gives the buyer/ holder the right but not the obligation to buy a specified quantity of an underlying asset.
- **Put options:** A Put option gives buyer/ holder the right but not the obligation to sell specified quantity of an underlying asset. 
""")


st.header('What our data contains?')
st.markdown("""
The data in the table primarily represents future and options trading, which involves the buying and selling of futures and options contracts. Both futures and options are derivative instruments that derive their value from an underlying asset. Futures involve an obligation to buy or sell at a future date, while options provide the right (but not the obligation) to buy or sell at a predetermined price before or on the expiration date.
""")


column_descriptions = [
    {"Column" : "UserID", "Description" : "This field should contain the ID of the user."},
    {"Column" : "TokenNo", "Description" : "This is the Token Number of the contract on which order is to be placed."},
    {"Column" : "InstrumentName", "Description" : "This field contains the type of the instrument. For example, OPTIDX, OPTSTK,FUTIDX, etc."},
    {"Column" : "Symbol", "Description" : "This field contains the Symbol of the security."},
    {"Column" : "ExpiryDate", "Description" : "This should contain valid Expiry Date of the contract."},
    {"Column" : "StrikePrice", "Description" : "This field will contain a valid strike for Options Contract and for Futures Contract it will be -1."},
    {"Column" : "OptionType", "Description" : "This field contains the OptionType identifier. Valid values are - CE -- CALL OPTION, PE -- PUT OPTION, XX -- FUTURES Contract"},
    {"Column" : "Buy/Sell Indicator", "Description" : "This field should contain one of the following values to specify whether the order is a buy or sell order '1' denotes Buy order '2' denotes Sell order."},
    {"Column" : "Volume", "Description" : "This field should contain the order quantity."},
    {"Column" : "Price", "Description" : "This field should contain the price at which the order is placed."},
    {"Column" : "Branch Id", "Description" : "The columns represent identifiers for the branch involved in the transaction."},
    {"Column" : "Trader Id", "Description" : "The columns represent identifiers for the trader involved in the transaction."},
    {"Column" : "Broker Id", "Description" : "The columns represent identifiers for the broker involved in the transaction."},
    {"Column" : "Pro/Client Indicator", "Description" : "This field should contain one of the following values to specify whether the order is entered on behalf of a broker or a trader. '1' represents the client's order, '2' represents a broker's order."}
]
df = pd.DataFrame.from_dict(data=column_descriptions)

st.header("Significance and use of each column")
st.dataframe(df, hide_index=True, use_container_width=True)


sample_data = [{
    "user_id" : "5091379",
    "token_no" : "65093",
    "instrument_name" : "OPTSTK",
    "symbol" : "DLF",
    "expiry_date" : "30/11/2023 14:30",
    "strike_price" : "1145",
    "option_type" : "PE",
    "buy_sell_indicator" : "1",
    "volume" : "1800",
    "price" : "17",
    "branch_id" : "1",
    "trader_id" : "5091379",
    "broker_id" : "79",
    "pro_client_indicator" : "1"
}]
sample_data_df = pd.DataFrame.from_dict(sample_data)

st.header("Sample Data with Explanation")
st.markdown("""The below data indicates that the user with ID 5091379 sold 1800 quantity put option contracts on DLF with a strike price of 1145, expiring on 30/11/2023 at a price of 17. The order was placed  through branch 1, trader 5091379, and broker 79, and the user is identified as a client.""")
st.dataframe(sample_data_df, hide_index=True, use_container_width=True)


st.header("Usage Examples")
st.text("Basic query on the Future and Option market data")
st.code("""
SELECT
    FNO.SYMBOL, 
    FNO.PRICE,
    FNO.INSTRUMENT_NAME,
    FNO.OPTION_TYPE,
    FNO.STRIKE_PRICE,
    FNO.EXPIRY_DATE,
    FNO.BUY_SELL_INDICATOR,
    FNO.VOLUME,
    FNO.PRO_CLIENT_INDICATOR,
    FNO.BRANCH_ID,
    FNO.BROKER_ID,
    B.BROKER_NAME,
    FNO.TOKEN_NO,
    FNO.TRADER_ID,
    T.TRADER_NAME
FROM
    MARKET_DATA.FUTURES_AND_OPTIONS FNO
LEFT JOIN
    MARKET_DATA.BROKERS B
ON
    B.BROKER_ID = FNO.BROKER_ID
LEFT JOIN
    MARKET_DATA.TRADERS T
ON 
    T.TRADER_ID = FNO.TRADER_ID;
""", language='sql')

st.text("Query the market data for a specific trader")
st.code("""
SELECT
    FNO.SYMBOL, 
    FNO.PRICE,
    FNO.INSTRUMENT_NAME,
    FNO.OPTION_TYPE,
    FNO.STRIKE_PRICE,
    FNO.EXPIRY_DATE,
    FNO.BUY_SELL_INDICATOR,
    FNO.VOLUME,
    FNO.PRO_CLIENT_INDICATOR,
    FNO.BRANCH_ID,
    FNO.BROKER_ID,
    B.BROKER_NAME,
    FNO.TOKEN_NO,
    FNO.TRADER_ID,
    T.TRADER_NAME
FROM
    MARKET_DATA.FUTURES_AND_OPTIONS FNO
LEFT JOIN
    MARKET_DATA.BROKERS B
ON
    B.BROKER_ID = FNO.BROKER_ID
LEFT JOIN
    MARKET_DATA.TRADERS T
ON 
    T.TRADER_ID = FNO.TRADER_ID
WHERE 
    FNO.TRADER_ID=5000001;
""", language='sql')

st.text("Query the market data for a specific Broker")
st.code("""
SELECT
    FNO.SYMBOL, 
    FNO.PRICE,
    FNO.INSTRUMENT_NAME,
    FNO.OPTION_TYPE,
    FNO.STRIKE_PRICE,
    FNO.EXPIRY_DATE,
    FNO.BUY_SELL_INDICATOR,
    FNO.VOLUME,
    FNO.PRO_CLIENT_INDICATOR,
    FNO.BRANCH_ID,
    FNO.BROKER_ID,
    B.BROKER_NAME,
    FNO.TOKEN_NO,
    FNO.TRADER_ID,
    T.TRADER_NAME
FROM
    MARKET_DATA.FUTURES_AND_OPTIONS FNO
LEFT JOIN
    MARKET_DATA.BROKERS B
ON
    B.BROKER_ID = FNO.BROKER_ID
LEFT JOIN
    MARKET_DATA.TRADERS T
ON 
    T.TRADER_ID = FNO.TRADER_ID
WHERE 
    FNO.BROKER_ID=1;
""", language='sql')

st.text("Query all trades where expiry date falls in FY 2022-23")
st.code("""
SELECT
    FNO.SYMBOL, 
    FNO.PRICE,
    FNO.INSTRUMENT_NAME,
    FNO.OPTION_TYPE,
    FNO.STRIKE_PRICE,
    FNO.EXPIRY_DATE,
    FNO.BUY_SELL_INDICATOR,
    FNO.VOLUME,
    FNO.PRO_CLIENT_INDICATOR,
    FNO.BRANCH_ID,
    FNO.BROKER_ID,
    B.BROKER_NAME,
    FNO.TOKEN_NO,
    FNO.TRADER_ID,
    T.TRADER_NAME
FROM
    MARKET_DATA.FUTURES_AND_OPTIONS FNO
LEFT JOIN
    MARKET_DATA.BROKERS B
ON
    B.BROKER_ID = FNO.BROKER_ID
LEFT JOIN
    MARKET_DATA.TRADERS T
ON 
    T.TRADER_ID = FNO.TRADER_ID
WHERE 
    FNO.EXPIRY_DATE BETWEEN '2022-04-01' and '2023-03-31';
""", language='sql')

st.text("Query market data only for option")
st.code("""
SELECT
    FNO.SYMBOL, 
    FNO.PRICE,
    FNO.INSTRUMENT_NAME,
    FNO.OPTION_TYPE,
    FNO.STRIKE_PRICE,
    FNO.EXPIRY_DATE,
    FNO.BUY_SELL_INDICATOR,
    FNO.VOLUME,
    FNO.PRO_CLIENT_INDICATOR,
    FNO.BRANCH_ID,
    FNO.BROKER_ID,
    B.BROKER_NAME,
    FNO.TOKEN_NO,
    FNO.TRADER_ID,
    T.TRADER_NAME
FROM
    MARKET_DATA.FUTURES_AND_OPTIONS FNO
LEFT JOIN
    MARKET_DATA.BROKERS B
ON
    B.BROKER_ID = FNO.BROKER_ID
LEFT JOIN
    MARKET_DATA.TRADERS T
ON 
    T.TRADER_ID = FNO.TRADER_ID
WHERE 
    FNO.INSTRUMENT_NAME IN ('OPTSTK', 'OPTIDX');
""", language='sql')

st.text("Query market data only for future")
st.code("""
SELECT
    FNO.SYMBOL, 
    FNO.PRICE,
    FNO.INSTRUMENT_NAME,
    FNO.OPTION_TYPE,
    FNO.STRIKE_PRICE,
    FNO.EXPIRY_DATE,
    FNO.BUY_SELL_INDICATOR,
    FNO.VOLUME,
    FNO.PRO_CLIENT_INDICATOR,
    FNO.BRANCH_ID,
    FNO.BROKER_ID,
    B.BROKER_NAME,
    FNO.TOKEN_NO,
    FNO.TRADER_ID,
    T.TRADER_NAME
FROM
    MARKET_DATA.FUTURES_AND_OPTIONS FNO
LEFT JOIN
    MARKET_DATA.BROKERS B
ON
    B.BROKER_ID = FNO.BROKER_ID
LEFT JOIN
    MARKET_DATA.TRADERS T
ON 
    T.TRADER_ID = FNO.TRADER_ID
WHERE 
    FNO.INSTRUMENT_NAME IN ('FUTSTK', 'FUTIDX');
""", language='sql')

st.text("Query the market data for a specific symbol")
st.code("""
SELECT
    FNO.SYMBOL, 
    FNO.PRICE,
    FNO.INSTRUMENT_NAME,
    FNO.OPTION_TYPE,
    FNO.STRIKE_PRICE,
    FNO.EXPIRY_DATE,
    FNO.BUY_SELL_INDICATOR,
    FNO.VOLUME,
    FNO.PRO_CLIENT_INDICATOR,
    FNO.BRANCH_ID,
    FNO.BROKER_ID,
    B.BROKER_NAME,
    FNO.TOKEN_NO,
    FNO.TRADER_ID,
    T.TRADER_NAME
FROM
    MARKET_DATA.FUTURES_AND_OPTIONS FNO
LEFT JOIN
    MARKET_DATA.BROKERS B
ON
    B.BROKER_ID = FNO.BROKER_ID
LEFT JOIN
    MARKET_DATA.TRADERS T
ON 
    T.TRADER_ID = FNO.TRADER_ID
WHERE 
    FNO.SYMBOL='ITC';
""", language='sql')