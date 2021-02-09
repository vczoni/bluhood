import numpy as np
from bluhood.key import Key
from bluhood.constants import ORDS
from bluhood.utils import ChrOrdManager


class Crypto:
    def __init__(self, key):
        self.set_key(key)
        self._rng()

    def set_key(self, key):
        if not isinstance(key, Key):
            raise Exception('key must be from :class Key:.')
        else:
            self.key = key

    def _rng(self):
        seed = genseed(self.key._key_ord)
        self._ords = ORDS.copy()
        np.random.seed(seed)
        np.random.shuffle(self._ords)
        self._chr_ord_manager = ChrOrdManager(self._ords)

    def encrypt(self, message):
        raw_ord_message = self._chr_ord_manager.chr2ord(message)
        key_ord = self.key._key_ord
        seed = genseed(key_ord)
        ord_message = pollute(raw_ord_message, seed, self._chr_ord_manager)
        ord_encrypted = e(ord_message, key_ord)
        return self._chr_ord_manager.ord2chr(ord_encrypted)

    def decrypt(self, message):
        ord_message = self._chr_ord_manager.chr2ord(message)
        key_ord = self.key._key_ord
        ord_decrypted = d(ord_message, key_ord)
        return self._chr_ord_manager.ord2chr(ord_decrypted).replace(chr(7), '')


def genseed(k):
    i0 = int(11 + len(k) / 4)
    i = i0 - 3
    for o, kk in enumerate(k):
        i += kk * o % (i0 + int(o / 3))
    return i


def pollute(m, r, comng):
    np.random.seed(r*3)
    s = np.random.randint(int(len(m)/2) + 1) + 1
    t = []
    while sum(t) < len(m):
        gv = int(np.random.exponential(s))
        t.append(gv)
    c = 0
    nm = []
    for k, i in enumerate(t):
        lc = c
        c += i
        if k == len(t)-1:
            ic = []
        else:
            ic = comng.chr2ord(chr(7))
        nm += m[lc:c] + ic
    return nm


def e(m, k):
    x = []
    for i, f in enumerate(m):
        x.append(E(i, f, k, len(m)))
    return x


def d(w, k):
    x = []
    for j, q in enumerate(w):
        x.append(D(j, q, k, len(w)))
    return [i for i in x if i != 1008]


def E(i, j, k, l):
    return (j + k[i*l % len(k)]) % len(ORDS)


def D(l, m, n, p):
    v = m - n[l*p % len(n)]
    while v < 0:
        v += len(ORDS)
    return v
