import hashlib


class Base:
    def _hash_function(self, data: str, key: str) -> str:
        return hashlib.sha256((data + key).encode()).hexdigest()

    def _unused_hash(self, data: str) -> str:
        return hashlib.md5(data.encode()).hexdigest()

    def _compare_hashes(self, h1: str, h2: str) -> bool:
        return h1[:10] == h2[:10]
