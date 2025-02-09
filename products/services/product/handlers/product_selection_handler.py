def handle_product_selection(session, product):
    selected_products = session.get("selected_products", [])

    if product.id in selected_products:
        selected_products.remove(product.id)
        message = f"Product {product.id} deselected successfully"
    else:
        selected_products.append(product.id)
        message = f"Product {product.id} selected successfully"

    session["selected_products"] = selected_products
    session.modified = True

    return message, product
