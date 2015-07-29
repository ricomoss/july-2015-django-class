

class BaseVendor:
    def _order_handler(self, *args, **kwargs):
        raise NotImplementedError

    def _cancel_order_handler(self, *args, **kwargs):
        raise NotImplementedError

    def _payment_handler(self, *args, **kwargs):
        raise NotImplementedError

    def handler(self, choice, *args, **kwargs):
        func = getattr(self, '_{}_handler'.format(choice))
        if func:
            return func(*args, **kwargs)
