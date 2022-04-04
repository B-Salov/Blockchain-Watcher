import classes as cls
import constants as c


def _main():
    # Output table with options
    option = cls.Style.get_option()

    blockchain = cls.BlockchainWatcher(c.INFURA_LINK)
    while option != 0:  # option 0 is Exit
        if option == 1:
            wallet = input('Wallet address --> ')  # 0xDA9dfA130Df4dE4673b89022EE50ff26f6EA73Cf
            currency = input('Currency for conversion (USD, EUR, etc): ')

            # Get current eth price in fiat
            cryptocompare = cls.CryptocompareAPI(currency)
            current_price = cryptocompare.create_request()

            wallet_balance = blockchain.get_wallet_balance(wallet, current_price)

            print(f'Total wallet balance is {wallet_balance[1]} ETH \n'
                  f'In {currency} it is {wallet_balance[0]}')

        elif option == 2:
            block_num = int(input('Number of Block --> '))
            block = blockchain.get_block_info(block_num)

            cls.Style.pretty_print(block)

        elif option == 3:
            # 0xcb4875fdc016717f9243a282a61843063a04e72df5271b2af722b71f72097987
            transaction_id = input('Transaction name --> ')
            transaction = blockchain.get_transaction(transaction_id)

            cls.Style.pretty_print(transaction)

        else:
            print('Invalid option!')

        option = cls.Style.get_option()

    print('Thank you for using this program!')


if __name__ == '__main__':
    _main()
