import random
import itertools
from optparse import make_option

from fixtureless.factory import create
from django.core.management.base import BaseCommand

from accounts import models as accounts_models
from common import models as common_models
from food import models as food_models


class Command(BaseCommand):
    help = 'Populate the local DB with review data.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--review_count',
            default=5,
            type=int,
            help='The number of reviews you want in your system. (default=50)',
        )
        parser.add_argument(
            '--clear_db',
            action='store_true',
            default=False,
            help='Clear the database to start fresh.',
        )


    REVIEW_TITLES = ['Bleh', 'Pass', 'Meh', 'Yummy', 'AMAZING!']
    REVIEW_CONTENTS = [
        'I got sick.', 'I did not like this.', 'The definition of average.',
        'Very tasty.  I highly recommend!',
        'As if it were made by the heavens']

    def __init__(self):
        common_models.Review.objects.all().delete()
        super().__init__()

    def _generate_reviews(self, review_count):
        initial_list = list()
        for _ in itertools.repeat(None, review_count):
            initial_list.append({
                'title': random.choice(self.REVIEW_TITLES),
                'content': random.choice(self.REVIEW_CONTENTS),
                'rating': random.randint(1, 5),
                'user': random.choice(accounts_models.User.objects.all()),
                'meal': random.choice(food_models.Meal.objects.all()),
            })
        create(common_models.Review, initial_list)

    def handle(self, *args, **options):
        if options['clear_db']:
            return

        review_count = options['review_count']
        self._generate_reviews(review_count)
