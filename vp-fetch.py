#import required library
import bullet
import pandas as pd
import requests

# request header
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html"
}

if __name__ == "__main__":

    # fetching data

    csv_content = requests.get(
        "http://www.vpngate.net/api/iphone/", headers=headers, timeout=10
    ).content

    # reading the csv data
    data = pd.read_csv(io.BytesIO(csv_content), skiprows=1)

    # Available coutries
    print(list(data["CountryShort"]))