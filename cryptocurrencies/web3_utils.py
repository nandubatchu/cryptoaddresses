from web3 import Web3


def is_address(address: str):
    if address[:2] != "0x":
        return False
    return Web3.isAddress(address.lower())
