# Authentication System

## Overview

This project uses **JWT-based authentication**. Users log in with their email and password, and the system automatically registers them if they don't exist.

### **Authentication Flow**
1. **Login / Auto-Registration:**  
   - If a user provides a valid email and password, they are authenticated.
   - If the email does not exist, a new user is automatically created.
   - A **JWT access token** and a **refresh token** are issued upon login.

2. **Token Refresh:**  
   - Access tokens expire after a certain period.
   - Users can refresh their access token using the refresh token.

3. **Logout:**  
   - Logging out invalidates the refresh token.
   - The access token expires naturally.

## Authentication Endpoints

| Method | Endpoint             | Description                            | Auth Required |
|--------|----------------------|----------------------------------------|--------------|
| POST   | `/auth/login/`       | Login or auto-register a user         | ❌ No       |
| POST   | `/auth/logout/`      | Logout and invalidate refresh token   | ✅ Yes       |
| POST   | `/auth/token/refresh/` | Refresh the access token              | ❌ No       |

## Token Format

- **Access Token:** Used to authenticate API requests.
- **Refresh Token:** Used to obtain a new access token.

## Error Handling

- **Invalid Credentials:** A new user is created if the email does not exist.
- **Expired/Invalid Token:** Requests with expired or invalid tokens will return `401 Unauthorized`.

## Notes

- **Session Persistence:** Tokens must be stored securely on the client-side.
- **Blacklist Handling:** Refresh tokens are invalidated on logout.

For detailed API specs, check **`/swagger`**.
