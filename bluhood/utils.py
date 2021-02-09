import numpy as np


class ChrOrdManager:
    def __init__(self, ordlist):
        self._ordlist = ordlist

    def ord2chr(self, ords):
        return ''.join([chr(self._ordlist[i]) for i in ords])

    def chr2ord(self, chrs):
        return [np.where(self._ordlist == ord(c))[0][0] for c in chrs]
