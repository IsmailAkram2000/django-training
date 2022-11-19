from django_filters import rest_framework as filters
from .models import Albums

class AlbumsFilters(filters.FilterSet):

    class Meta:
        model = Albums
        fields = {
            'cost': ['gte', 'lte'],
            'name': ['icontains']
        } 