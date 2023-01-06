import django_filters
from CartApp.models import Products

class productfilter(django_filters.FilterSet):
    class Meta:
        model=Products
        fields={
               
                "price":["lt"]
                }