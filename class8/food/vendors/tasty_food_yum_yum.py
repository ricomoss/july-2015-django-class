from food.vendors.base import BaseVendor


class TastyFoodYumYumVendor(BaseVendor):
    name = 'Tasty Food Yum Yum'

    def _order_handler(self, *args, **kwargs):
        msg = 'Made order from {}'.format(self.name)
        return {'response': msg, 'order_id': 'a1b2c3'}

    def _cancel_order_handler(self, *args, **kwargs):
        msg = 'Canceled order from {}'.format(self.name)
        return {'response': msg, 'verification_id': '3c2b1a'}

    def _payment_handler(self, *args, **kwargs):
        msg = 'Payment submitted for {}'.format(self.name)
        return {'response': msg, 'transaction_id': 'a2b4c6'}
