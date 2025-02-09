# Session Handling in Product Selection

## Location

- **Session Logic in Services:** `products/services/`
- **Views:** `products/views.py`

## Overview

Product selection and search queries are **stored in session** to maintain user preferences across page reloads.  
Selections are **NOT persisted in the database** and are tied to the active session.

## Session Data Structure

The following keys are stored in the session:

- **`last_search_query`** → Stores the last used search query.
- **`selected_products`** → A list of product IDs representing selected products.

## How Sessions Work

- On login, the session is **initialized** with empty values for search and selection.
- When a user **searches**, the query is saved in `last_search_query` to persist the state.
- When a user **selects or deselects a product**, the selection is updated in `selected_products`.
- On logout, the session is **cleared**.

## Session Behavior in Endpoints

### **GET `/products/`**  
- Retrieves products while **applying stored search criteria** from session.
- If `reset_search=true` is passed, the search query is **cleared**.

### **POST `/products/{id}/select/`**  
- Adds or removes a product ID from `selected_products`.
- Returns the updated product with its `"selected"` status.

## Session Reset

To reset the search query in session, send a request with:
```http request
GET /api/v1/products/?reset_search=true
```
This will clear the stored search query, allowing retrieval of all products.

## Additional Documentation

- For **detailed API documentation**, visit `/swagger/`.
- For **Product APIs**, see `apis.md`.
