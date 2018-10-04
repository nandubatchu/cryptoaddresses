from hashlib import sha256

BTC_DICT = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
XRP_DICT = "rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz"


def base58_custom(address: str, length: int, dict: str):
    n = 0
    for char in address:
        n = n * 58 + dict.index(char)
    return n.to_bytes(length, 'big')


def double_sha256(data):
    return sha256(sha256(data).digest()).digest()


def parse_base58_address_with_checksum(address: str, **kwargs):
    prefix_versions = kwargs.get('prefix_versions')
    if not prefix_versions:
        return False, None

    length = kwargs.get('length', 25)
    dictionary = kwargs.get('dictionary', BTC_DICT)
    hash_algorithm = kwargs.get('hash_algorithm', double_sha256)

    try:
        address_bytes = base58_custom(address, length, dictionary)[:-4]
        checksum_bytes = base58_custom(address, length, dictionary)[-4:]
    except Exception:
        return False, None

    if hash_algorithm(address_bytes)[:4] != checksum_bytes:
        return False, None

    prefix_version = base58_custom(address, length, dictionary)[0]
    for address_type, prefix_values in prefix_versions.items():
        if prefix_version in prefix_values:
            return True, address_type

    return False, None


def validate_base58_checksum(address: str, **kwargs):
    valid, detected_address_type = parse_base58_address_with_checksum(address=address, **kwargs)
    return valid
