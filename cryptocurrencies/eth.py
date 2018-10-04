from cryptocurrencies.base_class import BaseCryptocurrencyClass
from cryptocurrencies.web3_utils import is_address


class ETH(BaseCryptocurrencyClass):
    name = "Ethereum"

    @staticmethod
    def is_address(address):
        return is_address(address)

    def parse_address_format(self):
        pass
