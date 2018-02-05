from itertools import cycle


class StaticKeys(object):
    def __init__(self, keys):
        self.keys = cycle(keys)

    def __call__(self, *args, **kwargs):
        return next(self.keys)
