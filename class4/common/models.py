from django.db import models

from common import constants


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Review(BaseModel):
    title = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField(choices=constants.RATING_CHOICES)
    meal = models.ForeignKey('food.Meal')
    user = models.ForeignKey('accounts.User')

    @staticmethod
    def average_rating(meal):
        reviews = Review.objects.filter(meal=meal)
        if reviews.count() == 0:
            return 'Not Rated'
        total_rating = 0
        for review in reviews:
            total_rating += review.rating
        average = float(total_rating) / reviews.count()
        return '{:.1f} Stars'.format(average)
