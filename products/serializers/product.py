from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField()
    derived_from_saved_search = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "stock", "selected", "derived_from_saved_search"]

    def get_selected(self, obj):
        """
        Determines if the product is selected based on session data.
        """
        request = self.context.get("request")
        if request and request.session:
            selected_products = request.session.get("selected_products", [])
            return obj.id in selected_products
        return False

    def get_derived_from_saved_search(self, obj):
        """
        Returns `derived_from_saved_search` if applicable.
        """
        return self.context.get("derived_from_saved_search")
