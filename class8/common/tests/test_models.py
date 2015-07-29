from django.test import TestCase
from fixtureless import Factory

from common import models
from food import models as food_models


class ReviewTestCase(TestCase):
    def setUp(self):
        self.factory = Factory()

    def test_average_rating(self):
        meal = self.factory.create(food_models.Meal)
        review1_init = {'rating': 1, 'meal': meal}
        review2_init = {'rating': 2, 'meal': meal}
        self.factory.create(models.Review, (review1_init, review2_init))

        expected_results = '1.5 Stars'
        self.assertEqual(models.Review.average_rating(meal), expected_results)
