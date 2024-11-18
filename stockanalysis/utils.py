from bs4 import BeautifulSoup
import requests

def scrape_stock_data(symbol, exchange):
    if exchange == 'NASDAQ':
        url = f"https://finance.yahoo.com/quote/{symbol}"
    elif exchange == 'NSE':
        symbol = symbol + '.NS'
        url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch'
    else:
        print("Unsupported exchange.")
        return None

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Use get_text() if element is found, else return 'N/A'
            current_price = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})
            current_price = current_price.text if current_price else 'N/A'
            
            price_changed = soup.find("fin-streamer", {"data-field": "regularMarketChange"})
            price_changed = price_changed.text if price_changed else 'N/A'
            
            percentage_changed = soup.find("fin-streamer", {"data-field": "regularMarketChangePercent"})
            percentage_changed = percentage_changed.text if percentage_changed else 'N/A'
            
            previous_close = soup.find('td', {'data-test': 'PREV_CLOSE-value'})
            previous_close = previous_close.text if previous_close else 'N/A'
            
            week_52_range = soup.find('td', {'data-test': 'FIFTY_TWO_WK_RANGE-value'})
            week_52_range = week_52_range.text if week_52_range else 'N/A'
            
            if week_52_range != 'N/A' and ' - ' in week_52_range:
                week_52_low, week_52_high = week_52_range.split(' - ')
            else:
                week_52_low, week_52_high = 'N/A', 'N/A'
            
            market_cap = soup.find('td', {'data-test': 'MARKET_CAP-value'})
            market_cap = market_cap.text if market_cap else 'N/A'
            
            pe_ratio = soup.find('td', {'data-test': 'PE_RATIO-value'})
            pe_ratio = pe_ratio.text if pe_ratio else 'N/A'
            
            dividend_yield = soup.find('td', {'data-test': 'DIVIDEND_AND_YIELD-value'})
            dividend_yield = dividend_yield.text if dividend_yield else 'N/A'

            # Return the scraped stock data
            stock_response = {
                'current_price': current_price,
                'previous_close': previous_close,
                'price_changed': price_changed,
                'percentage_changed': percentage_changed,
                'week_52_low': week_52_low,
                'week_52_high': week_52_high,
                'market_cap': market_cap,
                'pe_ratio': pe_ratio,
                'dividend_yield': dividend_yield,
            }

            print(stock_response)  # Optional: to check output while developing
            return stock_response

        else:
            print(f"Failed to retrieve data: Status code {response.status_code}")
            return None

    except Exception as e:
        print(f'Error scraping the data: {e}')
        return None
