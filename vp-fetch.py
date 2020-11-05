#import required library
from bullet import Bullet
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
    try:
        csv_content = requests.get(
            "http://www.vpngate.net/api/iphone/", headers=headers, timeout=10
        ).content
    except requests.exceptions.ConnectionError:
        print("Unable to fetch data !!")
        print("Try again !!")
        exit(0)


    # reading the csv data
    data = pd.read_csv(io.BytesIO(csv_content), skiprows=1)

    #remove the nan
    data = data.loc[data['CountryLong'].notna()]


    # Available coutries
    country_list = list(set(data["CountryLong"]))

    select_country = Bullet(
        prompt = "\nPlease choose the country: ",
        choices = country_list,
        indent = 0,
        align = 5,
        margin = 2,
        shift = 0,
        bullet = "",
        pad_right = 5,
        return_index = True
    )

    result = select_country.launch()
    print("You chose country:", result[0])


    selected = data[data["CountryLong"] == result[0]]

    if not selected.empty:
        # sort according to the Score
        selected = selected.sort_values("Score")


        # select the first entry with the best score
        base_code = selected.iloc[0, -1]


        # decode base code
        base_code = decode_data(base_code)

        # write the *.ovpn file in current dir
        write_to_file(result[0], base_code)
    else:
        print("Incorrect country name !!")
