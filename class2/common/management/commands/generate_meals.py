import random
import itertools

from fixtureless import Factory
from django.core.management.base import BaseCommand

from food import models as food_models


class Command(BaseCommand):
    help = 'Populate the local DB with meal data.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--meal_count',
            default=5,
            help='The number of meals you want in your system. (default=5)',
        )
        parser.add_argument(
            '--item_count',
            default=25,
            help='The number of food items you want in your system. '
                 '(default=25)',
        )
        parser.add_argument(
            '--clear_db',
            action='store_true',
            default=False,
            help='Clear the database to start fresh.',
        )

    MEAL_NAMES = ['Hamburger', 'Enchilada', 'Spaghetti', 'Burrito', 'Omelette']
    ITEM_NAMES = [
        'beef patty', 'lettuce', 'bun', 'cheese', 'pickles', 'tomato',
        'mustard', 'ketchup', 'mayonnaise', 'tortilla', 'sauce', 'chicken',
        'rice', 'beans', 'noodles', 'meat balls', 'egg', 'avocado', 'mushroom'
    ]

    def __init__(self):
        food_models.Meal.objects.all().delete()
        food_models.Item.objects.all().delete()
        self.factory = Factory()
        super().__init__()

    def _generate_meals(self, meal_count):
        initial_list = list()
        for _ in itertools.repeat(None, meal_count):
            initial_list.append({
                'name': random.choice(self.MEAL_NAMES),
            })
        meals = self.factory.create(food_models.Meal, initial_list)
        for meal in meals:
            item_count = random.randint(
                1, food_models.Item.objects.all().count())
            for _ in range(0, item_count):
                item = random.choice(food_models.Item.objects.all())
                meal.items.add(item)

    def _generate_items(self, item_count):
        for item_name in self.ITEM_NAMES:
            if food_models.Item.objects.all().count() >= item_count:
                break
            self.factory.create(food_models.Item, {'name': item_name})

    def handle(self, *args, **options):
        if options['clear_db']:
            return

        item_count = options['item_count']
        self._generate_items(item_count)

        meal_count = options['meal_count']
        self._generate_meals(meal_count)
