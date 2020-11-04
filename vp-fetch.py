#import required library
import bullet
import pandas as pd
import requests
import io
import base64
# request header
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html"
}

def decode_data(coded_string):
    """return the base64 decoded string"""
    return base64.b64decode(coded_string)


def write_to_file(name, coded_string):
    """write the data to the .ovpn file"""
    name = f"{name}.ovpn"

    with open(name, "wb") as fd:
        fd.write(coded_string)

    print(f"\nThe file is saved with the name => {name}")



if __name__ == "__main__":

    # fetching data

    csv_content = requests.get(
        "http://www.vpngate.net/api/iphone/", headers=headers, timeout=10
    ).content

    # reading the csv data
    data = pd.read_csv(io.BytesIO(csv_content), skiprows=1)

    #remove the nan
    data = data.loc[data['CountryLong'].notna()]


    # Available coutries
    print(set(data["CountryLong"]))

    # select the name of counrty
    select = input("\nEnter the desired country name from list above :")

    selected = data[data["CountryLong"] == select]

    if not selected.empty:
        # sort according to the Score
        selected = selected.sort_values("Score")


        # select the first entry with the best score
        base_code = selected.iloc[0, -1]


        # decode base code
        base_code = decode_data(base_code)

        # write the *.ovpn file in current dir
        write_to_file(select, base_code)
    else:
        print("Incorrect country name !!")
