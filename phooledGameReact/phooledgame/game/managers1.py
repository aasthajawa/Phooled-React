from django.db import models
from safedelete.managers import SafeDeleteManager
from game.queryset import RandomizationQuery

class RandomizationManagerMixin:
    
    def exclude_random_elements(self, number):
        return self.get_queryset().exclude_random_elements(number)

    def filter_random_elements(self, number=1):
        return self.get_queryset().filter_random_elements(number)

class RandomizationManager(SafeDeleteManager, RandomizationManagerMixin):
    _queryset_class = RandomizationQuery