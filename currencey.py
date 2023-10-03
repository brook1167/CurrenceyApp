import json
import requests
from requests import HTTPError

def convertor():
  Action_command = input('Enter your choice ')

  if Action_command == 'c'.lower():
    fromInput = str(input('Enter from input '))
    toInput = str(input('Enter your to input '))
    amount = int(input('Enter amount '))

    url = f"your_api_website_with_api_key"{fromInput}/{toInput}/{amount}"
    try:
      response = requests.get(url)
      response.raise_for_status()
      result = response.json()
    except HTTPError as http_error:
     print(http_error)
    else:
     print(
       f"\n{amount} {fromInput.upper()} is {toInput.upper()} {result['conversion_rate'] * amount} at {result['time_last_update_utc']}\n")
  else:
    exit()

while True:
  print('----------- Currency Converter App-------------')
  print('PRESS C TO USE CURRENCY CONVERTER APP')
  print('PRESS ANY KEY TO EXIT')
  print('-------------------------')
  convertor()

