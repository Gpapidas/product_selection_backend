# Products APIs

## Location

- **Views:** `products/views.py`
- **Filters:** `products/filters/`
- **Urls:** `products/urls.py`
- **Serializers:** `products/serializers/`
- **Services:** `products/services/`
- **Tests:** `products/tests/`

## Overview

Provides endpoints for retrieving and selecting products.  
Search queries and selections are stored in session.

## Endpoints

- **GET `/products/`** → Returns a paginated list of products. Supports search and sorting. Requires authentication.
- **POST `/products/{id}/select/`** → Toggles product selection in the user session. Requires authentication.

## Request Parameters (For `/products/`)

- `search` *(optional)* → Filters products by name or description (case-insensitive).
- `ordering` *(optional)* → Sorts by a field (e.g., `"name"`, `"-price"`, `"stock"`). Default: `"-created_at"`.
- `reset_search` *(optional)* → If `"true"`, clears the stored search query in session.


## Notes

- The `"selected"` field in responses indicates whether the product is currently selected in the session.
- Product selection is **stored in session** and **NOT persisted in the database**.
- Search queries are **stored in session** to maintain state across page reloads.
- To reset the stored search query, use `reset_search=true` in the request.

## Additional Documentation

- For **detailed API documentation**, visit `/swagger/`.
- For **session handling details**, see `sessions.md`.

