from .handlers.product_selection_handler import handle_product_selection


class ProductService:

    @staticmethod
    def product_selection(session, product):
        """
        Toggles the selection of a product in session storage.
        """
        return handle_product_selection(session, product)
