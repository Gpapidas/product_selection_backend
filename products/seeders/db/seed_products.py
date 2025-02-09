from decimal import Decimal

from products.models import Product


def seed_products():
    """
    Seeds 10 book records into the database.
    Ensures products are created only if they don't already exist.
    """
    products_data = [
        ("The Lord of the Rings: The Fellowship of the Ring", "First book of J.R.R. Tolkien's epic fantasy trilogy.",
         19.99, 100),
        ("The Lord of the Rings: The Two Towers", "Second book in The Lord of the Rings trilogy.", 20.99, 90),
        ("The Lord of the Rings: The Return of the King", "Final book in the legendary trilogy by J.R.R. Tolkien.",
         21.99, 85),
        ("The Hobbit", "J.R.R. Tolkien's prequel to The Lord of the Rings, following Bilbo Baggins' adventure.", 18.99,
         120),
        ("Harry Potter and the Sorcerer’s Stone", "First book in J.K. Rowling's Harry Potter series.", 14.99, 150),
        ("Harry Potter and the Chamber of Secrets", "Second book in the Harry Potter series.", 15.99, 140),
        ("Harry Potter and the Prisoner of Azkaban", "Third book in the Harry Potter series.", 16.99, 130),
        (
            "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "Classic fantasy novel by C.S. Lewis.",
            17.99,
            110),
        ("Percy Jackson: The Lightning Thief", "First book in Rick Riordan's Percy Jackson & The Olympians series.",
         13.99, 100),
        ("Percy Jackson: The Sea of Monsters", "Second book in the Percy Jackson series.", 14.49, 95),
    ]

    created_products = []

    for name, description, price, stock in products_data:
        product, created = Product.objects.get_or_create(
            name=name,
            defaults={"description": description, "price": Decimal(price), "stock": stock}
        )
        created_products.append({"id": product.id, "created": created})

    return created_products
