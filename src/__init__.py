from src.base58 import validate_base58_checksum
from src.web3_utils import web3_validate_address

currencies_mapping = {
    "eth": {
        "name": "Ethereum",
        "validation_method": web3_validate_address
    },
    "etc": {
        "name": "Ethereum Classic",
        "validation_method": web3_validate_address
    },
    "btc": {
        "name": "Bitcoin",
        "validation_method": validate_base58_checksum,
        "validation_args": {'prefix_versions': {'p2pkh': [0], 'p2sh': [5]}}
    }
}

# todo: Address validation method
# todo: Address format detection method
# todo: Probabilistic address detection
# todo: Address generation/Sample Addresses for each format
# todo: Error case helper texts
# todo: Exception Handling
