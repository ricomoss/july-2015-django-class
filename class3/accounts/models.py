from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts import constants
from common.models import BaseModel


class User(BaseModel, AbstractUser):
    loyalty_level = models.CharField(
        max_length=6, choices=constants.LOYALTY_LEVEL_CHOICES)
