from web3 import Web3


def web3_validate_address(address: str, **kwargs):
    if address[:2] != "0x":
        return False
    return Web3.isAddress(address.lower())
