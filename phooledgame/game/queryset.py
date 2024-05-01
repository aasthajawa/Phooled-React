import random

from django.db.models import QuerySet, Max, Min
from safedelete.queryset import SafeDeleteQueryset

class RandomizationQueryMixin:
    
    def random_elements(self, number):
        assert number <= 100000, 'too large'
        max_pk = self.aggregate(Max('pk'))['pk__max']
        min_pk = self.aggregate(Min('pk'))['pk__min']
            
        ids = set()
        # Return only the number 
        if self.count() > number:
            while len(ids) < number:
                next_pk = random.randint(min_pk, max_pk)
                while next_pk in ids:
                    next_pk = random.randint(min_pk, max_pk)
                try:
                    found = self.get(pk=next_pk)
                    ids.add(found.pk)
                except self.model.DoesNotExist:
                    pass
        else:
            ids = self.only('pk')

        return ids

    def exclude_random_elements(self, number):
        selected_ids = self.random_elements(number)
        return self.exclude(pk__in=selected_ids)

    def filter_random_elements(self, number=1):
        selected_ids = self.random_elements(number)
        return self.filter(pk__in=selected_ids)

class RandomizationQuery(SafeDeleteQueryset, RandomizationQueryMixin):
	pass
