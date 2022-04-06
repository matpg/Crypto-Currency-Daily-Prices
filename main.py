from pyrsistent import b
import streamlit as st
import yfinance as yf
from PIL import Image
from urllib.request import urlopen
from datetime import datetime, timedelta

# CONFIG PAGE
st.set_page_config(page_title="Crypto Prices", page_icon="📈")

# TITLES AND SUBTITLES
st.title("₿ Crypto Daily Prices 🤑")
st.subheader("Main Dashboard")

# CRYPTO TICKER
BTC_DATA = yf.Ticker("BTC-USD")
ETH_DATA = yf.Ticker("ETH-USD")
LTC_DATA = yf.Ticker("LTC-USD")
BCH_DATA = yf.Ticker("BCH-USD")

# FECTH DATA FROM yfinance
BTC_DATA_HIST = BTC_DATA.history(period="1y")
ETH_DATA_HIST = ETH_DATA.history(period="1y")
LTC_DATA_HIST = LTC_DATA.history(period="1y")
BCH_DATA_HIST = BCH_DATA.history(period="1y")

# FETCH DATA FOR DATAFRAME
# today date
today = datetime.today().strftime("%Y-%m-%d")
# yesterday date
yesterday = datetime.today() - timedelta(days=1)
BTC = yf.download("BTC-USD", start=yesterday, end=today)
ETH = yf.download("ETH-USD", start=yesterday, end=today)
LTC = yf.download("LTC-USD", start=yesterday, end=today)
BCH = yf.download("BCH-USD", start=yesterday, end=today)

#VIEWS

#BITCOIN VIEW
st.write("BITCOIN ($)")
# load bitcoin symbol Image
img = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/200x200/1.png"))
st.image(img, width=100)
# table
st.table(BTC)
# line chart
st.write("1 Month Bitcoin Price History")
st.line_chart(BTC_DATA_HIST[['Close', 'High', 'Low']][-30:])

st.write("1 Year Bitcoin Price History")
st.line_chart(BTC_DATA_HIST[['Close', 'High', 'Low']])

#Etherium VIEW
st.write("Etherium ($)")
# load etherium symbol Image
img = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/200x200/1027.png"))
st.image(img, width=100)
# table
st.table(ETH)
# line chart
st.write("1 Month Etherium Price History")
st.line_chart(ETH_DATA_HIST[['Close', 'High', 'Low']][-30:])

st.write("1 Year Etherium Price History")
st.line_chart(ETH_DATA_HIST[['Close', 'High', 'Low']])

#Litecoin VIEW
st.write("Litecoin ($)")
# load litecoin symbol Image
img = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/200x200/2.png"))
st.image(img, width=100)
# table
st.table(LTC)
# line chart
st.write("1 Month Litecoin Price History")
st.line_chart(LTC_DATA_HIST[['Close', 'High', 'Low']][-30:])

st.write("1 Year Litecoin Price History")
st.line_chart(LTC_DATA_HIST[['Close', 'High', 'Low']])

#Bitcoin Cash VIEW
st.write("Bitcoin Cash ($)")
# load bitcoin cash symbol Image
img = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/200x200/1831.png"))
st.image(img, width=100)
# table
st.table(BCH)
# line chart
st.write("1 Month Bitcoin Cash Price History")
st.line_chart(BCH_DATA_HIST[['Close', 'High', 'Low']][-30:])

st.write("1 Year Bitcoin Cash Price History")
st.line_chart(BCH_DATA_HIST[['Close', 'High', 'Low']])

# Sidebar to another page
st.sidebar.header("Crypto Prices Features")
st.sidebar.info("Crypto Prices is a web application that shows you the current price of the crypto currencies.")
with st.spinner("Loading..."):
    choice = st.sidebar.radio("Crypto Prices Features", ['Main Page', 'Forecast Pricing'])
st.sidebar.success("You selected: {}".format(choice))

