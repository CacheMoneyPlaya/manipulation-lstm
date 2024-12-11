import httpx

if __name__ == '__main__':
    r = httpx.get('https://www.binance.com/futures/data/openInterestHist?symbol=btcusdt&period=5m&limit=25')
    print(r.text)
