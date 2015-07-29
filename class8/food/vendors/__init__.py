import inspect

from food.vendors.base import BaseVendor
from food.vendors.flavor_of_the_month import FlavorOfTheMonthVendor
from food.vendors.tasty_food_yum_yum import TastyFoodYumYumVendor
from food.vendors.we_got_yo_food import WeGotYoFoodVendor

VENDOR_OPTIONS = [
    (vendor.__name__, vendor.name) for vendor in locals().values()
    if inspect.isclass(vendor) and vendor is not BaseVendor
    and issubclass(vendor, BaseVendor)
]
VENDOR_OPTIONS.sort()
