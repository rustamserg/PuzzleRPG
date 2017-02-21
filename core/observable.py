class Event(object):
    pass


class Observable(object):
    def __init__(self):
        self.callbacks = []

    def subscribe(self, callback):
        self.callbacks.append(callback)

    def fire(self, event, **kwargs):
        e = Event()
        e.source = self
        for k, v in kwargs.items():
            setattr(e, k, v)
        for fn in self.callbacks:
            if fn.__name__ == event:
                fn(e)
