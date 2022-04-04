import requests
from web3 import Web3


class CryptocompareAPI:
    def __init__(self, currency):
        self.currency = currency

    def create_request(self):
        eth_url = 'https://min-api.cryptocompare.com/data/' \
                  f'price?fsym=ETH&tsyms=ETH,{self.currency}'
        current_eth_price = requests.get(eth_url).json()

        return int(current_eth_price[self.currency])


class BlockchainWatcher:
    def __init__(self, infura_link):
        # Connecting to blockchain
        self.web3 = Web3(Web3.HTTPProvider(infura_link))

    def get_wallet_balance(self, wallet, current_price):
        get_balance = self.web3.eth.get_balance(wallet)
        in_eth = self.web3.fromWei(get_balance, 'ether')  # Convert wei to eth

        result = int(int(in_eth) * current_price)  # ETH * Fiat price

        return [result, in_eth]

    def get_block_info(self, block_num):
        block = self.web3.eth.get_block(block_num)

        block_info = {
            'Difficulty': block['difficulty'],
            'Gas Limit': block['gasLimit'],
            'Gas Used': block['gasUsed'],
            'Hash': block['hash'],
            'Parent Hash': block['parentHash'],
            'Miner': block['miner'],
            'Size': block['size']
        }

        print(str(block['hash']))

        return block_info

    def get_transaction(self, transaction_id):
        transaction = self.web3.eth.get_transaction_receipt(transaction_id)
        
        transaction_info = {
            'Block Number': transaction['blockNumber'],
            'Sender': transaction['from'],
            'Recipient': transaction['to'],
            'Status': 'Success' if transaction['status'] == 1 else 'In Processing',
            'Hash': transaction['transactionHash']
        }

        return transaction_info


class Style:
    @staticmethod
    def get_option():
        # Main menu
        text = '''
[1] Get Wallet balance 
[2] Get Block info
[3] Get Transaction info
[0] Exit the program'''
        print(text)

        option = int(input('Your option --> '))

        return option

    @staticmethod
    def pretty_print(data):
        # Pretty print for dictionary
        print('\n')
        for key, item in data.items():
            print(f'{key}  -  {item}')
