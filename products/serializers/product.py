from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "stock", "selected"]

    def get_selected(self, obj):
        """
        Determines if the product is selected based on session data.
        """
        request = self.context.get("request")
        if request and request.session:
            selected_products = request.session.get("selected_products", [])
            return obj.id in selected_products
        return False
