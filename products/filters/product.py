import django_filters
from django.db.models import Q

from products.models import Product


class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="filter_search")
    ordering = django_filters.OrderingFilter(fields=["id", "name", "description", "price", "stock", "created_at"])

    class Meta:
        model = Product
        fields = ["ordering"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(description__icontains=value))
