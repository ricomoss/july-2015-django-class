from food.vendors.base import BaseVendor


class FlavorOfTheMonthVendor(BaseVendor):
    name = 'Flavor of the Month'

    def _order_handler(self, *args, **kwargs):
        msg = 'Made order from {}'.format(self.name)
        return {'response': msg, 'order_id': '12345'}

    def _cancel_order_handler(self, *args, **kwargs):
        msg = 'Canceled order from {}'.format(self.name)
        return {'response': msg, 'verification_id': '54321'}

    def _payment_handler(self, *args, **kwargs):
        msg = 'Payment submitted for {}'.format(self.name)
        return {'response': msg, 'transaction_id': '13579'}
