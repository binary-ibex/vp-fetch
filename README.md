# VP-FETCH

Simple python script to generate .ovpn config file. It fetch free vpn server information from https://www.vpngate.net/en/ .

## Installation
```
pip3 install -r requirements.txt

```

## Use
```python

python3 vp-fetch.py

```

Select the country from the list and press enter.

![Select the country](images/image_1.png)

<country_name>.ovpn file will be save in current working dir. In my case I select Canada.

![file saved with selected country name](images/image_2.png)

file in the folder

![folder](images/image_3.png)

To connect to the vpn server use the command

```sh

sudo openvpn Canada.ovpn

```
## System

- Ubuntu 20.04
- python 3.7.9 and 3.8.5


## Requirements
- **required python libraries**

  - bullet
  - pandas
  - bs4
  - requests

- **openvpn client**
