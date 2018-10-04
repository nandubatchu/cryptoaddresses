from abc import ABCMeta, abstractmethod


class BaseCryptocurrencyClass(ABCMeta):
    BTC_BASE58_DICT = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def is_address(self, address: str):
        pass

    @abstractmethod
    def parse_address_format(self):
        pass