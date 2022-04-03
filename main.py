"""
This is a blockchain watcher, which can get wallet balance
and convert it into fiat.

Project Plan:
1) Add block processing
1.1) Get gas, difficulty etc.
2) Add transaction processing
2.1) Gas, difficulty, sender, recipient
3) Create UI
"""

import requests
from web3 import Web3


# CONNECTING TO BLOCKCHAIN
infura_url = ''  # Your infura link
web3 = Web3(Web3.HTTPProvider(infura_url))


class CryptocompareAPI:
    def __init__(self, currency):
        self.currency = currency

    def create_request(self):
        eth_url = 'https://min-api.cryptocompare.com/data/' \
                  f'price?fsym=ETH&tsyms=ETH,{self.currency}'
        current_eth_price = requests.get(eth_url).json()

        return int(current_eth_price[self.currency])


def _main():
    wallet = input('Wallet address --> ')  # 0xDA9dfA130Df4dE4673b89022EE50ff26f6EA73Cf
    currency = input('Currency for conversion (USD, EUR, etc): ')

    cryptocompare = CryptocompareAPI(currency)
    current_price = cryptocompare.create_request()

    get_balance = web3.eth.get_balance(wallet)
    convert_to_eth = web3.fromWei(get_balance, 'ether')

    result = int(int(convert_to_eth) * current_price)  # ETH * Fiat price

    print(f"Total wallet balance is {convert_to_eth} ETH \n"
          f"In {currency} it is {result}")


if __name__ == '__main__':
    _main()
