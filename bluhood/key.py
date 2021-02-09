import numpy as np
from bluhood.constants import KEYORDS, B, M
from bluhood.utils import ChrOrdManager


chr_ord_manager = ChrOrdManager(KEYORDS.copy())


class Key:
    def __init__(self, key=None):
        self.key_exchanger = KeyExchanger(self)
        self._key = key

    def __repr__(self):
        return self._key

    @property
    def _key_ord(self):
        return chr_ord_manager.chr2ord(self._key)

    def set_key(self, key):
        self._key = key

    def set_random_key(self):
        self._key = self.generate_random()

    def set_random_seed(self, seed):
        np.random.seed(seed)

    def generate_random(self):
        size = np.random.randint(1024, 2048, 1)[0]
        ords_arr = np.random.randint(0, len(KEYORDS), size)
        ords = list(ords_arr)
        return chr_ord_manager.ord2chr(ords)

    def copy(self):
        return Key(self._key)

    def save(self, path):
        with open(path, 'w') as f:
            f.write(self._key)

    def load(self, path):
        with open(path, 'r') as f:
            key = f.read()
        return Key(key)


class KeyExchanger:
    def __init__(self, outer):
        self._outer = outer

    @property
    def original(self):
        return self._outer._key

    @property
    def external(self):
        key_ord = chr_ord_manager.chr2ord(self.original)
        external_ord = encrypt(key_ord)
        return chr_ord_manager.ord2chr(external_ord)

    def get_original(self):
        return Key(self.original)

    def get_external(self):
        return Key(self.external)

    def get_shared(self, foreign_external):
        external_ord = chr_ord_manager.chr2ord(self.external)
        foreign_external_ord = foreign_external._key_ord
        shared_ord = encrypt(external_ord, foreign_external_ord)
        shared = chr_ord_manager.ord2chr(shared_ord)
        return Key(shared)


def encrypt(x_key_ord, y_key_ord=None):
    if y_key_ord is None:
        return [B ** x % M for x in x_key_ord]
    else:
        return [B ** (x * y) % M for x, y in zip(x_key_ord, y_key_ord)]
